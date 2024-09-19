from collections import defaultdict


# Função hash de divisão (método da divisão)
def get_division_hash(city_name, table_size):
    # Converte o nome da cidade para uma representação numérica (soma dos códigos ASCII)
    total_ascii_value = sum(ord(char) for char in city_name)
    # Aplica o método da divisão para calcular o hash
    return total_ascii_value % table_size


# Função para carregar as cidades a partir de um arquivo
def load_cities(file_name):
    with open(file_name, "r") as file:
        cities = [line.strip() for line in file.readlines()]
    return cities


# Função para executar o hash e calcular as estatísticas
def execute_hashing(cities, table_size, hash_function):
    # Cria uma tabela hash usando listas para tratar colisões
    hash_table = defaultdict(list)
    collisions = 0

    # Insere cada cidade na tabela hash
    for city in cities:
        hash_value = hash_function(city, table_size)
        if len(hash_table[hash_value]) > 0:
            collisions += 1  # Se o bucket já tiver elementos, conta como colisão
        hash_table[hash_value].append(city)  # Insere a cidade no bucket

    # Calcula as estatísticas
    address_stats = defaultdict(int)  # Conta quantos buckets têm 0, 1, 2... 10+ cidades
    for bucket in hash_table.values():
        size = len(bucket)
        if size > 10:
            size = 10  # Considera buckets com mais de 10 cidades como "10 ou mais"
        address_stats[size] += 1

    # Exibe as estatísticas
    print(f"Tamanho da Tabela: {table_size}")
    print(f"Número total de colisões: {collisions}")
    for i in range(11):
        print(
            f"Buckets com {i if i < 10 else '10 ou mais'} cidades associadas: {address_stats[i]}"
        )
    print()


# Função principal
def main():
    # Carrega a lista de cidades a partir do arquivo 'Cidades.txt'
    cities = load_cities("Cidades.txt")

    # Executa o hash com diferentes tamanhos de tabela para ambas as funções de hash
    table_sizes = [100, 425, 853]  # Tamanhos da tabela hash a serem testados

    print("\nUsando o hash de divisão:")
    for size in table_sizes:
        execute_hashing(cities, size, get_division_hash)


if __name__ == "__main__":
    main()
