from transformers import pipeline

generator = pipeline("text-generation", model="distilgpt2")

res = 