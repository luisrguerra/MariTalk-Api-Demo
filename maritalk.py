import requests
from colorama import Fore

api_url = "https://chat.maritaca.ai/api/chat/inference"

api_key = ""  # Coloque aqui a sua chave de API (ex: "10035481...").

def create_auth_header(api_key):
    return {
        "authorization": f"Key {api_key}"
    }


def create_request_data(messages, do_sample=True, max_tokens=200, temperature=0.7, top_p=0.95):
    return {
        "messages": messages,
        "do_sample": do_sample,
        'max_tokens': max_tokens,
        "temperature": temperature,
        "top_p": top_p,
    }

def post_request(api_url, request_data, headers):
    return requests.post(
        api_url,
        json=request_data,
        headers=headers
    )

def check_rate_limit(response):
    if response.status_code == 429:
        return True
    else:
        return False

def get_maritalk_response(request_data):
  auth_header = create_auth_header(api_key)
  response = post_request(api_url, request_data, auth_header)

  if check_rate_limit(response):
     print("Limite de taxa atingido, tente novamente em breve")
     return None
  elif response.ok:
    data=response.json()
    return data["answer"]

  else:
    response.raise_for_status()
    return None

# Inicialize a lista de mensagens
messages = []

while True:
   
  user_message = input(Fore.BLUE + "Você: ")
  
  # Adicione a mensagem do usuário ao histórico
  messages.append({"role": "user", "content": user_message})

  request_data = create_request_data(messages)

  # Obtenha a resposta do assistente
  assistant_response = get_maritalk_response(request_data)
  
  # Adicione a resposta do assistente ao histórico
  messages.append({"role": "assistant", "content": assistant_response})

  print(Fore.GREEN + "MariTalk: " + assistant_response)