import requests

api_url = "https://chat.maritaca.ai/api/chat/inference"

messages = [
    {"role": "user", "content": "bom dia, esta é a mensagem do usuario"},
    {"role": "assistant", "content": "bom dia, esta é a resposta do assistente"},
    {"role": "user", "content": "Qual é o sentido da vida?"},
]

API_KEY = ""  # Coloque aqui a sua chave de API (ex: "10035481...").

auth_header = {
    "authorization": f"Key {API_KEY}"
}

def create_request_data(messages, do_sample=True, max_tokens=200, temperature=0.7, top_p=0.95):
    return {
        "messages": messages,
        "do_sample": do_sample,
        'max_tokens': max_tokens,
        "temperature": temperature,
        "top_p": top_p,
    }

request_data = create_request_data(messages)

def post_request(api_url, request_data, headers):
    return requests.post(
        api_url,
        json=request_data,
        headers=headers
    )

def get_maritalk_response(request_data, headers):
  response = post_request(api_url, request_data, headers)

  if response.status_code == 429:
    print("rate limited, tente novamente em breve")

  elif response.ok:
    data=response.json()
    print(data["answer"])

  else:
    response.raise_for_status()


get_maritalk_response(request_data, auth_header)