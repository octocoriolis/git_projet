def vitesse_moyenne(distance, duree):
    if duree <= 0:
        raise ValueError("La duree doit etre positive.")
    return distance / duree

def ms_vers_kmh(vitesse_ms):
    return vitesse_ms * 3.6
