hello = 'Seja bem-vindo ao '
jogo = 'Jogo do Número Secreto'
print({hello}, {jogo})
nome = input('Qual é seu nome?')
prazer= '[É um prazer jogar com '
print({prazer}, {nome})
secreto = 5
digite = 'Digite um número entre 1 e 10'
maior = 'O número é maior'
menor = 'O número é menor'
certo = f'Você acertou o número secreto: {secreto}'
diferente = 'O número é diferente'
escolha=0
jogada=0

# escolha =int(input({digite}))
# if escolha != secreto: print({diferente})
# else: print({certo})

def dica():    
    if escolha>secreto: print({menor}) 
    elif escolha<secreto: print({maior}); 
    else: print({certo})
while escolha != secreto: escolha=int(input({digite})); dica(); jogada=jogada+1
print(f'{nome} conseguiu descobrir o número secreto com {jogada} tentativas')


