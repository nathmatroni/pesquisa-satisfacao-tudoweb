# Pesquisa de satisfação - TudoWeb

excelente = 0
bom = 0
ruim = 0

print("=== PESQUISA DE SATISFAÇÃO TUDOWEB ===")

for i in range(50):
    print(f"\nEntrevistado {i + 1}")

    nome = input("Digite seu nome: ")

    while True:
        try:
            idade = int(input("Digite sua idade: "))
            if idade > 0:
                break
            print("A idade deve ser maior que zero.")
        except ValueError:
            print("Digite uma idade válida usando números.")

    print("\nComo você avalia nosso atendimento?")
    print("1 - EXCELENTE")
    print("2 - BOM")
    print("3 - RUIM")

    while True:
        try:
            opiniao = int(input("Digite sua opção: "))
            if opiniao in (1, 2, 3):
                break
            print("Opção inválida. Digite 1, 2 ou 3.")
        except ValueError:
            print("Digite apenas o número 1, 2 ou 3.")

    if opiniao == 1:
        excelente += 1
        classificacao = "EXCELENTE"
    elif opiniao == 2:
        bom += 1
        classificacao = "BOM"
    else:
        ruim += 1
        classificacao = "RUIM"

    print(f"Obrigado pela participação, {nome}!")
    print(f"Resposta registrada: {classificacao}")

print("\n=== RESULTADO FINAL DA PESQUISA ===")
print("Quantidade de respostas EXCELENTE:", excelente)
print("Quantidade de respostas RUIM:", ruim)
