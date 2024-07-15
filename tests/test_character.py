#Importando Componentes (variaveis) de 'functions.py'
from character import character_atk
from character import character_ELMB
from character import character_CRTRATE
from character import character_CRTDMG

#SKILLS CHAR
def char_basic_skill(atk):
    dano = ((atk * 50)/100)
    return round(dano)
def char_E_skill(atk):
    dano = ((atk * 100)/100)
    return round(dano)
def char_ultimate_skill(atk):
    dano = ((atk * 200)/100)
    return round(dano)

#FUNÇÔES
    #Função de Calcular o CRT
def critical_Damage(dano,CRTDMG,CRTRATE):
    crt = (dano * (1 + (CRTDMG * CRTRATE)))
    return round(crt)

    #Função de Calculo do Bonus Elemental
def elemental_bonus(atk,Elemental_Bonus):
    acr = (atk * Elemental_Bonus)
    dano = (atk + acr)
    return round(dano)

#Testes de variaveis
 # Testando de bonus elemental
def test_character_elemental_bonus():
    assert character_ELMB == 0.552
# Testando Varivel de taxa critica
def test_character_critical_rate():
    assert character_CRTRATE == 0.05
# Testando Varivel de dano critico
def test_character_critical_damage():
    assert character_CRTDMG == 0.55

#Testando Funções de Skills do Personagem
# Testando Ataque Basico
def test_basic_skill():
    assert char_basic_skill(character_atk) == 1500
# Testando Pericia
def test_E_skill():
    assert char_E_skill(character_atk) ==  3000
# Testando Pericia Suprema
def test_ultimate_skill():
    assert char_ultimate_skill(character_atk) == 6000

#Variavel de resultado para teste de funções abaixo utilizando de base resultado da Basic Skill
dano = char_basic_skill(character_atk)

#Testando Função de Calculo de CRT
def test_crital_damage():
    assert critical_Damage(dano,character_CRTDMG,character_CRTRATE) == 1541

#Testando Função de Calculo de Bonus Elemental
def test_elemental_bonus():
    assert elemental_bonus(dano,character_ELMB) == 2328