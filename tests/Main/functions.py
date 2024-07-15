#Função de Calcular o CRT
def critical_Damage(dano,CRTDMG,CRTRATE):
    crt = (dano * (1 + (CRTDMG * CRTRATE)))
    return crt

#Função de Calculo do Bonus Elemental
def elemental_bonus(atk,Elemental_Bonus):
    acr = (atk * Elemental_Bonus)
    dano = (atk + acr)
    return dano