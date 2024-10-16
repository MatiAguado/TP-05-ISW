def verificar_patente(nro_patente):
    if len(nro_patente) == 0:
        return 'Error en el numero de patente'
    else:
        return True

def determinar_precio_patentes(nroPatente, mod, valorAuto):
    modelo = mod.replace(" ","")
    valor_auto = valorAuto.replace(" ","")
    patente = verificar_patente(nroPatente)
    if patente == 'Error en el numero de patente':
        return 'Error en el numero de patente'
    if len(valor_auto) == 0:
        return 'Error en el valor del auto'
    else:
        if int(valor_auto) == 0:
            return 'Error en el valor del auto'     
    if len(modelo) == 0:
        return 'Error en la fecha del modelo'
    else:
        antiguedad = 2024 - int(modelo)
        if int(modelo) == 0 or int(modelo) > 2024:
            return 'Error en la fecha del modelo'
        if 0 <= antiguedad <= 5:
                tasa = 0.05  # 5% del valor del auto
        elif 6 <= antiguedad <= 10:
                tasa = 0.03  # 3% del valor del auto
        elif 11 <= antiguedad <= 25:
                tasa = 0.01  # 1% del valor del auto
        elif antiguedad > 25:
                tasa = 0     # No paga tasa de patente    
        precio_patente = int(valor_auto) * tasa
        return precio_patente