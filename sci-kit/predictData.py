from joblib import load
import getFormattedTextfromPdf

# Load the saved pipeline from disk
pipeline = load(r"D:\python_projects\teachmegcse\python_files\sci-kit\IGeco.joblib")

data = """
 production possibility curve
"""
data = getFormattedTextfromPdf.formatText(data)

# Use the loaded pipeline to make predictions on new data
test_data = [data]
predicted_labels2 = pipeline.predict(test_data)
predicted_labels = pipeline.predict_proba(test_data)
print(predicted_labels)
print(predicted_labels2)


def predict (data, model):
    pipeline = load(f"{model}.joblib")
    data = getFormattedTextfromPdf.formatText(data)
    test_data = [data]
    predicted_labels = pipeline.predict(test_data)
    return predicted_labels

def printLabel(data, model):
    pipeline = load(f"{model}.joblib")
    data = getFormattedTextfromPdf.formatText(data)
    test_data = [data]
    predicted_labels = pipeline.predict(test_data)
    return predicted_labels