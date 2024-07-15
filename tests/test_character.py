#Importando Componentes (variaveis) de 'functions.py'
from character import character_name
from character import character_lv
from character import character_atk
from character import character_element 
from character import character_ELMB
from character import character_CRTRATE
from character import character_CRTDMG
from character import elementalBonus
from character import crtRATE
from character import crtDMG

#Importando Metodo Construtor
from character import construc_char
from character import critical_Damage
from character import elemental_bonus


#Testes de variaveis
    # Testando Varivel de nome
def test_character_name():
    assert character_name == "Kafka"

    # Testando Varivel de level
def test_character_lv():
    assert character_lv == 80

    # Testando Varivel de ataque
def test_character_atk():
    assert character_atk == 3000

    # Testando Varivel de tipo do elemento
def test_character_element():
    assert character_element == "Lightning"

    # Testando Varivel do bonus elemental
def test_character_elemental_bonus():
    assert character_ELMB == 55.2

    # Testando Varivel de taxa critica
def test_character_critical_rate():
    assert character_CRTRATE == 5

    # Testando Varivel de dano critico
def test_character_critical_damage():
    assert character_CRTDMG == 55

    #Testando Variavel de Conversão de

#Testes de Funções
    # Testando Função de Calculo de CRT
def test_crital_damage():
    assert critical_Damage(character_atk,character_CRTDMG,character_CRTRATE) == 570

    # Testando Função de Calculo de Bonus Elemental
def test_elemental_bonus():
    assert elemental_bonus(character_atk,character_ELMB) == 390