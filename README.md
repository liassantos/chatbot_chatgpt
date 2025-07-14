
# 🤖 Chatbot

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
annotated-types==0.7.0
anyio==4.9.0
certifi==2025.7.9
charset-normalizer==3.4.2
distro==1.9.0
dotenv==0.9.9
exceptiongroup==1.3.0
git-filter-repo==2.47.0
h11==0.16.0
httpcore==1.0.9
httpx==0.28.1
idna==3.10
jiter==0.10.0
openai==1.95.1
pydantic==2.11.7
pydantic_core==2.33.2
python-dotenv==1.1.1
requests==2.32.4
sniffio==1.3.1
tqdm==4.67.1
typing-inspection==0.4.1
typing_extensions==4.14.1
urllib3==2.5.0
```

## ✍️ Autora

Desenvolvido por [Lia Santos](https://github.com/liassantos)
