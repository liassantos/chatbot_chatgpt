import json
import requests
import os
from dotenv import load_dotenv

load_dotenv()

def abrir_arquivo() -> dict:
  with open(os.getenv('CAMINHO_JSON'), 'r', encoding='utf-8') as arquivo:
    dados = json.load(arquivo)
  return dados


def busca_contato(contato: str) -> str:
    
  dados = abrir_arquivo()

  resultado = list(filter(lambda p: p.get("nome", None).startswith(contato.title()), dados["contatos"]))

  if not resultado:
    return None
  else:
    return str(resultado[0])


def insere_contato(nome: str, telefone: str, endereco: str) -> str:
  dados = abrir_arquivo()

  if len(telefone) < 13:
    return "Erro: número de telefone inválido. Deve ter ao menos 13 caracteres (ex: DDI+DDD+número)."

  novo_contato = {
      "nome": nome.title(),
      "telefone": telefone,
      "endereco": endereco.title()
  }
    
  dados['contatos'].append(novo_contato)

  with open(os.getenv('CAMINHO_JSON'), 'w', encoding='utf-8') as arquivo:
     json.dump(dados, arquivo, indent=4, ensure_ascii=False)

  return "Contato adicionado."


def envia_msg(telefone: str, mensagem: str) -> str:
  BASE_URL = os.getenv('URL_WPP')
  CMD = "chat"
  ID_AUTOMACAO = os.getenv('ID')
  
  params = {
    "cmd": CMD,
    "id": ID_AUTOMACAO,
    "to": f"{telefone}@c.us",
    "msg": mensagem
}

  response = requests.get(url=BASE_URL, params=params, timeout=10)

  print(response.status_code)

  if response.status_code == 200:
    return response.json()["type"]
  else:
    return response.text





    
