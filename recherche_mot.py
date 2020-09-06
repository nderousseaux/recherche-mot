lettres_inclus = ["c","e","s","t","u"]
lettres_exclus = ["a","b","d","f","g","h","i","j","q","l","m","n","o","p","q","r","v","w","x","y","z"]
tailleDuMot = None

mon_fichier = open("mots_francais.txt", "r")
contenu = mon_fichier.read().split("\n")

#On exclu les champs vide
contenu = [mot for mot in contenu if not len(mot)==0]

if lettres_inclus:
    for lettre in lettres_inclus:
        contenu = [mot for mot in contenu if lettre in mot]

if lettres_exclus:
    for lettre in lettres_exclus:
        contenu = [mot for mot in contenu if lettre not in mot]

if tailleDuMot:
    contenu = [mot for mot in contenu if len(mot) == tailleDuMot]

#La première lettre du mot
# contenu = [mot for mot in contenu if mot[0] == "s"]


print(contenu)
print(len(contenu), 'résultat(s)')

mon_fichier.close()
