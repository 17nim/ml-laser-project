from pynput import mouse

def on_click(x, y, button, pressed):
    """ แสดงค่าพิกัดทุกครั้งที่คลิก """
    if pressed:  # ตรวจจับเฉพาะตอนกดลง
        print(f"ตำแหน่งที่คลิก: x={x}, y={y}, ปุ่ม={button}")

# เริ่มดักจับอีเวนต์เมาส์
with mouse.Listener(on_click=on_click) as listener:
    listener.join()  # รอรับอีเวนต์ไปเรื่อย ๆ
