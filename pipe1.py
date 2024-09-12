from transformers import pipeline

# Create a sentiment-analysis pipeline
classifier = pipeline('sentiment-analysis', model='distilbert-base-uncased-finetuned-sst-2-english')

# Example text
text = "I love using Hugging Face transformers!"

# Get prediction
result = classifier(text)
print(result)
