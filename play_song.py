import cv2
import mediapipe as mp
import numpy as np
import subprocess
import time
import pyautogui

def openPetrunko() :
    subprocess.run(["open", "-a", "SoundSwitch"])
    time.sleep(1)  # รอให้แอปเปิดก่อน
                #pyautogui.click(x=794.0078125, y=842.26171875)  # ปรับตำแหน่งให้ตรงกับโฟลเดอร์
    time.sleep(1)  # รอให้แอปเปิดก่อน
    pyautogui.click(x=153, y=220)  # ปรับตำแหน่งให้ตรงกับโฟลเดอร์
    time.sleep(1)  # รอให้แอปเปิดก่อน
    pyautogui.click(x=143, y=237)  # ปรับตำแหน่งให้ตรงกับโฟลเดอร์
    time.sleep(1)
    pyautogui.doubleClick(x=502, y=156)  # ปรับตำแหน่งให้ตรงกับโฟลเดอร์
    time.sleep(1)  # รอให้แอปเปิดก่อน
                
    pyautogui.hotkey("shift", "space")
    pyautogui.press("space")  # กดปุ่ม Play
    return "Wide Hands Pose (Petrunko).."

def openFunkonaut():
    subprocess.run(["open", "-a", "SoundSwitch"])
    time.sleep(1)  # รอให้แอปเปิดก่อน
                #pyautogui.click(x=794.0078125, y=842.26171875)  # ปรับตำแหน่งให้ตรงกับโฟลเดอร์
    time.sleep(1)  # รอให้แอปเปิดก่อน
    pyautogui.click(x=153, y=220)  # ปรับตำแหน่งให้ตรงกับโฟลเดอร์
    time.sleep(1)  # รอให้แอปเปิดก่อน
    pyautogui.click(x=143, y=237)  # ปรับตำแหน่งให้ตรงกับโฟลเดอร์
    time.sleep(1)
    pyautogui.doubleClick(x=411, y=132)
    time.sleep(1)  # รอให้แอปเปิดก่อน
                
    pyautogui.hotkey("shift", "space")
    pyautogui.press("space")  # กดปุ่ม Play
    return "Hands Up (FunkonAut).."

def openAstroFunk():
    subprocess.run(["open", "-a", "SoundSwitch"])
    time.sleep(1)  # รอให้แอปเปิดก่อน
                #pyautogui.click(x=794.0078125, y=842.26171875)  # ปรับตำแหน่งให้ตรงกับโฟลเดอร์
    time.sleep(1)  # รอให้แอปเปิดก่อน
    pyautogui.click(x=153, y=220)  # ปรับตำแหน่งให้ตรงกับโฟลเดอร์
    time.sleep(1)  # รอให้แอปเปิดก่อน
    pyautogui.click(x=143, y=237)  # ปรับตำแหน่งให้ตรงกับโฟลเดอร์
    time.sleep(1)
    pyautogui.doubleClick(x=371, y=179)
    time.sleep(1)  # รอให้แอปเปิดก่อน
                
    pyautogui.hotkey("shift", "space")
    pyautogui.press("space")  # กดปุ่ม Play
    return "(AstroFunk).."