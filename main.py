from calculs import vitesse_moyenne

if __name__ == "__main__":
    distance = 18.0
    duree = 2.0
    vitesse = vitesse_moyenne(distance, duree)
    print(f"Vitesse Moyenne : {vitesse:.2f} km/h")
