from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import Pipeline
from joblib import dump

# Example training data and labels
def train(data, label):
    train_data = data
    train_labels = label

    # Create a pipeline that includes preprocessing, vectorization, and classification
    pipeline = Pipeline([
        ('vectorizer', CountVectorizer()),
        ('classifier', MultinomialNB())
    ])

    # Fit the pipeline to the training data and labels
    pipeline.fit(train_data, train_labels)

    # Save the trained pipeline to disk
    dump(pipeline, 'IGphy.joblib')
