import sys
import os
import shutil
import zipfile

# Define BASE_PATH relative to this test file location
# From src/tests/, go up one level to src/
BASE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Import the app directly
sys.path.append(BASE_PATH)
from main.classified.api import app
from fastapi.testclient import TestClient

def test_generate_pdf_and_save_response():
    """Test the generate-pdf endpoint and save the response to a file"""

    # Set up test directories and files using relative paths
    test_image_src = os.path.join(BASE_PATH, "resources", "images", "IGCSE", "chemistry", "mcq", "chemistry_p1_1.jpg")
    expected_dir = os.path.join(BASE_PATH, "resources", "images", "IGCSE", "chemistry", "p1")
    output_dir = os.path.join(BASE_PATH, "resources", "pdfs", "classified")

    # Create directories
    os.makedirs(expected_dir, exist_ok=True)
    os.makedirs(output_dir, exist_ok=True)

    # Copy test image to expected location (p1_api.py looks for images in IGCSE/p1/ subdirectory)
    expected_image_path = os.path.join(expected_dir, "chemistry_p1_1.jpg")
    if os.path.exists(test_image_src):
        shutil.copy2(test_image_src, expected_image_path)
        print(f"[OK] Copied test image to {expected_image_path}")
    else:
        print(f"[ERROR] Test image not found at {test_image_src}")
        return

    test_data = {
        "questionData": [
            {
                "Level": "IGCSE",
                "Answer": "A",
                "Chapter": "Test Chapter",
                "Subject": "chemistry",
                "pdfName": "test.pdf",
                "paperNumber": 1,
                "questionName": "chemistry_p1_1.jpg",
                "questionText": "Test question"
            }
        ]
    }

    print("Starting FastAPI TestClient...")
    client = TestClient(app)
    response = client.post("/generate-pdf/", json=test_data)

    print(f"Response status: {response.status_code}")
    print(f"Response headers: {dict(response.headers)}")

    if response.status_code == 200:
        # Check if it returns a file (ZIP archive)
        content_type = response.headers.get("content-type", "")
        print(f"Content type: {content_type}")

        if "application/zip" in content_type or "application/x-zip-compressed" in content_type:
            # Save the response content to a file in the tests directory
            output_file = os.path.join(os.path.dirname(__file__), "test_output.zip")
            with open(output_file, "wb") as f:
                f.write(response.content)

            print(f"Response saved to: {output_file}")
            print(f"File size: {len(response.content)} bytes")

            # Verify that the file was created and has content
            if os.path.exists(output_file) and os.path.getsize(output_file) > 0:
                print("Test passed: ZIP file created successfully")
                # Extract PDFs from ZIP and save them separately
                try:
                    with zipfile.ZipFile(output_file, 'r') as zip_ref:
                        file_list = zip_ref.namelist()
                        print(f"ZIP contents: {file_list}")
                        # Extract each PDF to the tests directory
                        tests_dir = os.path.dirname(__file__)
                        for file_name in file_list:
                            if file_name.endswith('.pdf'):
                                extracted_path = os.path.join(tests_dir, file_name)
                                with open(extracted_path, 'wb') as f:
                                    f.write(zip_ref.read(file_name))
                                print(f"Extracted PDF: {extracted_path}")
                except Exception as e:
                    print(f"Could not extract ZIP contents: {e}")
            else:
                print("Test failed: ZIP file not created or empty")
        else:
            print(f"Test failed: Expected ZIP file, got {content_type}")
            print(f"Response content preview: {response.content[:200]}...")
    else:
        print(f"Test failed: HTTP {response.status_code}")
        print(f"Response: {response.text}")

def main():
    print("Running P1 API Test...")
    test_generate_pdf_and_save_response()
    print("Test completed")

if __name__ == "__main__":
    main()

if __name__ == "__main__":
    main()