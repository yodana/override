def convertir_en_non_signe(nombre):
    if nombre < 0:
        # Si le nombre est négatif, utilisez la représentation complément à deux
        nombre_non_signe = 2**32 + nombre
    else:
        # Si le nombre est positif, il reste non signé
        nombre_non_signe = nombre
    
    return nombre_non_signe

# Demander à l'utilisateur d'entrer un nombre
nombre_entre = int(input("Entrez un nombre (positif ou négatif) : "))

# Appeler la fonction pour convertir en nombre non signé
nombre_non_signe = convertir_en_non_signe(nombre_entre)

# Afficher le résultat
print(f"Le nombre non signé correspondant est : {nombre_non_signe}, 0x{nombre_non_signe:X}")