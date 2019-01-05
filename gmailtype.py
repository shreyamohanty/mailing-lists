import pyautogui
pyautogui.failsafe = True

pyautogui.click(1345, 435)
pyautogui.click(1345, 435)

namelist = open('C:/Users/Shreya Mohanty/Documents/UC Berkeley/Voyager/Spring 2019 Recruitment/namelist.txt', 'r')


while True:
    name = namelist.readline()
    name = name.rstrip()
    pyautogui.PAUSE = 0.3
    pyautogui.typewrite(name)
    pyautogui.press('enter')
    pyautogui.PAUSE = 0

    if name == '':
        break
namelist.close()
