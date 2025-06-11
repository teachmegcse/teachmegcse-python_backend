from joblib import load
import getFormattedTextfromPdf

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