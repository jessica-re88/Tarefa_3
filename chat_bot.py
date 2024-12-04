import os
from datetime import datetime

def obter_resposta(texto: str) -> str:
    comando: str = texto.lower()
    # if comando in ('olá', 'boa tarde', 'bom dia'):
    #     return 'Olá tudo bem!'
    # if comando == 'como estás':
    #     return 'Estou bem, obrigado!'
    # if comando == 'como te chamas':
    #     return 'O meu nome é: Bot :)'
    # if comando == 'tempo':
    #     return 'Está um dia de sol!'
    # if comando in ('bye', 'adeus', 'tchau'):
    #     return 'Gostei de falar contigo! Até breve...'
    # if 'horas' in comando:
    #     return f'São: {datetime.now():%H:%M} horas'
    # if 'data' in comando:
    #     return f'Hoje é dia: {datetime.now():%d-%m-%Y}'

    # return f'Desculpa, não entendi a questão! {texto}'

    respostas = {
        ('olá', 'boa tarde', 'bom dia'): 'Olá tudo bem!',
        'como estás': 'Estou bem, obrigado!',
        'como te chamas': 'O meu nome é: Bot :)',
        ('criador', 'quem te criou'): 'Fui criado por um programador em Python.',
        ('profissão', 'trabalho'): 'Sou um assistente virtual, meu trabalho é conversar e ajudar.',
        'ajuda': 'Posso responder perguntas simples. Tente perguntar algo!',
        ('local', 'onde moras'): 'Moro no mundo digital, em um computador.',
        'tempo': 'Está um dia de sol!',
        'sol': 'Bom para ir à praia.',
        ('bye', 'adeus', 'tchau'): 'Gostei de falar contigo! Até breve...',
        'horas': f'São: {datetime.now():%H:%M} horas',
        'data': f'Hoje é dia: {datetime.now():%d-%m-%Y}'
    }

    for chave, resposta in respostas.items():
        if isinstance(chave, tuple):
            if comando in chave:
                return resposta
        elif chave in comando:
            return resposta

    return f'Desculpa, não entendi a questão! {texto}'


def chat() -> None:
    print('\033[1;34mBem-vindo ao ChatBot!\033[m')
    print('\033[1;35mEscreva "bye" para sair do chat\033[m')
    name: str = input('\033[1;33mBot: Como te chamas? \033[m')
    print(f'\033[1;32mBot: Olá, {name}! \n Como te posso ajudar?\033[m')

    while True:
        user_input: str = input('Tu: ')
        resposta: str = obter_resposta(user_input)
        print(f'Bot: {resposta}')

        if resposta == 'Gostei de falar contigo! Até breve...':
            break

    print('Chat acabou')
    print()


def main() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')
    chat()



if __name__ == '__main__':
    main()
