import openai

openai.api_key = "your-openai-api-key"   

def generate_answer_with_gpt3(relevant_chunks):
    context = " ".join(relevant_chunks)
    
    response = openai.Completion.create(
        engine="text-davinci-003",   
        prompt=context,
        max_tokens=150  
    )
    
    return response.choices[0].text.strip()
