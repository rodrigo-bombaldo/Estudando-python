hello = 'Definindo categoria do evento' 
print(hello)
evento = int(input('Quantas pessoas foram no evento?'))
print(evento)
if evento > 300: tipo='classe A'
else: tipo='Classe B'
print(tipo)


tipo ='evento Classe A' if evento>300 else 'evento Classe B'
print(tipo)