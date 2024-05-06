import json
from tabulate import tabulate

# Função para carregar os dados do arquivo JSON
def carregar_banco_de_dados(nome_arquivo):
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        return json.load(arquivo)

# Função para filtrar os filmes com base na pontuação e gênero
def filtrar_filmes_por_pontuacao_e_genero(filmes, pontuacao_minima, genero_alvo):
    filmes_filtrados = []
    for filme in filmes:
        if filme["Pontuação IMDB"] >= pontuacao_minima and genero_alvo in filme["Gênero"]:
            filmes_filtrados.append(filme)
    return filmes_filtrados

# Função para calcular a média de pontuação dos filmes
def calcular_media_pontuacao(filmes):
    total_pontuacao = sum(filme["Pontuação IMDB"] for filme in filmes)
    return total_pontuacao / len(filmes) if filmes else 0

# Carregar os dados do banco de dados
banco_de_dados = carregar_banco_de_dados("imdb.json")

# Mostrar opções de gênero
generos_disponiveis = set()
for filme in banco_de_dados:
    generos_disponiveis.update(filme["Gênero"].split(", "))
print("Gêneros disponíveis:", ", ".join(sorted(generos_disponiveis)))

# Solicitar entrada do usuário para o gênero e pontuação mínima
genero_alvo = input("Digite o gênero desejado: ")
pontuacao_minima = float(input("Digite a pontuação mínima desejada: "))

# Filtrar os filmes com base na pontuação e gênero
filmes_filtrados = filtrar_filmes_por_pontuacao_e_genero(banco_de_dados, pontuacao_minima, genero_alvo)

# Calcular a média de pontuação dos filmes filtrados
media_pontuacao = calcular_media_pontuacao(filmes_filtrados)

# Criar uma lista de dados para a tabela
dados_tabela = [[filme["Nome do Filme"], filme["Pontuação IMDB"]] for filme in filmes_filtrados]

# Imprimir a tabela
print(f"\nFilmes de {genero_alvo} com pontuação maior ou igual a {pontuacao_minima}:")
print(tabulate(dados_tabela, headers=["Nome do Filme", "Pontuação IMDB"], tablefmt="grid"))
print(f"\nMédia de pontuação dos filmes filtrados: {media_pontuacao:.2f}")
