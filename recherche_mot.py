# -*- coding: utf-8 -*-
from unidecode import unidecode

lettres_inclus = ["t","e","l","p","h","o","n"]
lettres_exclus = []
tailleDuMot = 9

mon_fichier = open("mots_francais.txt", "r")
contenu = mon_fichier.read().split("\n")

#On exclu les champs vide
contenu = [mot for mot in contenu if not len(mot)==0]

if lettres_inclus:
    for lettre in lettres_inclus:
        contenu = [unidecode(mot) for mot in contenu if lettre in unidecode(mot)]

if lettres_exclus:
    for lettre in lettres_exclus:
        contenu = [unidecode(mot) for mot in contenu if lettre not in unidecode(mot)]

if tailleDuMot:
    contenu = [unidecode(mot) for mot in contenu if len(mot) == tailleDuMot]

# La première lettre du mot
# contenu = [mot for mot in contenu if mot[0] == "s"]

print(contenu)
print(len(contenu), 'résultat(s)')

mon_fichier.close()
