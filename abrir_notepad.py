import pyautogui as posicao

posicao.hotkey('win', 'r')
posicao.sleep(1)

posicao.typewrite('notepad')
posicao.sleep(1)
posicao.press('enter')

posicao.sleep(2)
posicao.typewrite('Abri o bloco de notas com um robo')
    
posicao.sleep(3)
fecharJanelaNotepad = posicao.getActiveWindow()
fecharJanelaNotepad.close()

posicao.sleep(2)
posicao.press('tab')
posicao.sleep(2)
posicao.press('enter')

