import  os
import openai

openai.api_key = os.getenv('')

response = openai.Completion.create(
    model = 'text-davinci-003',
    prompt= 'write an email',
    max_tokens = 256,
    temprature = 0.7,
    top_p=1,
    frecuency_penalty = 0,
    presence-penalty = o

)