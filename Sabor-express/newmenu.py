sabor = 'SABOR EXPRESS';
# loja = 'restaurante';
loja = 'bar'
op1 = f'1 - Cadastrar {loja}'
op2 = f'2 - Listar {loja}';
op3 = f'3 - Ativar {loja}';
op4 = f'4 - Sair do {sabor}';
def menu(): print({sabor}, {op1}, {op2}, {op3}, {op4}, sep='\n');
menu();
digite = 'Digite uma opção: ';
# def escolha_opcao():    escolha = int(input(digite)); print(f'Você escolheu a opção {escolha}');  
# escolha_opcao();

escolha = int(input({digite}));
print(f'Você escolheu a opção {escolha}')

aqui = 'Você está em ';
outra = 'Escolha outra opção';

if escolha ==1: print({aqui}, {op1})
elif escolha ==2: print({aqui}, {op2})
elif escolha ==4: print({aqui}, {op4})
elif escolha ==3: print({aqui}, {op3})
else: print('Escolha outra opção')
