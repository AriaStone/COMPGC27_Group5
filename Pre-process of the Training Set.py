##############################################################################
############integrate the dataset#############################################
##############################################################################

import pandas as pd 
import numpy as np
import os
from pandas import Series, DataFrame

pokemon = pd.read_csv("G:\\Business Analytics\\Programming for Business Analytics\\pokemon.csv")
combat = pd.read_csv("G:\\Business Analytics\\Programming for Business Analytics\\combats.csv")
pokemons = np.array(pokemon)
combats = np.array(combat)
pokemons = pokemons.tolist()
combats = combats.tolist()
training_set = []
training_label = []
Types = []
Types_temp = [0,0,0,0]
T = []

Type = [[1,1,1,1,1,0.5,1,0,0.5,1,1,1,1,1,1,1,1,1]]#normal
Type.append([2,1,0.5,0.5,1,2,0.5,0,2,1,1,1,1,0.5,2,1,2,0.5])#fight
Type.append([1,2,1,1,1,0.5,2,1,0.5,1,1,2,0.5,1,1,1,1,1])#flying
Type.append([1,1,1,0.5,0.5,0.5,1,0.5,0,1,1,2,1,1,1,1,1,2])#Poison
Type.append([1,1,0,2,1,2,0.5,1,2,2,1,0.5,2,1,1,1,1,1])#Ground
Type.append([1,0.5,2,1,0.5,1,2,1,0.5,2,1,1,1,1,2,1,1,1])#Rock
Type.append([1,0.5,0.5,0.5,1,1,1,0.5,0.5,0.5,1,2,1,2,1,1,2,0.5])#Bug
Type.append([0,1,1,1,1,1,1,2,1,1,1,1,1,2,1,1,0.5,1])#Ghost
Type.append([1,1,1,1,1,2,1,1,0.5,0.5,0.5,1,0.5,1,2,1,1,2])#Steel
Type.append([1,1,1,1,1,0.5,2,1,2,0.5,0.5,2,1,1,2,0.5,1,1])#Fire
Type.append([1,1,1,1,2,2,1,1,1,2,0.5,0.5,1,1,1,0.5,1,1])#Water
Type.append([1,1,0.5,0.5,2,2,0.5,1,0.5,0.5,2,0.5,1,1,1,0.5,1,1])#Grass
Type.append([1,1,2,1,0,1,1,1,1,1,2,0.5,0.5,1,1,0.5,1,1])#Electr
Type.append([1,2,1,2,1,1,1,1,0.5,1,1,1,1,0.5,1,1,0,1])#Psychc
Type.append([1,1,2,1,2,1,1,1,0.5,0.5,0.5,2,1,1,0.5,2,1,1])#Ice
Type.append([1,1,1,1,1,1,1,1,0.5,1,1,1,1,1,1,2,1,0])#Dragon
Type.append([1,0.5,1,1,1,1,1,2,1,1,1,1,1,2,1,1,0.5,0.5])#Dark
Type.append([1,2,1,0.5,1,1,1,1,0.5,0.5,1,1,1,1,1,2,2,1])#Fairy



for i in range(0,len(combats)):
    if combats[i][0] == combats[i][2]:
        combats[i][2] = 1
    else:
        combats[i][2] = 0

for i in range(0,len(combats)):
        training_set.append(pokemons[combats[i][0] - 1] + pokemons[combats[i][1] - 1])
        training_set[i].pop(0)
        training_set[i].pop(0)
        training_set[i].pop(0)
        training_set[i].pop(10)
        training_set[i].pop(10)
        training_set[i].pop(10)
        training_set[i].pop(8)
        training_set[i].pop(8)
        training_set[i].pop()
        training_set[i].pop()
        if type(training_set[i][1]) == float:
            training_set[i][1] = 'NO'
        if type(training_set[i][9]) == float:
            training_set[i][9] = 'NO'

for i in range(0,len(combats)):
    training_label.append(combats[i][2])

for i in range(0,len(combats)):
    Types.append([training_set[i][0]])
    for j in [1,8,9]:
        Types[i].append(training_set[i][j])
        
for i in range(0,len(Types)):
    for j in range(0,4):
        if Types[i][j] == 'Normal':
            Types[i][j] = 0
        if Types[i][j] == 'Fighting':
            Types[i][j] = 1
        if Types[i][j] == 'Flying':
            Types[i][j] = 2
        if Types[i][j] == 'Poison':
            Types[i][j] = 3
        if Types[i][j] == 'Ground':
            Types[i][j] = 4
        if Types[i][j] == 'Rock':
            Types[i][j] = 5
        if Types[i][j] == 'Bug':
            Types[i][j] = 6
        if Types[i][j] == 'Ghost':
            Types[i][j] = 7
        if Types[i][j] == 'Steel':
            Types[i][j] = 8
        if Types[i][j] == 'Fire':
            Types[i][j] = 9
        if Types[i][j] == 'Water':
            Types[i][j] = 10
        if Types[i][j] == 'Grass':
            Types[i][j] = 11
        if Types[i][j] == 'Electric':
            Types[i][j] = 12
        if Types[i][j] == 'Psychic':
            Types[i][j] = 13
        if Types[i][j] == 'Ice':
            Types[i][j] = 14
        if Types[i][j] == 'Dragon':
            Types[i][j] = 15
        if Types[i][j] == 'Dark':
            Types[i][j] = 16
        if Types[i][j] == 'Fairy':
            Types[i][j] = 17


for i in range(0,50000):
    if 'NO' not in Types[i]:
        training_set[i][0] = Type[Types[i][0]][Types[i][2]] * Type[Types[i][0]][Types[i][3]]
        training_set[i][1] = Type[Types[i][1]][Types[i][2]] * Type[Types[i][1]][Types[i][3]]
        training_set[i][8] = Type[Types[i][2]][Types[i][0]] * Type[Types[i][2]][Types[i][1]]
        training_set[i][9] = Type[Types[i][3]][Types[i][0]] * Type[Types[i][3]][Types[i][1]]
        
    if Types[i][1] =='NO'and Types[i][3] =='NO':
        training_set[i][0] = Type[Types[i][0]][Types[i][2]] 
        training_set[i][1] = training_set[i][0]
        training_set[i][8] = Type[Types[i][2]][Types[i][0]] 
        training_set[i][9] = training_set[i][8]
        
    if Types[i][1] =='NO'and Types[i][3] !='NO':
        training_set[i][0] = Type[Types[i][0]][Types[i][2]] * Type[Types[i][0]][Types[i][3]]
        training_set[i][1] = training_set[i][0]
        training_set[i][8] = Type[Types[i][2]][Types[i][0]] 
        training_set[i][9] = Type[Types[i][3]][Types[i][0]] 
        
    if Types[i][1] !='NO'and Types[i][3] =='NO':
        training_set[i][0] = Type[Types[i][0]][Types[i][2]]
        training_set[i][1] = Type[Types[i][1]][Types[i][2]]
        training_set[i][8] = Type[Types[i][2]][Types[i][0]] * Type[Types[i][2]][Types[i][1]]
        training_set[i][9] = training_set[i][8]

column1 = ['1 type 1','1 type 2','1 HP','1 Attack','1 Defense', '1 Sp Atk', '1 Sp Def', '1 Speed',\
          '2 type 1','2 type 2','2 HP','2 Attack','2 Defense', '2 Sp Atk', '2 Sp Def', '2 Speed']        
dataframe1 = pd.DataFrame(training_set,columns = column1)
dataframe1.to_csv("G:\\Business Analytics\\Programming for Business Analytics\\features.csv",index = False)

column2 = ['Whether 1 wins']
dataframe2 = pd.DataFrame(training_label,columns = column2)
dataframe2.to_csv("G:\\Business Analytics\\Programming for Business Analytics\\labels.csv",index = False)

T = []   
for i in range(0,50000):
    T.append([training_set[i][0],training_set[i][1],training_set[i][8],training_set[i][9]])

column3 = ['1 type 1','1 type 2','2 type 1','2 type 2',]
dataframe3 = pd.DataFrame(T,columns = column3)
dataframe3.to_csv("G:\\Business Analytics\\Programming for Business Analytics\\type features.csv",index = False)

features = np.array(dataframe1)
labels = np.array(dataframe2)
    

      


    
