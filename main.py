import openai
import datetime
import sys
import json
from IPython import embed
def init_openai():
    openai.api_key = 'ADD YOUR OWN API_KEY HERE, ASK ChatGPT HOW TO GET ONE IF YOU DON'T KNOW'

messages=[
        {"role": "system", "content": "I'm a ChatBot!"},
]

def chat(text):
    global messages
    messages.append({"role": "user", "content": text})
#     return openai.ChatCompletion.create(
#       model="gpt-3.5-turbo",
#       messages=messages,
#       max_tokens=3000,
#         stream = True,
#     n=5,
#     stop=None,
#     temperature=1.0,
#     )
    return openai.ChatCompletion.create(
    model='gpt-3.5-turbo',
    messages=messages,
    temperature=0,
)

    
def chat_with_gpt():
    global messages
    print("Chat with GPT")
    try:
        with open("log.json", "r") as f:
            messages = json.load(f)
    except:
        pass
    print("\n".join((str(i) for i in messages)))
    # Chat with GPT
    while True:
        # Get user input
        now = datetime.datetime.now()
        d = f"{now.strftime('%Y-%m-%d %H:%M:%S')}"
        user_input = input(f"[{d}] User: ")
        if "delete our chat log" in user_input:
            print("all deleted")
            messages.clear()
        # Generate response
        response = chat(user_input)
        # Print response
#         embed()
        result = response.choices[0]['message']
        print(f"[{d}] {result['role']}: {result['content']}")    
        messages.append(result)
        with open("log.json", "w") as f:
            json.dump(messages, f)
        with open("log.txt", "a") as f:
            f.write(f"[{d}] User: {user_input}\n[{d}] {result['role']}: {result['content']}\n----------------------\n\n")

if __name__ == "__main__":
    init_openai()
    chat_with_gpt()
