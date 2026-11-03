"""Scores the chapter models in resources/sci-kit against chapter_gold.json, questions labelled by hand from real
papers. A question spanning several topics lists each chapter accepted as correct.

Usage: python evaluate_chapters.py [--split dev|test|all] [--misses]
"""
import argparse
import collections
import json
import os
import sys

BASE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..", "src"))
sys.path.append(BASE_PATH)

from main.utils import get_question_texts, get_level_and_chapter, formatText


def predicted_label(text: str, paper: int, definitions: dict) -> str | None:
    """The chapter name get_level_and_chapter picks for a question, the same way the pipeline does."""
    paper_type = "IGCSE" if "chapters" in definitions else "A-level"
    level, chapter = get_level_and_chapter(formatText(text), paper, paper_type, definitions)
    if not chapter:
        return None
    if level == "IGCSE":
        return definitions["chapters"][chapter - 1]
    if level == "AS":
        return definitions["ASChapters"][chapter - 1]
    return definitions["A2Chapters"][chapter - 1 - len(definitions["ASChapters"])]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Score the chapter models against the hand-labelled questions.")
    parser.add_argument("--split", default="all", choices=["dev", "test", "all"])
    parser.add_argument("--misses", action="store_true", help="Also print every wrong prediction")
    args = parser.parse_args()

    with open(f"{BASE_PATH}/main/definitions.json") as f:
        definitionsData = json.load(f)
    with open(f"{BASE_PATH}/main/sci-kit/chapter_gold.json") as f:
        gold = json.load(f)

    scores = collections.defaultdict(lambda: [0, 0])
    for pdf_name, entry in gold.items():
        if args.split != "all" and entry["split"] != args.split:
            continue
        code = pdf_name[:4]
        paper = int(pdf_name.split("_")[3][0])
        texts = get_question_texts(f"{BASE_PATH}/resources/full_pdfs/{code}/{pdf_name}.pdf")
        for number, accepted in entry["questions"].items():
            label = predicted_label(texts[int(number) - 1], paper, definitionsData[code])
            key = f"{code} {definitionsData[code]['subjectName']}"
            scores[key][1] += 1
            scores[key][0] += label in accepted
            if args.misses and label not in accepted:
                print(f"{pdf_name} Q{number}: predicted {label!r}, expected {accepted}")

    for key, (correct, total) in sorted(scores.items()):
        print(f"{key:28} {correct:3}/{total:<3} {correct / total:.0%}")
    correct, total = (sum(values) for values in zip(*scores.values()))
    print(f"{'total':28} {correct:3}/{total:<3} {correct / total:.0%}")
