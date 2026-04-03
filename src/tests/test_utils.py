import os
import sys
import json
from unittest.mock import patch
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from main.utils import cleanup, extract_paper_number, formatText, get_level_and_chapter


def test_cleanup_removes_files():
    """Test that cleanup() removes files from target directories"""
    # Create a test file in one of the actual directories
    test_file = os.path.join(os.path.dirname(__file__), "..", "resources", "images", "test_images", "currentPdfImages", "test.txt")
    
    # Create file if directory exists
    os.makedirs(os.path.dirname(test_file), exist_ok=True)
    with open(test_file, "w") as f:
        f.write("test content")
    
    assert os.path.exists(test_file), "Test file was not created"
    
    # Run cleanup
    cleanup()
    
    # Verify file was deleted
    assert not os.path.exists(test_file), "Test file was not deleted by cleanup()"


def test_extract_paper_number():
    """Test that extract_paper_number() correctly extracts paper number from filename"""
    # Test with the given input
    result = extract_paper_number('9702_m20_qp_51.pdf')
    assert result == 5, f"Expected 5, but got {result}"


def test_formatText_basic_processing():
    """Test that formatText() performs basic text processing operations"""
    # Test lowercase conversion
    assert formatText("HELLO WORLD") == "hello world"
    
    # Test punctuation removal
    assert formatText("Hello, world!") == "hello world"
    
    # Test digit removal
    assert formatText("Hello 123 world") == "hello world"
    
    # Test combined operations
    assert formatText("HELLO, 123 WORLD!") == "hello world"


def test_formatText_command_word_removal():
    """Test that formatText() removes Cambridge command words"""
    # Test individual command words (note: stemming affects results)
    assert formatText("analyse this problem") == "thi problem"  # "this" -> "thi", "problem" unchanged
    
    # Test other command words
    assert formatText("calculate the answer") == "the answer"
    assert formatText("describe the process") == "the process"


def test_formatText_stemming():
    """Test that formatText() applies stemming to words"""
    # Test basic stemming
    assert formatText("running") == "run"
    assert formatText("jumped") == "jump"
    assert formatText("studies") == "studi"


def test_formatText_combined_operations():
    """Test that formatText() handles complex text with all operations"""
    input_text = "CALCULATE the ANSWER! Running studies, 123 problems."
    result = formatText(input_text)
    
    # Check that punctuation and digits are removed
    assert "!" not in result
    assert "123" not in result
    assert "CALCULATE" not in result
    
    # Check that text is lowercase
    assert result == result.lower()
    
    # Check that command word is removed
    assert "calcul" not in result  # stemmed version of calculate


def load_definitions_data():
    """Load the actual definitions.json data for testing"""
    definitions_path = os.path.join(os.path.dirname(__file__), "..", "main", "definitions.json")
    with open(definitions_path, 'r') as f:
        return json.load(f)


@patch('main.utils.predict')
def test_get_level_and_chapter_igcse_with_real_data(mock_predict):
    """Test get_level_and_chapter() for IGCSE using real definitions data"""
    # Mock the predict function to return a known chapter
    mock_predict.return_value = "Motion, forces and energy"
    
    # Load real definitions data
    definitions_data = load_definitions_data()
    physics_data = definitions_data["0625"]  # IGCSE Physics
    
    # Test IGCSE case
    level, chapter_num = get_level_and_chapter(
        formatted_text="force mass acceleration",
        paper_num=3,  # Long paper
        paperType="IGCSE",
        currentDefinitionsData=physics_data
    )
    
    assert level == "IGCSE"
    assert chapter_num == 1  # "Motion, forces and energy" is at index 0, so chapter_num = 0 + 1 = 1
    mock_predict.assert_called_once_with("force mass acceleration", "igphy.joblib")


@patch('main.utils.predict')
def test_get_level_and_chapter_as_level_with_real_data(mock_predict):
    """Test get_level_and_chapter() for AS level using real definitions data"""
    # Mock the predict function
    mock_predict.return_value = "Kinematics"
    
    # Load real definitions data
    definitions_data = load_definitions_data()
    physics_data = definitions_data["9702"]  # A-Level Physics
    
    # Test AS case (paper_num 1 is in ASpapers)
    level, chapter_num = get_level_and_chapter(
        formatted_text="velocity displacement time",
        paper_num=1,
        paperType="A-level",
        currentDefinitionsData=physics_data
    )
    
    assert level == "AS"
    assert chapter_num == 2  # "Kinematics" is at index 1, so chapter_num = 1 + 1 = 2
    mock_predict.assert_called_once_with("velocity displacement time", "asphy.joblib")


@patch('main.utils.predict')
def test_get_level_and_chapter_a2_level_with_real_data(mock_predict):
    """Test get_level_and_chapter() for A2 level using real definitions data"""
    # Mock the predict function
    mock_predict.return_value = "Quantum physics"
    
    # Load real definitions data
    definitions_data = load_definitions_data()
    physics_data = definitions_data["9702"]  # A-Level Physics
    
    # Test A2 case (paper_num 4 is in A2papers)
    level, chapter_num = get_level_and_chapter(
        formatted_text="photons electrons energy levels",
        paper_num=4,
        paperType="A-level",
        currentDefinitionsData=physics_data
    )
    
    assert level == "A2"
    # "Quantum physics" is at index 10 in A2Chapters, so chapter_num = 10 + 1 + len(ASChapters) = 10 + 1 + 11 = 22
    assert chapter_num == 22
    mock_predict.assert_called_once_with("photons electrons energy levels", "a2phy.joblib")


@patch('main.utils.predict')
def test_get_level_and_chapter_unknown_chapter_with_real_data(mock_predict):
    """Test get_level_and_chapter() when predicted chapter is not in labels using real data"""
    # Mock the predict function to return unknown chapter
    mock_predict.return_value = "Unknown Physics Topic"
    
    definitions_data = load_definitions_data()
    physics_data = definitions_data["0625"]  # IGCSE Physics
    
    # Test with unknown chapter
    level, chapter_num = get_level_and_chapter(
        formatted_text="unknown physics concept",
        paper_num=3,
        paperType="IGCSE",
        currentDefinitionsData=physics_data
    )
    
    assert level == "IGCSE"
    assert chapter_num == 0  # Unknown chapter returns 0


if __name__ == "__main__":
    test_cleanup_removes_files()
    test_extract_paper_number()
    test_formatText_basic_processing()
    test_formatText_command_word_removal()
    test_formatText_stemming()
    test_formatText_combined_operations()
    
    # Also run the mocked tests when called directly
    from unittest.mock import patch
    
    print("\nRunning mocked tests...")
    
    # Test IGCSE with real data
    with patch('main.utils.predict') as mock_predict:
        mock_predict.return_value = "Motion, forces and energy"
        definitions_data = load_definitions_data()
        igcse_data = definitions_data["0625"]
        level, chapter_num = get_level_and_chapter('force mass acceleration', 3, 'IGCSE', igcse_data)
        assert level == 'IGCSE' and chapter_num == 1
        print("✓ IGCSE test passed")
    
    # Test AS with real data
    with patch('main.utils.predict') as mock_predict:
        mock_predict.return_value = "Kinematics"
        definitions_data = load_definitions_data()
        alevel_data = definitions_data["9702"]
        level, chapter_num = get_level_and_chapter('velocity displacement time', 1, 'A-level', alevel_data)
        assert level == 'AS' and chapter_num == 2
        print("✓ AS test passed")
    
    # Test A2 with real data
    with patch('main.utils.predict') as mock_predict:
        mock_predict.return_value = "Quantum physics"
        definitions_data = load_definitions_data()
        alevel_data = definitions_data["9702"]
        level, chapter_num = get_level_and_chapter('photons electrons energy levels', 4, 'A-level', alevel_data)
        expected_chapter_num = 10 + 1 + len(alevel_data['ASChapters'])  # 10 + 1 + 11 = 22
        assert level == 'A2' and chapter_num == expected_chapter_num
        print("✓ A2 test passed")
    
    # Test unknown chapter
    with patch('main.utils.predict') as mock_predict:
        mock_predict.return_value = "Unknown Physics Topic"
        definitions_data = load_definitions_data()
        igcse_data = definitions_data["0625"]
        level, chapter_num = get_level_and_chapter('unknown physics concept', 3, 'IGCSE', igcse_data)
        assert level == 'IGCSE' and chapter_num == 0
        print("✓ Unknown chapter test passed")
    
    print("\n All tests passed!")
