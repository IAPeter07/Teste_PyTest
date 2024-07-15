#Importando Componentes (variaveis) de 'functions.py'
from Main.character import character_name
from Main.character import character_lv
from Main.character import character_atk
from Main.character import character_element 
from Main.character import character_ELMB
from Main.character import character_CRTRATE
from Main.character import character_CRTDMG
from Main.character import elementalBonus
from Main.character import crtRATE
from Main.character import crtDMG

#Importando Metodo Construtor
from Main.character import construc_char

character_name = "Kafka"
#Testando variaveis
def test_character_name():
    assert character_name() == "Kafka"

def test_character_lv():
    assert character_lv == 80