hello = 'Em que fase da vida você está?'
print(hello)
idade = int(input('Qual sua idade?'))
if idade <0: fase = 'erro'

if idade < 12: fase='criança'
elif idade <18  : fase = 'adolescente'
else: fase='adulto'
print(fase)

fase='criança' if idade<12 'adolescente'