import cv2
import mediapipe as mp
import numpy as np
import subprocess
import time
import pyautogui

def openPetrunko () :
    subprocess.run(["open", "-a", "SoundSwitch"])
    time.sleep(1)  # รอให้แอปเปิดก่อน
                #pyautogui.click(x=794.0078125, y=842.26171875)  # ปรับตำแหน่งให้ตรงกับโฟลเดอร์
    time.sleep(1)  # รอให้แอปเปิดก่อน
    pyautogui.click(x=153.5078125, y=220.4765625)  # ปรับตำแหน่งให้ตรงกับโฟลเดอร์
    time.sleep(1)  # รอให้แอปเปิดก่อน
    pyautogui.click(x=143.34765625, y=237.89453125)  # ปรับตำแหน่งให้ตรงกับโฟลเดอร์
    time.sleep(1)
    pyautogui.doubleClick(x=502.5, y=156.59765625)  # ปรับตำแหน่งให้ตรงกับโฟลเดอร์
    time.sleep(1)  # รอให้แอปเปิดก่อน
                
    pyautogui.hotkey("shift", "space")
    pyautogui.press("space")  # กดปุ่ม Play
    return "Hand Up (FunkonAut).."

def openFunkonaut  ():
    subprocess.run(["open", "-a", "SoundSwitch"])
    time.sleep(1)  # รอให้แอปเปิดก่อน
                #pyautogui.click(x=794.0078125, y=842.26171875)  # ปรับตำแหน่งให้ตรงกับโฟลเดอร์
    time.sleep(1)  # รอให้แอปเปิดก่อน
    pyautogui.click(x=153.5078125, y=220.4765625)  # ปรับตำแหน่งให้ตรงกับโฟลเดอร์
    time.sleep(1)  # รอให้แอปเปิดก่อน
    pyautogui.click(x=143.34765625, y=237.89453125)  # ปรับตำแหน่งให้ตรงกับโฟลเดอร์
    time.sleep(1)
    pyautogui.doubleClick(x=411.3359375, y=132.29296875)
    time.sleep(1)  # รอให้แอปเปิดก่อน
                
    pyautogui.hotkey("shift", "space")
    pyautogui.press("space")  # กดปุ่ม Play
    return "titanic pose (Petrunko).."

def openAstroFunk ():
    subprocess.run(["open", "-a", "SoundSwitch"])
    time.sleep(1)  # รอให้แอปเปิดก่อน
                #pyautogui.click(x=794.0078125, y=842.26171875)  # ปรับตำแหน่งให้ตรงกับโฟลเดอร์
    time.sleep(1)  # รอให้แอปเปิดก่อน
    pyautogui.click(x=153.5078125, y=220.4765625)  # ปรับตำแหน่งให้ตรงกับโฟลเดอร์
    time.sleep(1)  # รอให้แอปเปิดก่อน
    pyautogui.click(x=143.34765625, y=237.89453125)  # ปรับตำแหน่งให้ตรงกับโฟลเดอร์
    time.sleep(1)
    pyautogui.doubleClick(x=371.734375, y=179.43359375)
    time.sleep(1)  # รอให้แอปเปิดก่อน
                
    pyautogui.hotkey("shift", "space")
    pyautogui.press("space")  # กดปุ่ม Play
    return ".."