import copy

def verifica_se_ganhou(tab):
    a = True;
    if tab[0][0] !=0: a = False
    if tab[0][1] !=1: a = False
    if tab[0][2] !=2: a = False
    if tab[1][0] !=3: a = False
    if tab[1][1] !=4: a = False
    if tab[1][2] !=5: a = False
    if tab[2][0] !=6: a = False
    if tab[2][1] !=7: a = False
    if tab[2][2] !=8: a = False
    return a

def tab_iguais(tab1, tab2):
    sao_iguais = True
    for i in range(3):
        for j in range(3):
            if tab1[i][j] != tab2[i][j]:
                sao_iguais = False
    return sao_iguais


def expandir(tab):
    jogadas = []
    #1 se vazio seta no meio do tab
    if tab[1][1]==0:
        #move para baixo
        a = copy.deepcopy(tab)
        a[1][1] = a[0][1]
        a[0][1] = 0
        a[3][0] = a[3][0]+1 #profundidade do nó
        a[3][1] = tab
        jogadas.append(a)

        #move para direita
        a = copy.deepcopy(tab)
        a[1][1] = a[1][0]
        a[1][0] = 0
        a[3][0] = a[3][0]+1
        a[3][1] = tab
        jogadas.append(a)

        #move para esquerda
        a = copy.deepcopy(tab)
        a[1][1] = a[1][2]
        a[1][2] = 0
        a[3][0] = a[3][0] + 1
        a[3][1] = tab
        jogadas.append(a)

        #move para cima
        a = copy.deepcopy(tab)
        a[1][1] = a[2][1]
        a[2][1] = 0
        a[3][0] = a[3][0]+1
        a[3][1] = tab
        jogadas.append(a)
    #2 se vazio esta no canto esquerto superior
    elif tab[0][0]==0:
        #move para cima
        a = copy.deepcopy(tab)
        a[0][0] = a[1][0]
        a[1][0] = 0
        a[3][0] = a[3][0]+1
        a[3][1] = tab
        jogadas.append(a)

        #move para esquerta
        a = copy.deepcopy(tab)
        a[0][0] = a[1][1]
        a[1][1] = 0
        a[3][0] = a[3][0]+1
        a[3][1]= tab
        jogadas.append(a)

        # 3 se vazio esta no canto direito superior
    elif tab[0][2] == 0:
        # move pra cima
        a = copy.deepcopy(tab)
        a[0][2] = a[1][2]
        a[1][2] = 0
        a[3][0] = a[3][0] + 1
        a[3][1] = tab
        jogadas.append(a)
        # move pra direita
        a = copy.deepcopy(tab)
        a[0][2] = a[0][1]
        a[0][1] = 0
        a[3][0] = a[3][0] + 1
        a[3][1] = tab
        jogadas.append(a)
    # 4 se vazio esta no canto inferior esquerdo
    elif tab[2][0] == 0:
        # move pra baixo
        a = copy.deepcopy(tab)
        a[2][0] = a[1][0]
        a[1][0] = 0
        a[3][0] = a[3][0] + 1
        a[3][1] = tab
        jogadas.append(a)
        # move pra esquerda
        a = copy.deepcopy(tab)
        a[2][0] = a[2][1]
        a[2][1] = 0
        a[3][0] = a[3][0] + 1
        a[3][1] = tab
        jogadas.append(a)
    # 5 se vazio esta no canto inferior direito
    elif tab[2][2] == 0:
        # move pra baixo
        a = copy.deepcopy(tab)
        a[2][2] = a[1][2]
        a[1][2] = 0
        a[3][0] = a[3][0] + 1
        a[3][1] = tab
        jogadas.append(a)
        # move pra direita
        a = copy.deepcopy(tab)
        a[2][2] = a[2][1]
        a[2][1] = 0
        a[3][0] = a[3][0] + 1
        a[3][1] = tab
        jogadas.append(a)
    # 6 se vazio esta no meio da linha de cima
    elif tab[0][1] == 0:
        # move pra cima
        a = copy.deepcopy(tab)
        a[0][1] = a[1][1]
        a[1][1] = 0
        a[3][0] = a[3][0] + 1
        a[3][1] = tab
        jogadas.append(a)
        # move pra direita
        a = copy.deepcopy(tab)
        a[0][1] = a[0][0]
        a[0][0] = 0
        a[3][0] = a[3][0] + 1
        a[3][1] = tab
        jogadas.append(a)
        # move pra esquerda
        a = copy.deepcopy(tab)
        a[0][1] = a[0][2]
        a[0][2] = 0
        a[3][0] = a[3][0] + 1
        a[3][1] = tab
        jogadas.append(a)
    # 7 se vazio esta no meio da linha de baixo
    elif tab[2][1] == 0:
        # move pra baixo
        a = copy.deepcopy(tab)
        a[2][1] = a[1][1]
        a[1][1] = 0
        a[3][0] = a[3][0] + 1
        a[3][1] = tab
        jogadas.append(a)
        # move pra direita
        a = copy.deepcopy(tab)
        a[2][1] = a[2][0]
        a[2][0] = 0
        a[3][0] = a[3][0] + 1
        a[3][1] = tab
        jogadas.append(a)
        # move pra esquerda
        a = copy.deepcopy(tab)
        a[2][1] = a[2][2]
        a[2][2] = 0
        a[3][0] = a[3][0] + 1
        a[3][1] = tab
        jogadas.append(a)
    # 8 se vazio esta no meio da coluna da esquerda
    elif tab[1][0] == 0:
        # move pra baixo
        a = copy.deepcopy(tab)
        a[1][0] = a[0][0]
        a[0][0] = 0
        a[3][0] = a[3][0] + 1
        a[3][1] = tab
        jogadas.append(a)
        # move pra cima
        a = copy.deepcopy(tab)
        a[1][0] = a[2][0]
        a[2][0] = 0
        a[3][0] = a[3][0] + 1
        a[3][1] = tab
        jogadas.append(a)
        # move pra esquerda
        a = copy.deepcopy(tab)
        a[1][0] = a[1][1]
        a[1][1] = 0
        a[3][0] = a[3][0] + 1
        a[3][1] = tab
        jogadas.append(a)
    # 9 se vazio esta no meio da coluna da direita
    elif tab[1][2] == 0:
        # move pra baixo
        a = copy.deepcopy(tab)
        a[1][2] = a[0][2]
        a[0][2] = 0
        a[3][0] = a[3][0] + 1
        a[3][1] = tab
        jogadas.append(a)
        # move pra cima
        a = copy.deepcopy(tab)
        a[1][2] = a[2][2]
        a[2][2] = 0
        a[3][0] = a[3][0] + 1
        a[3][1] = tab
        jogadas.append(a)
        # move pra direita
        a = copy.deepcopy(tab)
        a[1][2] = a[1][1]
        a[1][1] = 0
        a[3][0] = a[3][0] + 1
        a[3][1] = tab
        jogadas.append(a)
    return jogadas




