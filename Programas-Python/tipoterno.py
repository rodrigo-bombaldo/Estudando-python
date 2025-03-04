hello = 'Definindo se evento pode ser repetido'
print(hello)
evento = int(input('Quantas pessoas foram no evento?'))
print(evento)
if evento >=200: confirma='Sim'
else: confirma='Não'
print(confirma)

confirma='Pode repetir' if evento >=200  else 'Não pode repetir'
print(confirma)