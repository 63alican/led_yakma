import tkinter as tk
import serial
# Seri port ayarlar:
ser = serial. Serial ('COM5',9600)
def led_yak():
    ser.write (b'y') # Komutu ESP32'ye gönder
    print ("LED yakıld1")
def led_sondur ():
    ser.write (b's')# Kønutu ESP32'ye gönder
    print ("LED söndüruldu")
# Tkinter penceresi O
root = tk.Tk()
root.title ("ESP32 LED Kontrol")
# LED yak butonu
btn_yak = tk.Button (root, text="LED Yak", command=led_yak)
btn_yak. pack(pady=10)
# LED söndür
butonu
btn_sondur = tk.Button(root, text="LED Söndur", command=led_sondur)
btn_sondur. pack(pady=10)
# Pencereyi göster
root.mainloop()