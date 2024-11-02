import pyautogui 
"""import pyautogui as XX""" #dar apelido - nome mais curto
import time

pyautogui.FAILSAFE = True #para n perder o controle da automação, fazendo com q ele pare quando entra na posição 00 (canto da tela)

"pyautogui.PAUSE = 0.3""" #pausa geral - para tds os comandos

time.sleep(1) #esperar tempo para pegar a posição ( no caso 5 seg) - usado as vezes no lugar do pause 
"""print(pyautogui.position())""" #pegar posição do mouse:


#pegar tamanho da tela:
"""print(pyautogui.size())"""

#clicar automatico: 
"""pyautogui.click(x = 500, y = 420, button = "right")""" #button serve para indicar o botão do mouse wue sera clicado

#dois clicks:
""" pyautogui.click(x = 403, y = 363 , clicks = 2) """

#mover mouse:
""" pyautogui.moveTo(x=602, y=187,  duration = 1)
pyautogui.moveTo(x=1167, y=265,  duration = 1)
pyautogui.click(x=1159, y=270,  duration = 1)
pyautogui.scroll(-1500)
pyautogui.click(x=1344, y=179,  duration = 1) """


#usar teclado:
pyautogui.press("win")

#para escrever:
pyautogui.write("clima", interval = 0.25)

pyautogui.press("enter")

#pressionar duas teclas - como o copiar:
pyautogui.hotkey("ctrl", "c")




