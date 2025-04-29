import pyautogui
import time
import webbrowser

webbrowser.open("https://moodle.mcu.edu.tw/")
time.sleep(3)

pyautogui.click(226, 455)
pyautogui.write("學號沒差", interval=0.1)

pyautogui.press("tab")
pyautogui.write("*************", interval=0.1)

pyautogui.press("enter")
time.sleep(1)

course_btn = pyautogui.locateCenterOnScreen("test01.png", confidence=0.8)

if course_btn:
    pyautogui.moveTo(course_btn)
    pyautogui.click()