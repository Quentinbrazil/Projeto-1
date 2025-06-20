# -*- coding: utf-8 -*-
"""
Created on Thu Jun 19 19:37:49 2025

@author: Devorsine
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

R = 0.01 
D= 2*R      
U = 0.05

fichier_csv = 'profil_numerique.csv'

df = pd.read_csv(fichier_csv) 

def u_analytique (r):
    return 2*U*(1-(r/R)**2)

r = df['Points:1']
u_numerique = df['U:0']
u_analytique_val = u_analytique(r)
u_numerique_moyen = u_numerique.sum()/1001
E = (0.05-u_numerique_moyen)/0.05*100
print('velocidade media da simulaçao : ',u_numerique_moyen )
print('erro relativo : ', E, '%')



plt.figure(figsize=(8, 6))
plt.plot(r, u_numerique, 'o', label='Numérique (OpenFOAM)', markersize=4)
plt.plot(r, u_analytique_val, '-', label='Analytique (Poiseuille)', linewidth=2)
plt.xlabel('Distance Radiale (m)')
plt.ylabel('Vitesse Axiale (m/s)')
plt.title('Comparaison des Profils de Vitesse')
plt.grid(True)
plt.legend()
plt.show()