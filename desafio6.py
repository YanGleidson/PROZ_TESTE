def obter_nome_e_ano():

    nome_completo = input("Digite seu nome: ")

    while True:
        try:
            ano_nascimento = int(input("Digite o ano de nascimento (entre 1922 e 2025): "))
            if 1922 <= ano_nascimento <= 2025:
                break
            else:
                print("Ano de nascimento inválido. Digite um ano entre 1922 e 2025.")
        except ValueError:
            print("Entrada inválida. Digite um número inteiro para o ano de nascimento.")

    return nome_completo, ano_nascimento


def calcular_idade(ano_nascimento):
   
    ano_atual = 2025
    idade = ano_atual - ano_nascimento
    return idade


if __name__ == "__main__":
    nome_completo, ano_nascimento = obter_nome_e_ano()
    idade = calcular_idade(ano_nascimento)

    print("\nSeu nome:", nome_completo)
    print("Sua idade em 2025:", idade, "anos")