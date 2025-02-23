sabor = 'SABOR EXPRESS'
op1 = '1 - Cadastrar bar'
op2 = '2  - Listar bar'
op3 = '3  - Ativar bar'
op4 = f'4  - Sair do {sabor}'
def menu(): print({sabor}, {op1}, {op2}, {op3}, {op4}, sep = '\n')
menu()
digite = 'Escolha uma opção: '
escolha = int(input({digite}))
you = 'Você escolheu '
outra = 'Escolha outra opção'
match escolha:
    case 1: print([you], {op1})
    case 2: print([you], {op2})
    case 3: print([you], {op3})
    case 4: print([you], {op4})
    case _: print({outra})

