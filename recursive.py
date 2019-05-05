# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 17:33:44 2019

@author: Mouloua
"""
"""
equipeGroupe = {  "FCB": 1, "PSG": 1,
               "BM": 1, "MUC": 1, "Real": 1, "Juve": 1,
          "Atl": 2, "Tot": 2, "LFC": 2, "S04": 2,
               "Ajax": 2, "OL": 2}"""

equipeGroupe = {  "FCB": 1, "PSG": 1,
               "BM": 1, "MUC": 1, "Real": 1, 
          "Atl": 2, "Tot": 2, "LFC": 2, "S04": 2,
               "Ajax": 2}

equipeLettre = {"Dortmund": "A", "FCB": "B", "PSG": "C", "FC Porto": "D",
               "BM": "E", "MUC": "F", "Real": "G", "Juve": "H","Atl": "A", "Tot": "B", "LFC": "C", "S04": "D",
               "Ajax": "E", "OL": "F", "As Roma": "G", "Manchester United": "H"
               }

equipes_nationalites = {"Dortmund": "Allemagne", "FCB": "Espagne", "PSG": "France", "FC Porto": "Portugal",
               "BM": "Allemagne", "MUC": "Angleterre", "Real": "Espagne", "Juve": "Italie",
                        "Atl": "Espagne", "Tot": "Angleterre", "LFC": "Angleterre", "S04": "Allemagne",
               "Ajax": "Pays Bas", "OL": "France", "As Roma": "Italie", "Manchester United": "Angleterre"
                       }

equipeType1=[]
equipeType2=[]
for i in equipeGroupe:
    if equipeGroupe[i]==1:
        equipeType1.append(i)
    else:
        equipeType2.append(i)

equipes=[]
for i in equipeType1:
    equipes.append(i)
    
for i in equipeType2:
    equipes.append(i)

def TirageRecursiveSecondaire(tirage, Tirage, stat):
        for equipe in equipes:
            tirage_copy=list(tirage)
            if len(tirage_copy)<len(equipes) and equipe not in tirage_copy:
                index=len(tirage_copy)
                if(equipeGroupe[equipe]!=equipeGroupe[tirage_copy[index-1]]) and (equipeLettre[equipe]!=equipeLettre[tirage_copy[index-1]])  :
                    tirage_copy.append(equipe)
                    TirageRecursiveSecondaire(tirage_copy, Tirage,stat)
            else:
                if tirage_copy not in Tirage and len(tirage_copy)>=len(equipes):
                    Tirage.append(tirage_copy)
                    stat.append(1)
                elif tirage_copy in Tirage:
                    stat[Tirage.index(tirage_copy)]+=1

def TirageRecursivePrincipale():
    Tirage=[]
    stat=[]
    for equipe in equipeType2:
        tirage=[]
        tirage.append(equipe)
        TirageRecursiveSecondaire(tirage, Tirage,stat)
    print(stat)
    print(len(stat))
    return Tirage



test=[]
testTot=[]
testTirage=TirageRecursivePrincipale()
