#!/usr/bin/python2

#-----------------

#CALCUL D'ENTIER


#a = 10

#b = 5

#print(a+b)

#-----------------

#ASSIGNATION ET REASSIGNATION

#age = "je suis vieux"

#print(age)

#age = "je suis jeune"

#print(age)

#-----------------


#REMONTE DE TYPE

#text = "je suis du texte"

#print(type(text))

#nombre = 42

#print(type(nombre))

#-----------------

#CONCATENATION

#text= "je suis du texte"

#print(text *3)

#text = text+" en plus"




#print(text)

#txt = "hello world"

#print(len(txt))

#print(txt([1])

#print (txt[0:5])

#print



#text = "je suis du \"texte \""

#print(text)

#-----------------


#LES LISTES

#maListe = []

#print(type(maListe))

#maListe = [1, 2, 3]

#print(maListe)

#maListe = []

#maListe.append(1)

#print(maListe)

#maListe.append("salut")

#print(maListe)

#-----------------

#SORTIR UN ELEMENT

maListe = ["1er", "duexieme", "troisieme" ]

print(maListe[1])

print(maListe[2])

#-----------------

#REASSIGNEMENT DE VALEUR

maListe[1] = "changement"

print(maListe)

#-----------------

#SUPRIMER UN ELEMENT

maListe = ["1er", "duexieme", "troisieme" ]

#supprimer avec l'index

del (maListe[1])

print(maListe)

#-----------------

#SUPPRIMER AVEC LA VALEUR

maListe.remove("troisieme")

print(maListe)

#-----------------

maListe = ["1er", "deuxieme", "troisieme"]
secondeList = maListe
maListe[0] = "toto"
print(secondeList)


maListe = ["1er", "deuxieme", "troisieme"]
secondeList = maListe[:]
maListe[0] = "toto"
print(secondeList)


maListe = ["1er", "deuxieme", "troisieme"]
print("1er" in maListe)
print ("toto" in maListe)

maListe = list(range(15))
print(maListe)

liste = list(range(10))
liste.extend(maListe)
print(liste)

#----------------- TRIE A BULLES

def bubule():
  list = [4, 8, 415, 1, 25, 75, 6]
  last = True
  limit = len(list)
  while last:
     for i in range(0, limit-1):
        last = False
        if (list[i] > list[i+1]):
           list[i+1], list[i] = list[i], list[i+1]
           last = True
     limit = limit - 1
  print(list)

#----------------- TRI PAR INSERTION

def insertion():
  list = [4, 8, 415, 1, 25, 75, 6]
  for i in range(1, len(list)):
     current = list[i]
     j = i
     while j > 0 and list[j - 1] > current:
        list[j] = list[j - 1]
        j = j - 1
     list[j] = current
  print(list)


def table(nb, max=10):
    for i in range(1,max+1):
        print(i, " * ", nb, " = ", i * nb)


def exo04():
    mot =input("entrez un mot")
    print (len(mot))

#def exo05():
   # nbr = input("Entrez un nombre")
    #if (nbr % 2 = 1)
        #print ("pair")
    #else
        #print("impair")


#def exo06():
    #print ("ecrires un nombre en ")
    #nbr=int(input())
    #if number < 10
        #print("plus petit !" )
    #else
        #print("Plus grand")

#08 Ecrire un programme qui demande un nombre de depart, et qui ensuite ecrit la table de multiplication de ce nombre.

def exo08():
    nbr = int(input("nombre de depart"))
    max = 10
    for i in range(1,max+1):
        print(i, " * ", nbr, " = ", i * nb)


#09 Ecrire un programme qui demande un nombre de depart

def exo09():
    Somme=0
    nbr=int(input(" saisir un nombre  de depart"))
    for i in range(1, nbr+1):
        somme = somme + i
    print(somme)


def exo09():
    n = input(" saisir un nombre  de depart")
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s

#10 Ecrire un programme qui demande age un enfant
#Poussin de 6 a 7 ans
#Pupille de 8 a 9 ans
#Minime de 10 a 11 ans
#Cadet apres 12 ans

def exo10():
    age = int(input(" Entrez l'age de l'enfant :"))
    if age >= 12:
        print("Cadet")
    elif age >= 10:
        print("Minine")
    elif age >= 8:
        print("Pupille")
    elif age >= 6:
        print("Poussin")
    elif age <= 5:
        print("Trop petit")
    exo10()


#11 Ecrivez un programme qui calcule le prix TTC

def exo11():
    prixU = int(input("Entrez le prix unitaire"))
    nbr =int(input("Entrez le nombre"))
    tva = int(input("Entrez la TVA"))

    prixTtc = ( prixU * nbr) * (1 * (tva/100))
    print(" Nombre d'article " + str(nbr))
    print(" Prix unitaire " + str(prixU))
    print(" Prix TTC " + str(prixTtc))


#12 Ecrire un programme qui calcule la factorielle de n.

def exo12(n):

    if n<2:
        return 1
    else:
        return n*fact(n-1)
    print(exo12(10))

#13 Ecrire un programme qui convertit un nombre d'?cimal (base 10) en binaire

def exo13(n):
    """Convertit un nombre en binaire"""
    q = -1
    res = ''
    while q != 0:
        q = n // 2
        r = n % 2
        res = `r` + res
        n = q
    return res
print(exo13(10))

#14 si nous listons tous les nombres naturels inferieurs


from Tkinter import *
fenetre = Tk()
label = Label(fenetre, text="Hello World")
label.pack()
fenetre.mainloop()
