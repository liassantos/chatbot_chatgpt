import os
from dotenv import load_dotenv 
from openai import OpenAI
import json
import functions as f

load_dotenv()

client = OpenAI(api_key=os.getenv('API_KEY'))


tools = [
    {
        "type": "function",
        "function": {
            "name": "abrir_arquivo",
            "description": "Lê os dados dos contatos que estão contidos no arquivo em json.",
            "parameters": {}
        }
    },
    {
        "type": "function",
        "function":{
            "name": "busca_contato",
            "description": "Busca o contato que está contido no arquivo em json de acordo com o nome informado pelo usuário.",
            "parameters": {
                "type": "object",
                "properties": {
                    "contato": {
                        "type": "string",
                        "description": "Nome de pessoa, por exemplo: Maria."
                    }
                },
                "required": [
                    "contato"
                ],
                "additionalProperties": False
            },
        },        
    },
    {
        "type": "function",
        "function":{
            "name": "insere_contato",
            "description": "Insere dados de um novo contato no arquivo em json de acordo com o nome, endereço e telefone informados pelo usuário.",
            "parameters": {
                "type": "object",
                "properties": {
                    "nome": {"type": "string", "description": "Nome do contato"},
                    "telefone": {"type": "string", "description": "Telefone com DDI e DDD"},
                    "endereco": {"type": "string", "description": "Endereço completo"}
                },
                "required": ["nome", "telefone", "endereco"],
                "additionalProperties": False
            },
        },        
    },
    {
        "type": "function",
        "function":{
            "name": "envia_msg",
            "description": "Envia uma mensagem via whatsapp para o telefone fornecido de um dos contatos que estão no arquivo json.",
            "parameters": {
                "type": "object",
                "properties": {
                    "telefone": {"type": "string", "description": "Telefone com DDI e DDD"},
                    "mensagem": {"type": "string", "description": "Mensagem com a informação que o usuário irá informar"}
                },
                "required": ["telefone", "mensagem"],
                "additionalProperties": False
            },
        },        
    }
]


messages = [
    {
        "role": "system",
        "content": (
            "Você é um assistente que gerencia uma agenda de contatos. "
            "Quando o usuário pedir para enviar uma informação de um contato para outro, "
            "você deve primeiro buscar os dois contatos pelo nome (origem e destino) "
            "e depois usar a função 'envia_msg' para enviar a mensagem. "
            "O conteúdo da mensagem deve conter os dados solicitados (telefone ou endereço) "
            "de forma amigável. Continue a conversa até concluir todas as etapas necessárias."
            "Você precisa pedir validação do usuário para acessar a função 'envia_msg'"
            "quando você terminar de executar as funções, deve perguntar ao usuário se ele quer continuar"
            "ou se não, para isso informe que o usuário deve escrever 'sair', caso ele queira parar."
        )
    }
] 

def main():
    print("=== Chatbot de contatos ===")
    while True:
        user_input = input("Você: ")
        if user_input.lower() in ["sair", "exit", "quit"]:
            print("Encerrando o chatbot.")
            break

        messages.append({"role": "user", "content": user_input})

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            tools=tools,
            tool_choice="auto"
        )

        message = response.choices[0].message

        if message.tool_calls:
        # Se o modelo quiser chamar uma função:
            for tool_call in message.tool_calls:
                func_name = tool_call.function.name
                args = json.loads(tool_call.function.arguments)

                

                if func_name == "busca_contato":
                    resultado = f.busca_contato(args["contato"])
                    if resultado:
                        resposta = resultado
                    else:
                        resposta = f"Não encontrei o contato '{args['contato']}'. Deseja cadastrá-lo?"
                    # Atualiza histórico com tool call e resposta
                    messages.append({"role": "assistant", "tool_calls": [tool_call]})
                    messages.append({"role": "tool", "tool_call_id": tool_call.id, "content": resposta})
                    

                elif func_name == "insere_contato":
                    resultado = f.insere_contato(args["nome"], args["telefone"], args["endereco"])
                    messages.append({"role": "assistant", "tool_calls": [tool_call]})
                    messages.append({"role": "tool", "tool_call_id": tool_call.id, "content": resultado})
                    

                elif func_name == "envia_msg":
                    resultado = f.envia_msg(args["telefone"], args["mensagem"])
                    messages.append({"role": "assistant", "tool_calls": [tool_call]})
                    messages.append({"role": "tool", "tool_call_id": tool_call.id, "content": resultado})
                    

                else:
                    # Função desconhecida
                    messages.append({"role": "assistant", "tool_calls": [tool_call]})
                    messages.append({"role": "tool", "tool_call_id": tool_call.id, "content": "Função desconhecida."})
                    print("Função desconhecida.")

        else:
            print(f"Assistente: {message.content}")
            messages.append({"role": "assistant", "content": message.content})

        
        followup = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages
        )
        final_response = followup.choices[0].message.content
        if final_response:
            messages.append({"role": "assistant", "content": final_response})
            print(f"Assistente: {final_response}")


if __name__ == "__main__":
    main()