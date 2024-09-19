from transformers import pipeline

# Create a sentiment-analysis pipeline
classifier = pipeline('sentiment-analysis', model='distilbert-base-uncased-finetuned-sst-2-english', device=0)

# Example text
text = "I know that dog, So is it try to bit me"

# Get prediction
result = classifier(text)
print(result)
