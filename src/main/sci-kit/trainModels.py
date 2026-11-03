from sklearn.naive_bayes import ComplementNB
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from joblib import dump


def chunk_lines(text, lines=12):
    """Splits syllabus text into pieces of a few lines, each a separate training example. Helps when a chapter's text
    is short and its wording is close to other chapters' (mathematics)."""
    rows = [row for row in text.split("\n") if row.strip()]
    return ["\n".join(rows[i : i + lines]) for i in range(0, len(rows), lines)]


def train(data, label, output_path):
    # Each chapter has about one document of syllabus text, and chapters differ a lot in length. Complement naive Bayes
    # and TF-IDF cope with that much better than MultinomialNB on raw counts, see chapter_gold.json
    pipeline = Pipeline(
        [
            ("vectorizer", TfidfVectorizer(sublinear_tf=True)),
            ("classifier", ComplementNB()),
        ]
    )

    pipeline.fit(data, label)

    dump(pipeline, output_path)
