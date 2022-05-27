import json
import os.path
import sys


def obter_dados():
    '''
    Essa função carrega os dados dos produtos e retorna uma lista de dicionários, onde cada dicionário representa um produto.
    NÃO MODIFIQUE essa função.
    '''
    with open(os.path.join(sys.path[0], 'dados.json'), 'r') as arq:
        dados = json.loads(arq.read())
    return dados


def printar_categorias(categorias: list) -> None:
    for index in range(len(categorias) - 1):
         print(f'{index + 1}º {dados[index]["categoria"]}')
 
def obter_categorias(dados):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    Essa função deverá retornar uma lista contendo todas as categorias dos diferentes produtos.
    Cuidado para não retornar categorias repetidas.    
    '''
    lista_categorias = []
    for index in range(len(dados) - 1):
        if dados[index]['categoria'] not in lista_categorias:
            lista_categorias.append(dados[index]['categoria'])
    return lista_categorias

def listar_por_categoria(dados: list, categoria: str) -> list:
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    O parâmetro "categoria" é uma string contendo o nome de uma categoria.
    Essa função deverá retornar uma lista contendo todos os produtos pertencentes à categoria dada.
    '''
    lista_por_categoria = list()
    for dado in dados:
        if dado['categoria'] == categoria:
            lista_por_categoria.append(dado)

    return lista_por_categoria

def produto_mais_caro(dados:list, categoria:str) -> dict: 
        
    mais_caro = dados[0]
    for dado in dados:
        if dado['categoria'] == categoria:
            if float(mais_caro['preco']) < float(dado['preco']):
                mais_caro = dado
            
    return mais_caro

def produto_mais_barato(dados:list, categoria:str) -> dict:
    
    mais_barato = dados[0]
    for dado in dados:
        if dado['categoria'] == categoria:
            if float(mais_barato['preco']) > float(dado['preco']):
                mais_barato = dado
        
    return mais_barato


def top_10_caros(dados:list):
         
    return sorted(dados, key=lambda x: float(x['preco']), reverse=True)[:10]


def top_10_baratos(dados:list):
    
    return sorted(dados, key=lambda x: float(x['preco']))[:10]

def divisoes():
    print()
    print('=+' * 40)
    print()

def printar_produtos(dados:list):
    for dado in dados:
        print(f'\n\t Categoria: {dado["categoria"].replace("_", " ")} \n\t Id: {dado["id"]} \n\t Preço: {dado["preco"]}') 
        print('-' * 50)

def printar_produto(dado:list):
    print(f'\n\t Categoria: {dado["categoria"].replace("_", " ")} \n\tPreço: {dado["preco"]}') 
    
def opcoes_menu() -> dict:
    divisoes()
    print(""" Escolha uma das opções listadas abaixo: 

-> Orientações:
    * Caso escolha uma dessas opções [2] | [3] | [4], em seguida, quando solicitado, escreva o nome da categoria desejada;
    * Nas demais opções, escreva apenas o número correspondente a opçao desejada.   
    """)

    opcoes = {'1': 'Listar categorias','2': 'Listar produtos de uma categoria','3': 'Produto mais caro por categoria','4': 'Produto mais barato por categoria', '5': 'Top 10 produtos mais caros','6': 'Top 10 produtos mais baratos','0': 'Sair'}

    for opcao in opcoes.items():
        print(f'\n\t [{opcao[0]}] {opcao[1]}')
    divisoes()
    return opcoes

def opcao_escolhida_user():
    opcoes= opcoes_menu()
    
    opcao_escolhida = input(f'--> Qual dessas opções você deseja? ').strip()[0]
    if opcao_escolhida not in opcoes.keys():
        print(f'Opção inválida! Por favor, escolha uma opção válida.')
        opcao_escolhida = input(f'--> Qual dessas opções você deseja? ').strip()[0]
    elif opcao_escolhida == '0':
        exit()

    return opcao_escolhida

def quer_contiuar(): 
    dados = obter_dados()
    quer_continuar = input(f'--> Quer continuar? [9] sim / [0] não: ')[0]
    if quer_continuar != '0' and quer_continuar != '9':
        quer_continuar = input(f'Digite um opção válida! \n-->Quer continuar? [9] sim / [0] não: ')[0]
    elif quer_continuar == '9':
            menu(dados)
    elif quer_continuar == '0':
            exit()

def menu(dados):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    Essa função deverá, em loop, realizar as seguintes ações:
    - Exibir as seguintes opções:
        1. Listar categorias
        2. Listar produtos de uma categoria
        3. Produto mais caro por categoria
        4. Produto mais barato por categoria
        5. Top 10 produtos mais caros
        6. Top 10 produtos mais baratos
        0. Sair
    - Ler a opção do usuário.
    - No caso de opção inválida, imprima uma mensagem de erro.
    - No caso das opções 2, 3 ou 4, pedir para o usuário digitar a categoria desejada.
    - Chamar a função adequada para tratar o pedido do usuário e salvar seu retorno.
    - Imprimir o retorno salvo. 
    O loop encerra quando a opção do usuário for 0.
    '''  
    opcao_escolhida = opcao_escolhida_user()
    while opcao_escolhida != '0':
            if opcao_escolhida == '1':
                printar_categorias(obter_categorias(dados))
                quer_contiuar()
            elif opcao_escolhida == '2':
                categoria = input(f'--> Qual categoria você deseja? ').strip().lower()
                if categoria in obter_categorias(dados): 
                    printar_produtos(listar_por_categoria(dados, categoria))
                else:
                    print('Não foi encontrado nenhuma categoria com esse nome.')
                quer_contiuar()
            elif opcao_escolhida == '3':
                categoria = input(f'--> Qual categoria você deseja? ').strip().lower() 
                if categoria in obter_categorias(dados):  
                    printar_produto(produto_mais_caro(dados, categoria))
                else:
                    print('Não foi encontrado nenhuma categoria com esse nome.')
                quer_contiuar()
            elif opcao_escolhida == '4':
                categoria = input(f'--> Qual categoria você deseja? ').strip().lower()
                if categoria in obter_categorias(dados):  
                    printar_produto(produto_mais_barato(dados, categoria))
                else:
                    print('Não foi encontrado nenhuma categoria com esse nome.')
               
                quer_contiuar()
            elif opcao_escolhida == '5':
                printar_produtos(top_10_caros(dados))
                quer_contiuar()
            elif opcao_escolhida == '6':
                printar_produtos(top_10_baratos(dados))
                quer_contiuar()
            elif opcao_escolhida == '0':
                exit()
           


    
# Programa Principal - não modificar!
dados = obter_dados()
menu(dados)
