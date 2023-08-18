import requests

url = "https://chat.maritaca.ai/api/chat/inference"

messages = [
    {"role": "user", "content": "bom dia, esta é a mensagem do usuario"},
    {"role": "assistant", "content": "bom dia, esta é a resposta do assistente"},
    {"role": "user", "content": "Você pode me falar quanto é 25 + 27?"},
]

API_KEY = ""  # Coloque aqui a sua chave de API (ex: "10035481...").

auth_header = {
    "authorization": f"Key {API_KEY}"
}

request_data = {
  "messages": messages,
  "do_sample": True,
  'max_tokens': 200,
  "temperature": 0.7,
  "top_p": 0.95,
}


def get_maritalk_response(request_data, headers):
  response = requests.post(
      url,
      json=request_data,
      headers=headers
  )

  if response.status_code == 429:
    print("rate limited, tente novamente em breve")

  elif response.ok:
    data=response.json()
    print(data["answer"])

  else:
    response.raise_for_status()


get_maritalk_response(request_data, auth_header)