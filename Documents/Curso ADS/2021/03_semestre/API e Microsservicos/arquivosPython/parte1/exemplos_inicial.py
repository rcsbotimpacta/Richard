dic = {
    "alimentos": {
        "pizzas": ["margueritta", "mussarella", 
                   "frango com catupiry", "portuguesa"],
        "bolos": ("floresta negra", 
                   "red velvet", 
                   "de laranja", "dá vó"),
        "calorias": {
            "leite": 129, "fatia pizza": 320,
            "agua": 0, "maça": 95
            }
    },
    "linguagens": [
        {"nome": "javascript", "criacao": 1996, 
        "paradigma": ["eventos","funcional"]},
        {"nome": "python", "criacao": 1991, 
        "paradigma": ["orientada a objetos","estruturada"]},
        {"nome": "haskell", "criacao": 1990, 
        "paradigma": ["funcional"]}
        ]
    }
#10 Escreva uma função "mais velha" que
# recebe um dicionário como dic e
# retorna (isso é diferente de imprimir!) a linguagem de programação mais velha da nossa lista


def maisvelha(dic):
    listalinguagem = dic["linguagens"]
    listanterior = listalinguagem[0]
    for item in listalinguagem:
        if item["criacao"] < listanterior["criacao"]:
            listanterior = item
    return listanterior







#Só se aprende fazendo. PAUSE O VIDEO E TENTE RESPONDER!
#Se possível, FAÇA JUNTO NO SEU COMPUTADOR

#1. quantas chaves tem o dicionario dic?
# print("r1",len(dic)) # 2

#2. dic['linguagens'] é uma tupla, um dicionário ou uma lista?
# print("r2", type(dic['linguagens'])) # lista

#3. Como eu faço para mostrar todos os bolos?
# (escreva o código!)
# for bolos in dic["alimentos"]["bolos"]:
#     print(f'{bolos}')
# floresta negra
# red velvet
# de laranja
# dá vó
#4. Qual o tipo da lista de todos os bolos?
# print("r4", type(dic['alimentos']['bolos'])) #tupla

#5. O que o seguinte acesso imprime? Se ele dá erro, qual o erro? Se dá erro, como corrigir?
# print("r5", dic["linguagens"]["javascript"]["criacao"])
# TypeError: list indices must be integers or slices, not str
# Os indices da listas devem ser inteiros ou fatias, nao string
# print("r5", dic["linguagens"][0]["criacao"])
# Como linguagens é uma lista, eu preciso busca-lo como indice
# e nao pela chave conforme exemplo
# -------------------------------------------------------------
# print(dic["linguagens"][0]["paradigma"])
# for paradigma in dic["linguagens"][0]["paradigma"]:
#     print(paradigma)

#6 O que o seguinte acesso imprime? Se ele dá erro, qual o erro? Se dá erro, como corrigir?
# print("r6", dic["linguagens"][2] == "haskell")
# # resultado será False, para ser true:
# print("r6", dic["linguagens"][2]["nome"] == "haskell")

#7 O que o seguinte acesso imprime? Se ele dá erro, qual o erro? Se dá erro, como corrigir?
# print("r7", dic["alimentos"]["pizzas"][2] == "mussarella")
# # O resultado sera False, pois "alimentos"/"pizza"/2 == "frango com catupiry"
# # Para True, mudar o  == Frango com caturipy
# print("r7", dic["alimentos"]["pizzas"][2] == "frango com catupiry")
# # Para rodar todas pizzas em alimentos:
# for pizzas in dic["alimentos"]["pizzas"]:
#     print(pizzas)

#8 O que o seguinte acesso imprime? Se ele dá erro, qual o erro? Se dá erro, como corrigir?
# print("r8", 1996 in dic['linguagens'][0])  # False, para True
# print("r8",  1996 in dic['linguagens'][0].values())

#9 O que o seguinte acesso imprime? Se ele dá erro, qual o erro? Se dá erro, como corrigir?
# print("r9", "criacao" in dic['linguagens'][0]) # True a mesma coisa que
# print("r9", "criacao" in dic['linguagens'][0].keys())

#9 O que o seguinte acesso imprime? Se ele dá erro, qual o erro? Se dá erro, como corrigir?
# print("ex9b", "pudim" in dic["sobremesas"]["doces"])
# KeyError: 'sobremesas' ,  nao existe a chave 

#10 Escreva uma função "mais velha" que
# recebe um dicionário como dic e
# retorna (isso é diferente de imprimir!) a linguagem de programação mais velha da nossa lista




#11 Escreva uma função que retorna uma lista (sem repetições) de paradigmas de linguagens de programação

