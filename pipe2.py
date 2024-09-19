from transformers import pipeline

generator = pipeline("text-generation", model="distilgpt2", device=1)

res = generator(
    "In this scenario help you to",
    max_length=30,
   
    ##------this value mean, type of sentence that I want to get------
    num_return_sequences=2,

    ##------to address the future warning-------
    clean_up_tokenization_spaces=True, 

    ##------This use to handle input trunction explicitly-------
    truncation=True
)
print(res)