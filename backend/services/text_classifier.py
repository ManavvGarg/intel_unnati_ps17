from transformers import pipeline

class TextClassifier:
    def __init__(self):
        self.classifier = pipeline("sentiment-analysis")

    def classify(self, text):
        classification = self.classifier(text)
        return classification[0]
