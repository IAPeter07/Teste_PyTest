#Testes Unitarios em Python Utilizando o Pytest
#Utilizando Codigo Base "Character.py",para exemplares de Calculo
#Utilização de mesma estrutura Logica para verificação de retorno

#Importando Componentes (variaveis) de 'character.py'
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

    #Função de verificação de Entrada de Valores de Nome e Level
def check_name_and_lv(name,lv):
    if isinstance(name, str) and lv > 0:
        return "Ok"
    else:
        return "Error"

    #Função de verificação de Entrada de Valores de Ataque e Elemental
def check_atk_and_ELMB(Atk,ELMB):
    if isinstance(Atk,int) and Atk > 0 and ELMB >= 0:
        return "Ok"
    else:
        return "Error"

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

#Testando Parte de Construtor (Checando nome e level do personagem)
    #Normal
def test_check_name_and_lv():
    assert check_name_and_lv("Nome",80) == "Ok"
    #Level menor que 0
def test_check_name_and_lv_2():
    assert check_name_and_lv("Nome",-1) == "Error"
def test_check_name_and_lv_3():
    assert check_name_and_lv("Nome",0) == "Error"


#Testando Parte de Construtor (Checando ataque e Bonus elemental do personagem)
    #Normal
def test_check_atk_and_ELMB():
    assert check_atk_and_ELMB(1,10) == "Ok"
    #Ataque igual a 0
def test_check_atk_and_ELMB2():
    assert check_atk_and_ELMB(0,1) == "Error"
    #Elemental Bonus negativo
def test_check_atk_and_ELMB3():
    assert check_atk_and_ELMB(0,-1) == "Error"
    #Ataque negativo
def test_check_atk_and_ELMB4():
    assert check_atk_and_ELMB(-1,0) == "Error"
    #Ambos Negativos
def test_check_atk_and_ELMB5():
    assert check_atk_and_ELMB(-1,-1) == "Error"