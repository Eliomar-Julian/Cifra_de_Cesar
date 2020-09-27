# Cifra_de_Cesar

## um script de criptografia simples usado para o meu aprendizado
# 📜  📜  📜
## [veja mais aqui](https://pt.wikipedia.org/wiki/Cifra_de_C%C3%A9sar) 😀😀

> a primeira função serve para criptografar uma palavra e deve ser passado uma chave.

> a segunda serve para quebrar a critografia da primeira.

> deve ser usada via CLI.

### __uso para criptografar__ [param > senha > chave ]
```
-c senha 5
```
### __uso para decriptografar__ [param > senha]
`
-d senha
`
### um pequeno trecho de codigo
`
x in senha:
        posi = lista_alfa.index(x)
        nova_senha = nova_senha + lista_alfa[(posi + chave)%len(alfabeto)]
    
    try:
        nova_senha = nova_senha + alfabeto[(chave)%len(alfabeto)]
    except:
        pass

    return nova_senha
    `
