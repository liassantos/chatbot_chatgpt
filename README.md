
# 🤖 Chatbot - v1

Este é um chatbot em Python que gerencia uma **agenda de contatos** e permite **enviar mensagens automatizadas via WhatsApp**.  
Utiliza a API da OpenAI com integração de funções (`tools`) para executar ações como busca, inserção e envio de mensagens.  
É ideal para automatizar interações simples com uma base de contatos armazenada em JSON.

## 🧩 Funcionalidades

- 🔍 Buscar contatos pelo nome  
- ➕ Inserir novos contatos com nome, telefone e endereço  
- 💬 Enviar mensagens via API do WhatsApp  
- 🤖 Interação inteligente com o usuário usando a OpenAI (GPT-4o-mini)  
- 🗂️ Armazenamento seguro dos dados e credenciais  

## 🛠️ Tecnologias utilizadas

- Python 3.8+
- [OpenAI API](https://platform.openai.com/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)
- [requests](https://pypi.org/project/requests/)
- API externa de envio de mensagens WhatsApp

## 📁 Estrutura de pastas

```
chatbot-v1/
├── data/               # Arquivos de dados (como contatos.json)
│   ├── contatos.json
├── src/
│   ├── chatgpt.py      # Script principal do chatbot (interface CLI + integração OpenAI)
│   └── functions.py    # Funções auxiliares (busca, inserção, envio)
├── .env                # Arquivo com variáveis de ambiente
├── .gitignore
├── README.md
└── requirements.txt
```

## ⚙️ Como executar

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/chatbot-v1.git
cd chatbot-v1
```

### 2. Crie o arquivo `.env`

```env
API_KEY=sua-chave-da-openai
CAMINHO_JSON=./data/contatos.json
URL_WPP=https://sua-api-de-whatsapp.com/send
ID=seu-id-da-automacao
```

### 3. Crie o arquivo `contatos.json` em `./data` com o conteúdo:

```json
{
  "contatos": []
}
```

### 4. Instale as dependências

```bash
pip install -r requirements.txt
```

### 5. Execute o chatbot

```bash
python src/chatgpt.py
```

## 💡 Exemplo de uso

```
=== Chatbot de contatos ===
Você: inserir contato Ana +5511999999999 Rua das Flores, 123
Assistente: Contato adicionado.
Você: buscar Ana
Assistente: {'nome': 'Ana', 'telefone': '+5511999999999', 'endereco': 'Rua Das Flores, 123'}
Você: sair
```

## 🧠 Como funciona?

O chatbot usa a API da OpenAI com a funcionalidade `tools` para decidir, com base nas mensagens do usuário, qual função Python deve ser executada:

- `abrir_arquivo` → Lê os dados do arquivo JSON  
- `busca_contato` → Busca um contato por nome  
- `insere_contato` → Adiciona um novo contato  
- `envia_msg` → Envia mensagem para um telefone via API  

O histórico da conversa é mantido e atualizado dinamicamente.

## 📦 requirements.txt

```txt
openai>=1.0.0
python-dotenv>=1.0.0
requests>=2.31.0
```

## ✍️ Autora

Desenvolvido por [Lia Santos](https://github.com/liassantos)
