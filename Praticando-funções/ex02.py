# Escrever na tela se é professor ou professora e o nome do professor ou professora.

hello = "Seja bem-vindo à escola"
print({hello})
nome_escola = input("Qual é onome da sua escola?")
nome_aluno = input("Qual seu nome?")
print(f"{nome_aluno} estuda na escola {nome_escola}")
genero = "Seu professor é?"
homem = "Digite 1 para HOMEM"
mulher = "Digite 2 para MULHER"
print({genero}, {homem}, {mulher}, sep="\n")
digite = "Digite sua opção:"
opcao = int(input({digite}))
if opcao == 1:
    pro = "seu professor"
elif opcao == 2:
    pro = "sua professora"
else:
    print("Opção inválida!")

print(f"{nome_aluno} estuda com {pro}")
