# valor = n
# moedas = m


def main():
    valor = 80

    moedas = [50, 25, 10, 5, 1]

    resultado, total_moedas = CalculaTrocoMinimo(valor, moedas)
    print(f"Moedas usadas: {resultado}")
    print(f"Total de moedas: {total_moedas}")


def CalculaTrocoMinimo(valor, moedas):

    moedas.sort(reverse=True)  # ordenação em ordem decrescente
    resultado = {}
    total_moedas = 0

    for moeda in moedas:
        if valor >= moeda:
            qtd_moedas = valor // moeda
            resultado[moeda] = qtd_moedas
            total_moedas += qtd_moedas
            valor -= qtd_moedas * moeda  # subtrai o valor total desta moeda do troco

    if valor != 0:
        return "Não é possível dar o troco exato com as moedas disponíveis."

    return resultado, total_moedas


if __name__ == "__main__":
    main()
