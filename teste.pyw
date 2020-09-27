from string import ascii_letters
from sys import argv

alfabeto = ascii_letters + "0123456789"

def cripta(senha: str, chave: int) -> str:
    lista_alfa = list()
    nova_senha = str()
    for x in alfabeto:
        lista_alfa.append(x)
    for x in senha:
        posi = lista_alfa.index(x)
        nova_senha = nova_senha + lista_alfa[(posi + chave)%len(alfabeto)]
    
    try:
        nova_senha = nova_senha + alfabeto[(chave)%len(alfabeto)]
    except:
        pass

    
    return nova_senha

def decripta(senha: str) -> str:
    lista_alfa = list()
    nova_senha = str()
    chave = int
    for x in alfabeto:
        lista_alfa.append(x)
    for x in senha:
        posi = lista_alfa.index(x)
        chave = lista_alfa.index(senha[-1])
        nova_senha = nova_senha + lista_alfa[(posi - chave)%len(alfabeto)]
    
    return nova_senha[:-1]


try:
    if argv[1] == "-c":
        print(cripta(argv[2], int(argv[3])))
    elif argv[1] == "-d":
        print(decripta(argv[2]))
except:
    print("\033[1;31mPor favor insira uma opção válida")