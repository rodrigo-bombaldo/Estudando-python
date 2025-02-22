qual ='Escolha um número: '
escolha = int(input(qual));
positivo = f'O número {escolha} é positivo!'                    ;
negativo = f'O número {escolha} é negativo!'                    ;
zero = f'O número {escolha} é zero';
if escolha>0:   print(positivo);
elif escolha<0:   print(negativo);
else:   print(zero);