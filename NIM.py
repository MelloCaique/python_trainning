
def usuario_escolhe_jogada(n,m):

def computador_escolhe_jogada(n,m):




def partida():
    print("Bem-vindo ao jogo NIM! Escolha: ")
    print("1 - para jogar uma partida isolada")
    print("2 - para jogar um campeonato")
    escolha=int(input())

    if escolha == 1:
        print("Voce escolheu uma partida isolada!")
    else:
        print("Voce escolheu um campeonato!")

    n=int(input("Quantas peças? "))
    m=int(input("Limite de peças por rodada? "))

    if n%(m+1)==0:
        print("Você começa!")
    else:
        print("Computdor começa!")

partida()