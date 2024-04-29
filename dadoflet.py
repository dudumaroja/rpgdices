import random
import os


def resultado(q , face , lados, resposta):
    r1 = ""
    nd = q
    if nd == 1:
        random.shuffle(face)
        r1 = (F"{resposta}  O resultado do dado é {face[0]}") # Resultado do dado e chama o teste de critico (se tiver 20 lados)

        return(r1)

    else:
        d = 1

        while d <= nd:
            random.shuffle(face)
            r1 = r1 + F" O resultado do {d}° dado é {face[0]}\n"
            d =  d + 1

        return (resposta+r1)



def joga_dados( lados  , quantidade ):

    #Variaveis e listas
    face = []
    l = 1
    n = 1
    nd = quantidade
    resposta = ''

    # Loop para preencher a quantidade de faces dos dados
    while l <= lados:
        face.append(l)
        l = l + 1


    # Loop que arremessa quantas dados o usuário pediu.
    if quantidade == 1:

        resposta = (f'1 dado de {lados} lados lançado! \n')
        r2 = resultado(1, face, lados, resposta)
        print("Passei do primeiro loop")
        return (r2)


    else:


        resposta = (f'{quantidade} dados de {lados} lados lançados! \n')
        r2 = resultado(quantidade, face, lados, resposta)

        return (r2)



