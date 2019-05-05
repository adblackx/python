# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 17:33:44 2019

@author: Mouloua
"""
import copy
import random



equipe = {  "FCB": 1, "PSG": 1,
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
                       }

def tirageRencontreCarer(rencontre, equipePossibles):
    carreListe=[]
    vide=0
    while(len(carreListe)!=len(equipe)/2): #CHANGEMENT A FAIRE ICI, RECHERCHE D OPTIMISATION EN COURS
        carreListe=[]
        equipePossiblesCopy=list(equipePossibles)
        random.shuffle(equipePossiblesCopy)
        #print(equipePossiblesCopy)
        compteur=0
        while compteur<len(equipe)/2:
        	tirageRencontre(carreListe, equipePossiblesCopy)
        	compteur+=1
       
        for i in carreListe:
            for a in i:
                #print("taille de a")
                #print len(a)
                if len(a)==0:
                    vide=1
        if vide==1:
            carreListe=[]
            vide=0
    for e in carreListe:
        rencontre.append(e)
    del equipePossibles[:]

#AJOUT FONCTION POUR LES 4 DERNIERES EQUIPES
def tirageRencontre(rencontre, equipePossibles):
    tirageEquipe1=0
    tirageEquipe2=0
    equipeType=[]
    #print("Equipes possibles:")
    #print(equipePossibles)
    random.shuffle(equipePossibles)
    for e1 in equipePossibles:
        if equipe[e1]==2 and tirageEquipe1==0:
            #rencontre.append(e1)
            equipeType.append(e1)
            equipePossibles.remove(e1)
            tirageEquipe1=1
    for e2 in equipePossibles:
        if equipe[e2]==1 and equipeLettre[e2]!=equipeLettre[equipeType[0]] and tirageEquipe2==0:
            #rencontre.append(e2)
            equipeType.append(e2)
            equipePossibles.remove(e2)
            tirageEquipe2=1
    #print("Equipes tirees")
    #print((equipeType2,equipeType1))
    if len(equipeType)>1:
        rencontre.append((equipeType[0],equipeType[1]))
    else:
        rencontre.append(([],[]))

import random
def tirage():
    poule=[]
    equipePossibles=[]
    for e1 in equipe:
        equipePossibles.append(e1)
    #print(equipePossibles)
    random.shuffle(equipePossibles)
    while len(equipePossibles)!=0:
        tirageRencontreCarer(poule, equipePossibles)
        #print(poule)
        #print(equipePossibles)
    return poule



def binomeidentiques(binome1,binome2):
    compteur1=0
    for b1 in binome1:
        for b2 in binome2:
            if b1==b2:
                compteur1+=1
    if compteur1==2:
        return 1
    else:
        return 0


def PouleDejaTiree(Poules, pouletiree,stats):
    while(len(Poules)>len(stats)):
        stats.append(1)
    for p in Poules:
        compteurDejaTiree=0
        for p1 in p:
            for p2 in pouletiree:
                if(binomeidentiques(p1,p2)==1):
                    #print(p1,p2)
                    compteurDejaTiree+=1
        #print(compteurDejaTiree)
        if compteurDejaTiree==len(pouletiree):
            stats[Poules.index(p)]+=1
            #print(Poules.index(p))
            return 1
    return 0


def tirageGlobal():
    Poules=[]
    compteurGlobal=0
    stats=[]
    while(compteurGlobal<1000):
        pouletiree=tirage()
        if len(pouletiree)>0:
            if PouleDejaTiree(Poules, pouletiree,stats)==0:
                Poules.append(pouletiree)
        compteurGlobal+=1
    a=[]
    for i in stats:
        a.append(i/1000)
    print(a)
    print(stats)
    return Poules

test=[]
test=tirageGlobal()
print(test)
len(test)