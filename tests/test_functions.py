#Testes Unitarios em Python Utilizando o Pytest
#Utilizando Codigo Base "functions.py",para exemplares de Calculo
#Utilização de Valores individuais exemplares para Calcular um Resultado esperado

#Importando Componentes de 'functions.py'
from functions import critical_Damage
from functions import elemental_bonus

#Variaveis Para Testar as Funções
    #Dano Critico
crtDMG = (120/100)
    #Taxa Critica
crtRate = (75/100)
    #Bonus Elemental
char_ELMB = (30/100)

#Testando Função de Calculo de CRT
def test_crital_damage():
    assert critical_Damage(300,crtDMG,crtRate) == 570

#Testando Função de Calculo de Bonus Elemental
def test_elemental_bonus():
    assert elemental_bonus(300,char_ELMB) == 390

