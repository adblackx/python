import mult
import numpy as np
import matplotlib.pyplot as plot
import time
import scipy.optimize


def mesure(function, nb_chiffres):
    avant = time.time()
    nb = [9]*nb_chiffres
    function(nb, nb)
    return time.time()-avant

mesure(mult.somme, 500)
mesure(mult.produit_naif, 100)
mesure(mult.Karatsuba, 500)


tailles=[]
x=[]
i=10
while i<=2560:
    tailles.append([9]*i)
    x.append(i)
    i=i*2
    
resultat_somme=[]
resultat_produit_naif=[]
resultat_Karatsuba=[]

for i in tailles:
    resultat_somme.append(mesure(mult.somme, np.size(i)))
    resultat_produit_naif.append(mesure(mult.produit_naif, np.size(i)))
    resultat_Karatsuba.append(mesure(mult.Karatsuba, np.size(i)))


plot.plot(x, resultat_somme, "ro-", label="Somme")
plot.plot(x, resultat_produit_naif, "go-", label="Produit Naif")
plot.plot(x, resultat_Karatsuba, "bo-", label="Karatsuba")
plot.legend()
plot.title("Temps de calculs en fonction de la taille")
plot.xlabel("Taille du chiffre")
plot.ylabel("Temps en s")
plot.show()

plot.plot(np.log(x),np.log(resultat_produit_naif), "go-", label="Produit Naif")
plot.plot(np.log(x),np.log(resultat_Karatsuba), "bo-", label="Karatsuba")
plot.legend()
plot.title("Temps de calculs en fonction de la taille version logarithmique")
plot.xlabel("Abscisses")
plot.ylabel("Ordonnées")
plot.show()

vX= np.array(np.log(x))
vY_naif= np.array(np.log(resultat_produit_naif))
vY_Karatsuba= np.array(np.log(resultat_Karatsuba))


def func (x,a,b):
    return a*x+b

R= scipy.optimize.curve_fit(func , vX,vY_naif)
alpha_naif= R[0][0]
#alpha_naif = 1.9470444773238826
C_naif=np.exp(R[0][1])
#Cnaif=  6.2311396234131706e-07

R1= scipy.optimize.curve_fit(func , x,vY_Karatsuba)
alpha= R1[0][0]
#alpha_Karatsuba=1.2545763293413482
C_Karatsuba=np.exp(R1[0][1])
#C_Karatsuba= 1.8558190524365732e-06

res_naif=[]
res_Karatsuba=[]

def multiplication(x,a,b):
    return b*pow(x,a)

for i in x:
    res_naif.append(multiplication(i,alpha_naif,C_naif))
    res_Karatsuba.append(multiplication(i,alpha,C_Karatsuba))

#comparaison modèles données
plot.plot(np.log(x),np.log(resultat_produit_naif), "go-", label="Produit Naif")
plot.plot(np.log(x),np.log(resultat_Karatsuba), "bo-", label="Karatsuba")
plot.plot(vX,np.log(res_naif), "ro-", label="Produit Naif")
plot.plot(vX,np.log(res_Karatsuba), "yo-", label="Karatsuba")
plot.legend()
plot.title("Comparaison entre les courbes théoriques et experimentale")
plot.xlabel("log(Taille du chiffre)")
plot.ylabel("Log(temps de calcul)")
plot.show()


def multiplication(x,a,b):
    return b*pow(x,a)

million=1000000
res_naif=multiplication(million,alpha_naif,logCnaif)
#Million_naif=299801 soit 4 jours
res_K=multiplication(million,alpha,C_Karatsuba)
#Million_Karatsuba= 13677 soit 4 heures
#res_nais>>>res_K
