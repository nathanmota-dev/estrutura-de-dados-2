from collections import defaultdict

# Função getHash original convertida para Python
def get_hash(city_name, divisor):
    # Converte o nome da cidade em uma lista de códigos ASCII
    ascii_values = [ord(ch) for ch in city_name]
    
    final_hash = 0
    
    # Para cada código ASCII, reverte o número e soma ao final_hash
    for char_code in ascii_values:
        char_string = str(char_code)
        reversed_char_string = char_string[::-1]  # Inverte a string
        reversed_code = int(reversed_char_string)
        final_hash += reversed_code
    
    # Aplica o divisor para gerar o hash final
    return final_hash % divisor

# Função para carregar as cidades a partir de um arquivo
def load_cities(file_name):
    with open(file_name, 'r') as file:
        cities = [line.strip() for line in file.readlines()]
    return cities

# Função para executar o hash e calcular as estatísticas
def execute_hashing(cities, table_size):
    # Cria uma tabela hash usando listas para tratar colisões
    hash_table = defaultdict(list)
    collisions = 0
    
    # Insere cada cidade na tabela hash
    for city in cities:
        hash_value = get_hash(city, table_size)
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
        print(f"Buckets com {i if i < 10 else '10 ou mais'} cidades associadas: {address_stats[i]}")
    print()

# Função principal
def main():
    # Carrega a lista de cidades a partir do arquivo 'Cidades.txt'
    cities = load_cities("Cidades.txt")
    
    # Executa o hash com diferentes tamanhos de tabela
    table_sizes = [100, 425, 853]  # Tamanhos da tabela hash a serem testados
    for size in table_sizes:
        execute_hashing(cities, size)

if __name__ == "__main__":
    main()
