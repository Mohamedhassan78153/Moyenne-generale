print("MOHAMED HASSAN MOHAMED")
print("◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙◙")
n1 =float(input("saisir la note Cryptographie: "))
n2 =float(input("saisir la note Python: "))
n3 =float(input("saisir la note Réseau: "))
n4 =float(input("saisir la note Mathématique: "))
n5 =float(input("saisir la note Routage: "))
n6 =float(input("saisir la note Analyse des données: "))
n7 =float(input("saisir la note windows servers: "))
Moyenne = (n1+n2+n3+n4+n5+n6+n7)/7
print("la moyenne de l'etudiant est : ",format(Moyenne,".2f"))
if Moyenne < 10 :
    print("Résultat Insuffisant, Semestre Non-Validé")
elif Moyenne >=10 and Moyenne < 12 :
    print("Résultat Mention Passable, Semestre Validé")
    print("Admis(e) en classe Supérieur")
elif Moyenne >=12 and Moyenne < 14 :
    print("Résultat Mention Assez-Bien, Semestre Validé")
    print("Admis(e) en classe Supérieur")
elif Moyenne >=14 and Moyenne < 16 :
    print("Résultat Mention Bien, Semestre Validé")
    print("Admis(e) en classe Supérieur")
elif Moyenne >=16 and Moyenne < 18 :
    print("Résultat Mention Très-Bien, Semestre Validé")
    print("Admis(e) en classe Supérieur")
else :
    print("Résultat Mention Excellent, Semestre Validé")
    print("bravo, excellent travail")
    print("Admis(e) en classe Supérieur")



