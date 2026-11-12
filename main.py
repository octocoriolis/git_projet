from calculs import vitesse_moyenne, ms_vers_kmh

if __name__ == "__main__":
    distance = 100.0   # en metres
    duree = 20.0       # en secondes
    v_ms = vitesse_moyenne(distance, duree)
    v_kmh = ms_vers_kmh(v_ms)
    print(f"Vitesse moyenne : {v_ms:.2f} m/s")
    print(f"Vitesse moyenne : {v_kmh:.2f} km/h")
