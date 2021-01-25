import pyautogui, time
time.sleep(3)
for i in range(10):
    pyautogui.write("Hello world")
    pyautogui.press('enter')
    time.sleep(1)