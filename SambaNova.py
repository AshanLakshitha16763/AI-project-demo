import os
import openai

client = openai.OpenAI(
   
#-------api_key=os.environ.get("41f6da69-a987-48ab-b424-a71cced2e3d1")---------#

##----- you can give the API key (in SambaNova)directly like this------## 
#-------No need to use "api_key= os.environ.get("Here API key")" function

    api_key="41f6da69-a987-48ab-b424-a71cced2e3d1",
    base_url="https://api.sambanova.ai/v1",
)

response = client.chat.completions.create(
    model='Meta-Llama-3.1-8B-Instruct',
    messages=[{"role":"system","content":"You are a helpful assistant"},{"role":"user","content":"Hello"}],
    temperature =  0.1,
    top_p = 0.1
)

print(response.choices[0].message.content)
      