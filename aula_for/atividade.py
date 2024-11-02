import pyautogui as py
import time
py.FAILSAFE = True
#assunto = Resultado do Processo Seletivo 
#abrir o gmail:
time.sleep(3)
py.press("win") 
py.typewrite("Goo", interval = 1) 
py.press("enter")
"""y.moveTo(x=555, y=747)
py.click(x=555, y=747)""" #ir na aba chrome
time.sleep(1)
py.moveTo(x=417, y=427, duration = 0.30)
py.click(x=417, y=427)
py.sleep(1) 
py.moveTo(x=1164, y=149, duration = 0.40)
py.click(x=1164, y=149)
time.sleep(7)
#p ir p escreve
py.moveTo(x=33, y=210, duration = 2)
py.click(x = 33, y = 210)
#destino
py.moveTo(x=843, y=307, duration = 2)
py.click(x=843, y=307)
py.typewrite("isabellesilvamaximo@gmail.com", interval = 0.20)
py.press("tab")
#corpoato
py.moveTo(x=822, y=353, duration = 1)
py.click(x=822, y=353)
py.typewrite("Olá! Prezado Candidato(a)", interval = 0.20)
py.moveTo(x=811, y=396)
py.click(x=811, y=396)
py.typewrite("Identificamos que o seu perfil não se encaixa diretamente com a vaga.", interval = 0.20)
py.press("enter")
py.typewrite("Infelizmente não foi desta vez...te vemos na proxima!", interval = 0.20)
py.press("enter")
py.press("enter")
py.typewrite("Atenciosamente Maximo's Acessoria.", interval = 0.20)
#enviar o email
py.press("tab")
py.press("enter")