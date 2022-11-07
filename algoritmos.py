def aire(bares_iniciales=0, bares_finales=0, porcentaje_inicial_o2=21, porcentaje_final_o2=21, porcentaje_inicial_he=0, porcentaje_final_he=0):
    bares_nuevos = bares_finales - bares_iniciales # Cuantos bares tengo que llenar?

    # Helio
    bares_he_originales = bares_iniciales * porcentaje_inicial_he / 100 # Calculo los bares que tenia
    porcentaje_final_he = 100 * bares_he_originales / bares_finales # Esos bares el nuevo porcentaje en la botella llena

    # Oxigeno
    bares_o2_originales = bares_iniciales * porcentaje_inicial_o2 / 100 # Calculo los bares que tenia
    porcentaje_final_o2 = 100 * (bares_o2_originales + bares_nuevos * 0.21) / bares_finales


    resultado = {
        'porcentaje_o2': porcentaje_final_o2,
        'porcentaje_he': porcentaje_final_he,
        'bares_aire': bares_nuevos,
        'bares_o2': 0,
        'bares_he': 0,
    }
    return resultado


def pp(bares_iniciales=0, bares_finales=0, porcentaje_inicial_o2=21, porcentaje_final_o2=21, porcentaje_inicial_he=0, porcentaje_final_he=0):
    



def calculo_costes(volumen, bares_aire, bares_o2, bares_he, precio_aire=0.001, precio_o2=0.01, precio_he=0.09):
    litros_aire = volumen * bares_aire
    coste_aire = litros_aire * precio_aire

    litros_o2 = volumen * bares_o2
    coste_o2 = litros_o2 * precio_o2

    litros_he = volumen * bares_he
    coste_he = litros_he * precio_he

    coste_total = coste_aire + coste_o2 + coste_he

    resultado = {
        'aire': f"{coste_aire:.2f} €",
        'o2': f"{coste_o2:.2f} €",
        'he': f"{coste_he:.2f} €",
        'total': f"{coste_total:.2f} €",
    }
    return resultado