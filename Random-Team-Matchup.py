import random
team =[]

# size é o tamanho do grupo, para adicionar mais times digite team.append([])

group_size = 2

team.append(['Pedro','Vitória','Erik','Victor','Grazielli','Samuel','Nicolas'
,'Clara','Isabela','Eduardo'])

team.append(['Raíssa','Leonardo','Luís','Lívia','Kauã','Guillermo',
'Vinícius','Ana','Letícia'])

team.append(['Cauã','Caroline','Rauany','Wellington','Raquel','Maria','Kauê',
'Valesca'])

# Randomizando times
size_biggest_team = 0
indice_biggest_team = 0
list_status_quo=[]
for x in range(len(team)):
    random.shuffle(team[x])
    list_status_quo.append([0])
    if(len(team[x])>size_biggest_team):
        size_biggest_team = len(team[x])
        indice_biggest_team = x

# Igualando tamanho do maior time em múltiplos para o size
while(len(team[indice_biggest_team])%group_size !=0):
    team[indice_biggest_team].append(team[indice_biggest_team][list_status_quo[indice_biggest_team][0]])
    list_status_quo[indice_biggest_team][0]+=1

# Igualando tamanho dos times com o maior
for x in range(len(team)):
    if(indice_biggest_team!=x):
        while(len(team[x])<len(team[indice_biggest_team])):
            team[x].append(team[x][list_status_quo[x][0]])
            list_status_quo[x][0]+=1

# Imprimindo os confrontos entre os times
for i in range(len(team[indice_biggest_team])//group_size):
    indice = i*group_size
    temp_team = []
    for x in range(len(team)):
        temp_team.append([])
        for y in range(group_size):
            temp_team[x].append(team[x][indice+y])
    temp_string= ""
    for indice_team in range(len(temp_team)):
        for x in range(len(temp_team[indice_team])):
            temp_string += temp_team[indice_team][x]
            if x == len(temp_team[indice_team])-2:
                temp_string += ' e '
            #elif x == len(temp_team[indice_team])-1:
                #temp_string += '.'
            elif x != len(temp_team[indice_team])-1:
                temp_string  += ', '
        if(indice_team < len(temp_team)-1):
            temp_string += ' X '
        if(indice_team == len(temp_team)-1):
            temp_string += '.'
    print(i+1,'-',temp_string)

