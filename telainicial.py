print("Bem-vindo(a) ao melhor jogo de damas!")
print("")
############################################################


print("Digite 'c' para começar")
print("Digite 'i' para as instruções")
Resposta = input('O que Deseja Fazer?')
if Resposta == "c":
    #PLAY GAME
    print("O Jogo começou!")
elif Resposta == "i":
    print("Os jogadores devem mover-se estrategicamente com o propósito de eliminar o oponente. A única forma de ganhar o jogo é eliminar todas as peças do outro jogador!")
    print("Digite 'c' para começar")
    print("Digite 'i' para as instruções")
    Resposta = input('O que Deseja Fazer?')
    if Resposta == "c":
    #PLAY GAME
        print("O Jogo começou!")
else:
    while Resposta != "c" and "i":
    
        print("Não entendi o que quis dizer. Pode digitar novamente?")
        print("Digite 'c' para começar")
        print("Digite 'i' para as instruções")
        print("")
        print("O que deseja fazer?")
        print("")
        Resposta = input()
        if Resposta == "c":
        #PLAY GAME
            print("O Jogo começou!")
        if Resposta == "i":
             print("Os jogadores devem mover-se estrategicamente com o propósito de eliminar o oponente. A única forma de ganhar o jogo é eliminar todas as peças do outro jogador!")
