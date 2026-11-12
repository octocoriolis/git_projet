def vitesse_moyenne(distance, duree):
    if duree <= 0:
        raise ValueError("La duree doit etre positive.")
    return distance / duree
