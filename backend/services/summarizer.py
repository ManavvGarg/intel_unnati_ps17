from transformers import pipeline
from .contract_parser import read_file

class Summarizer:
    def __init__(self):
        self.summarizer = pipeline("summarization")

    def summarize(self, text):
        text_read = read_file(text)
        summary = self.summarizer(text_read, max_length=1500, min_length=200, num_beams=1)
        return summary[0]['summary_text']
