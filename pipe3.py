from transformers import pipeline

classifier = pipeline("zero-shot-classification", device=1)

res = classifier(

    "this device has machintosh operating system; So, it must be very useful",

##------consider above sentence, which catagory that it including follow areas-------##
    candidate_labels=("education", "comedy", "militery"),

)

print(res)