#Variaveis Iniciais da Construção do Persoangem
    # Variavel de nome
character_name = ("Kafka")
    # Variavel de Level
character_lv = (80)
    # Variavel de ataque 
character_atk = (3000)
    # Variavel de Elemento 
character_element = ("Lightning") 
    # Varaivel de Bonus Elemental
character_ELMB = (55.2/100) #Inserir Valor em % para ser convertido em Decimal
    # Variavel de Taxa Critica
character_CRTRATE = (5/100) #Inserir Valor em % para ser convertido em Decimal
    # Variavel de Dano Critico
character_CRTDMG =  (55/100) #Inserir Valor em % para ser convertido em Decimal
        
#importando Função para calculo do CRT
from functions import critical_Damage
from functions import elemental_bonus

#Construtor de Personagem
def construct_char(char_Name,char_LV,char_element,char_ELMB,char_Atk,char_CRTDMG,char_CRTRATE):
    #Verificando Entrada de Valores de Nome e Level
    if (char_Name != None and char_LV > 0):
        print(f"-- {char_Name} Skills [LV{char_LV}] --")
    else:
        print("Error: Invalid Level or Name,Try Again")
        exit
    
    #Verificando o valor do Tipo de Elemento
    if character_element in ["Physical","Fire","Ice","Imaginary","Quantum","Wind","Lightning"]:
        print(f"-- Element: {char_element} --\n")

    else:
        print("invalid Element,Try Again")
        exit

    #Verificando a Entrada dos Valores de Ataque e Bonus Elemental
    if char_Atk > 0 and char_ELMB > 0:
        def char_basic_skill(atk):
            dano = ((atk * 50)/100)
            #Aplicando Bonus Elemental
            danoE = elemental_bonus(dano,char_ELMB)
            #Calculando CRT
            crt = critical_Damage(danoE,char_CRTRATE,char_CRTDMG)
            print(f"{char_Name} Basic Skill DMG: {round(danoE)} - [CRT]:{round(crt)}")

        def char_E_skill(atk):
            dano = ((atk * 100)/100)
            #Aplicando Bonus Elemental
            danoE = elemental_bonus(dano,char_ELMB)
            #Calculando CRT
            crt = critical_Damage(danoE,char_CRTRATE,char_CRTDMG)
            print(f"{char_Name} E-Skill DMG: {round(danoE)} - [CRT]:{round(crt)}")
                    
        def char_ultimate_skill(atk):
            dano = ((atk * 200)/100)
            #Aplicando Bonus Elemental
            danoE = elemental_bonus(dano,char_ELMB)
            #Calculando CRT
            crt = critical_Damage(danoE,char_CRTRATE,char_CRTDMG)
            print(f"{char_Name} Ultimate Skill DMG: {round(danoE)} - [CRT]:{round(crt)}\n")
                        
        #ATIVAÇÂO DE SKILLS
        char_basic_skill(char_Atk)
        char_E_skill(char_Atk)
        char_ultimate_skill(char_Atk)
    else:
        print("Invalid ATK or Elemental Bonus")
        exit

#ATIVAÇÂO DO CONSTRUTOR
construct_char(character_name,character_lv,character_element,character_ELMB,character_atk,character_CRTDMG,character_CRTRATE)