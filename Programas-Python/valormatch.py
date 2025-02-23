hello = 'Seja bem-vindo '
mundo = 'ao maravilhoso mundo da matemática!'
print({hello}, {mundo})
digite = 'Digite um número: '
escolha = int(input({digite}))
positivo = f'O número {escolha} é positivo'
negativo = f'O número {escolha} é negativo'
zero = 'O número {escolha} é zero'
p = int()
if escolha>0: p=1
elif escolha<0: p=2
else: p=3
# print(f'O valor de p é {p}')
# 
# Esse p é só para controlar o match
match p: 
    case 1: print([positivo])
    case 2: print({negativo}) 
    case 3: print({zero})
    case _: prnt('erro')
