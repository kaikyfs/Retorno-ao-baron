import random

#ABERTURA
def igual():
    print('='*120) 

def enter():
    input('Pressione Enter para continuar\n')

def dialogo_inicial():
    igual()
    print('Imediato: Mestre Cecil, a tripulação está indagando se foi certo o que fizemos ao roubar o cristal das mãos de civís.')
    igual()
    enter()
    igual()
    print('Cecil: Também não gostei do que vi, mas não cabe a nós questionar a ordem do rei')
    igual()
    enter()
    igual()
    print('Cecil: Logo chegaremos ao reino de Biron e é melhor que esses comentários cessem logo ou .....')
    igual()
    enter()
    igual()
    print('Timoneiro: Monstros na proa!')
    igual()
    enter()
    igual()
    print('Cecil: Preparem-se para a batalha.')
    igual()
    enter()

def dialFechamento():
     print('Imediato: Estamos condenados.\nCecil: A cada dia que se passa, monstros cada vez mais fortes nos ameaçam.')

#Funções para batalha
def menu_protagonista():
     opcao=[0,1,2]
     while True:
        entrada = int(input("Opções\n0 - Atacar\n1 - Usar item\n2 - Fugir\n"))
        if validar_entrada(opcao, entrada):
             break
        else:
             print("Opção inválida, tente novamente")
     return entrada

def menu_ataque_protagonista():
     opcao= [0,1]
     while True:
          entrada = int(input("Escolha um monstro para atacar:\n0 - Olhudo\n1 - Olhão\n"))
          if validar_entrada(opcao, entrada):
               break              
          else:
               print("Opção inválida")
     return entrada

def realizar_ataque(atacante, defensor):
    dano = atacante['Atk'] - defensor['Def']
    if dano>0:
        defensor['HP'] -= dano
        print(f"{atacante['Nome']} atacou {defensor['Nome']} e causou {dano} pontos de dano.")
        return defensor
    else:
        print(f'{defensor['Nome']} tem mais armadura que o poder de ataque de {atacante['Nome']}, nenhum dano foi causado')

def exibir_informacoes(personagem):
    print(f"Nome: {personagem['Nome']}")
    print(personagem['Imagem'])
    print(f"HP: {personagem['HP']}")
    print(f"Ataque: {personagem['Atk']}")
    print(f"Defesa: {personagem['Def']}")

#Função para validar entradas
def validar_entrada(opcoes, entrada):
    return entrada in opcoes
    
#Personagens 

def inteiroAleatorio(inf, sup):
    return random.randint(inf, sup)

def importaImagem(arquivo):
    arq = open(arquivo)
    per = arq.read()
    arq.close()
    return per

personagem1={
    'Nome': 'Cecil',
    'Imagem': importaImagem('cecil.txt'),
    'Tipo':'Protagonista',
    'Atk': inteiroAleatorio(1,20),
    'Def': inteiroAleatorio(1,10),
    'HP': inteiroAleatorio(1,100),
    'Agil': inteiroAleatorio(0,2),
}

personagem2={
    'Nome': 'Olhão',
    'Imagem': importaImagem('monster.txt'),
    'Tipo':'Monstro',
    'Atk': inteiroAleatorio(1,20),
    'Def': inteiroAleatorio(1,10),
    'HP': inteiroAleatorio(1,80),
    'Agil': inteiroAleatorio(0,2),
}

personagem3={
    'Nome': 'Olhudo',
    'Imagem': importaImagem('monster.txt'),
    'Tipo':'Monstro',
    'Atk': inteiroAleatorio(1,20),
    'Def': inteiroAleatorio(1,10),
    'HP': inteiroAleatorio(1,80),
    'Agil': inteiroAleatorio(0,2),
}



#Menu itens
itens=[]
for i in range(1,2):
    for j in range(1,3):
        x = inteiroAleatorio(1,12)
        if 1<x<=4:
            sena=inteiroAleatorio(1,3)
            val=inteiroAleatorio(10,20)
            if sena==3:
                    ataque={'atk':val}
                    itens.append(ataque)
        elif 4<x<=8:
            sena=inteiroAleatorio(1,3)
            val=inteiroAleatorio(10,20)
            if sena==3:
                    defesa={'def':val}
                    itens.append(defesa)
        elif 8<x<=12:
            sena=inteiroAleatorio(1,3) 
            val=inteiroAleatorio(10,20)
            if sena==3:
                    vida={'hp':val}
                    itens.append(vida)


#Ordem das jogadas
personagens = [personagem1, personagem2, personagem3]

# Defina uma função para determinar a ordem com base no valor de 'Agil':
def ordem(personagem):
    return -personagem.get('Agil')  # O sinal de menos (-) inverte a ordem para 'sorted'

# Classifique a lista de personagens com base na função 'ordem':
personagens_ordenados = sorted(personagens, key=ordem)

# Os três primeiros personagens em 'personagens_ordenados' representam a ordem desejada:
player1, player2, player3 = personagens_ordenados[:3]



#Batalha
dialogo_inicial()
controle=1

while controle!=0:
    while personagem1['HP']>0 or (personagem2['HP']>0 and personagem3['HP']>0) or opcao!=2:
        if player1.get('Nome')=='Olhão':
            if player2.get('Nome')=='Olhudo':
                #Olhão ataca Cecil
                exibir_informacoes(player1)
                igual()
                realizar_ataque(player1, player3)
                igual()
                enter()
                #Olhudo ataca cecil
                exibir_informacoes(player2)
                igual()
                realizar_ataque(player2, player3)
                igual()
                enter()
                #Cecil ataca
                exibir_informacoes(player3)
                igual()
                entrada = menu_protagonista()
                if entrada ==0:
                     opcao = menu_ataque_protagonista()
                     if opcao == 0:
                          igual()
                          realizar_ataque(player3, player2)
                          igual()
                          enter()
                     elif opcao == 1:
                          igual()
                          realizar_ataque(player3, player1)
                          igual()
                          enter()
                elif entrada == 1:
                     print(itens)
                elif entrada == 2:
                     print("VOCÊ FUGIU!!!!")
                     controle == 0
                     break
            elif player2.get('Nome') == 'Cecil':
                #Olhão ataca Cecil
                exibir_informacoes(player1)
                igual()
                realizar_ataque(player1, player2)
                igual()
                enter()
                #Cecil ataca
                exibir_informacoes(player2)
                igual()
                entrada = menu_protagonista()
                if entrada ==0:
                     opcao = menu_ataque_protagonista()
                     if opcao == 0:
                          igual()
                          realizar_ataque(player2, player3)
                          igual()
                          enter()
                     elif opcao == 1:
                          igual()
                          realizar_ataque(player2, player1)
                          igual()
                          enter()
                elif entrada == 1:
                     print(itens)
                elif entrada == 2:
                     print("VOCÊ FUGIU!!!!")
                     controle == 0
                     break
                enter()
                #Olhudo ataca cecil
                exibir_informacoes(player3)
                igual()
                realizar_ataque(player3, player2)
                igual()
                enter()
        elif player1.get('Nome') == 'Olhudo':
             if player2.get('Nome') == 'Olhão':
                #Olhudo ataca Cecil
                exibir_informacoes(player1)
                igual()
                realizar_ataque(player1, player3)
                igual()
                enter()
                #Olhão ataca cecil
                exibir_informacoes(player2)
                igual()
                realizar_ataque(player2, player3)
                igual()
                enter()
                #Cecil ataca
                exibir_informacoes(player3)
                igual()
                entrada = menu_protagonista()
                if entrada ==0:
                     opcao = menu_ataque_protagonista()
                     if opcao == 0:
                          igual()
                          realizar_ataque(player3, player1)
                          igual()
                          enter()
                     elif opcao == 1:
                          igual()
                          realizar_ataque(player3, player2)
                          igual()
                          enter()
                elif entrada == 1:
                     print(itens)
                elif entrada == 2:
                     print("VOCÊ FUGIU!!!!")
                     controle == 0
                     break
             elif player2.get('Nome') == 'Cecil':
                #Olhudo ataca Cecil
                exibir_informacoes(player1)
                igual()
                realizar_ataque(player1, player2)
                igual()
                enter()
                #Cecil ataca
                exibir_informacoes(player2)
                igual()
                entrada = menu_protagonista()
                if entrada ==0:
                     opcao = menu_ataque_protagonista()
                     if opcao == 0:
                          igual()
                          realizar_ataque(player2, player1)
                          igual()
                          enter()
                     elif opcao == 1:
                          igual()
                          realizar_ataque(player2, player3)
                          igual()
                          enter()
                elif entrada == 1:
                     print(itens)
                elif entrada == 2:
                     print("VOCÊ FUGIU!!!!")
                     controle == 0
                     break
                enter()
                #Olhão ataca cecil
                exibir_informacoes(player3)
                igual()
                realizar_ataque(player3, player2)
                igual()
                enter()
        elif player1.get('Nome') == 'Cecil':
             if player2.get('Nome') == 'Olhão':
                #Cecil ataca
                exibir_informacoes(player1)
                igual()
                entrada = menu_protagonista()
                if entrada ==0:
                     opcao = menu_ataque_protagonista()
                     if opcao == 0:
                          igual()
                          realizar_ataque(player1, player3)
                          igual()
                          enter()
                     elif opcao == 1:
                          igual()
                          realizar_ataque(player1, player2)
                          igual()
                          enter()
                elif entrada == 1:
                     print(itens)
                elif entrada == 2:
                     print("VOCÊ FUGIU!!!!")
                     controle == 0
                     break
                #Olhão ataca Cecil
                exibir_informacoes(player2)
                igual()
                realizar_ataque(player2, player1)
                igual()
                enter()
                #Olhudo ataca cecil
                exibir_informacoes(player3)
                igual()
                realizar_ataque(player3, player1)
                igual()
                enter()
             elif player2.get('Nome') == 'Olhudo':
                  #Cecil ataca
                exibir_informacoes(player1)
                igual()
                entrada = menu_protagonista()
                if entrada ==0:
                     opcao = menu_ataque_protagonista()
                     if opcao == 0:
                          igual()
                          realizar_ataque(player1, player2)
                          igual()
                          enter()
                     elif opcao == 1:
                          igual()
                          realizar_ataque(player1, player3)
                          igual()
                          enter()
                elif entrada == 1:
                     print(itens)
                elif entrada == 2:
                     print("VOCÊ FUGIU!!!!")
                     controle == 0
                     break
                #Olhudo ataca Cecil
                exibir_informacoes(player2)
                igual()
                realizar_ataque(player2, player1)
                igual()
                enter()
                #Olhão ataca cecil
                exibir_informacoes(player3)
                igual()
                realizar_ataque(player3, player1)
                igual()
                enter()   
    if personagem1['HP'] <0:
         print('Você morreu!')
         controle == 0
    elif (personagem2['HP'] and personagem3['HP']) <0:
         print('Parabéns, você derrotou os monstros')
         controle == 0  
dialFechamento()