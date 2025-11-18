#Pseudocode de la question 1

#Regarder la première lettre du message

#Voir sa position dans la liste cle_gr3

#Voir quel chiffre dans la liste de 1 à 9 correspond à cette position (exemple: Si la lettre "j" commence la liste, sa position est 1)

#Répéter les étapes de 1 à 3 jusqu'attend que toute les lettres dans le mot ont un chiffre associé à eux

#Maitenant, remplacer les lettres du message par les chiffres correspondant de la cle

cle_gr3 = [
    ["a", "b", "c", "d", "e", "f", "g", "h", "i"], ["j", "k", "l", "m", "n", "o", "p", "q", "r"], ["s", "t", "u", "v", "w", "x", "y", "z", "é"],
    ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
]

message = "Je vais réussir cet examen!"

print(cle_gr3[3][0])


