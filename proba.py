# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 17:33:44 2019

@author: Mouloua
"""
"""
equipeGroupe = {  "FCB": 1, "PSG": 1,
               "BM": 1, "MUC": 1, "Real": 1, "Juve": 1,
          "Atl": 2, "Tot": 2, "LFC": 2, "S04": 2,
               "Ajax": 2, "OL": 2}

equipeLettre = {"Dortmund": "A", "FCB": "B", "PSG": "C", "FC Porto": "D",
               "BM": "E", "MUC": "F", "Real": "G", "Juve": "H","Atl": "A", "Tot": "B", "LFC": "C", "S04": "D",
               "Ajax": "E", "OL": "F", "As Roma": "G", "Manchester United": "H"
               }

equipes_nationalites = {"Dortmund": "Allemagne", "FCB": "Espagne", "PSG": "France", "FC Porto": "Portugal",
               "BM": "Allemagne", "MUC": "Angleterre", "Real": "Espagne", "Juve": "Italie",
                        "Atl": "Espagne", "Tot": "Angleterre", "LFC": "Angleterre", "S04": "Allemagne",
               "Ajax": "Pays Bas", "OL": "France", "As Roma": "Italie", "Manchester United": "Angleterre"
                       }"""

equipeGroupe = { "MU": 1, "PSG": 1, "LFC": 1, "Tot":1,
          "BM": 2, "Juve": 2, "Real": 2, "Porto":2}
equipeLettre = { "MU": "A", "PSG": "B", "LFC": "C","Tot": "D","Manchester City": "E","Schalke 04": "F",
          "BM": "A", "Juve": "B", "Real": "C", "Porto": "D", "As Roma": "E","Atletico de Madrid": "F",}

def carreIdentique(Equipesss1, Equipesss2):
    return ((equipeLettre[Equipesss1[0]]==equipeLettre[Equipesss2[0]]) 
      and (equipeLettre[Equipesss1[1]]==equipeLettre[Equipesss2[1]])) or ((equipeLettre[Equipesss1[1]]==equipeLettre[Equipesss2[0]]) and (equipeLettre[Equipesss1[0]]==equipeLettre[Equipesss2[1]]))

def TirageEquipe2ProbaExact(EquipeDisponibles, Equipe):
    entier=0
    for v in EquipeDisponibles:
        if((equipeLettre[Equipe]!=equipeLettre[v])) and (equipeGroupe[Equipe]!=equipeGroupe[v]) :
            entier+=1
    return entier

def TiragePrincipaleProbaExact(ListePrincipale):
    equipe1=[]
    equipe2=[]
    probabilite=1
    for i in ListePrincipale:
        if equipeGroupe[i]==1:
            equipe1.append(i)
        else:
            equipe2.append(i)
    while(len(equipe1)!=0):
        if len(equipe1)>2:
            choixposs=TirageEquipe2ProbaExact(equipe1, equipe2[0])
            probabilite*=choixposs
            probabilite*=len(equipe1)
        else:
            if carreIdentique(equipe1, equipe2)==1:
                return probabilite
            else:
                probabilite*=len(equipe1)
                choixposs=TirageEquipe2ProbaExact(equipe1, equipe2[0])
                if(choixposs==1) :
                    return probabilite
                probabilite*=choixposs
                return probabilite
        del equipe1[0]
        del equipe2[0]
    return probabilite

print(TiragePrincipaleProbaExact( ['Juve', 'MU', 'Porto', 'LFC', 'BM', 'PSG', 'Real', 'Tot'])) #288
print(TiragePrincipaleProbaExact( ['Juve', 'MU', 'BM', 'PSG', 'Real', 'Tot','Porto', 'LFC'])) #108
print(TiragePrincipaleProbaExact(['Real', 'MU', 'Juve', 'LFC', 'Porto', 'PSG', 'BM', 'Tot'])) #144
print(TiragePrincipaleProbaExact(['Real', 'MU', 'Juve', 'Tot', 'BM', 'LFC', 'Porto', 'PSG'])) #288
print("done !")