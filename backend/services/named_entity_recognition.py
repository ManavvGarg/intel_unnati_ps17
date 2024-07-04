from transformers import pipeline

class NamedEntityRecognizer:
    def __init__(self):
        self.ner = pipeline("ner", grouped_entities=True)

    def recognize(self, text):
        entities = self.ner(text)
        return entities
