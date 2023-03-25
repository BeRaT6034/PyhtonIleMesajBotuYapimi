import pyautogui
import time

def mesajİslemi():
    tekrar= int(input("Kaç Tekrarlamak İstersin...:"))
    mesaj= input("Hangi Mesaji Tekrarlamak İstersin...: ")
    for i in range(tekrar):
        time.sleep(2)
        pyautogui.write(mesaj)
        pyautogui.press("enter")

while True:
    mesajİslemi()