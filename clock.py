import tkinter as tk
from tkinter import Canvas
import math
import time
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
# Jadwal untuk setiap jam
jadwal = [
    "Breakfast", "Ngedrakor", "Baca Buku", "Coding", "Baca Buku", "Scroll IG", "Ngopi", "Scroll Tiktok",
    "Bermain Game", "Coding", "Mendengar Musik", "Istirahat"
]

# Fungsi untuk menggambar jam analog
def draw_clock(canvas, hour, minute, second):
    canvas.delete("all")
    width = 400
    height = 400
    radius = 180
    center_x = width // 2
    center_y = height // 2

    # Gambar lingkaran jam
    canvas.create_oval(center_x - radius, center_y - radius, center_x + radius, center_y + radius)

    # Gambar angka dan jadwal
    for i in range(12):
        angle = math.radians(i * 30 - 60)
        x = center_x + radius * 0.8 * math.cos(angle)
        y = center_y + radius * 0.8 * math.sin(angle)
        canvas.create_text(x, y, text=f"{i+1}\n{jadwal[i]}", font=("Arial", 10), fill="black")

    # Gambar jarum jam
    hour_angle = math.radians((hour % 12) * 30 + (minute / 60) * 30 - 90)
    minute_angle = math.radians(minute * 6 - 90)
    second_angle = math.radians(second * 6 - 90)

    hour_x = center_x + radius * 0.5 * math.cos(hour_angle)
    hour_y = center_y + radius * 0.5 * math.sin(hour_angle)
    canvas.create_line(center_x, center_y, hour_x, hour_y, width=6, fill="black")

    minute_x = center_x + radius * 0.7 * math.cos(minute_angle)
    minute_y = center_y + radius * 0.7 * math.sin(minute_angle)
    canvas.create_line(center_x, center_y, minute_x, minute_y, width=4, fill="blue")

    second_x = center_x + radius * 0.9 * math.cos(second_angle)
    second_y = center_y + radius * 0.9 * math.sin(second_angle)
    canvas.create_line(center_x, center_y, second_x, second_y, width=2, fill="red")

    # Update kanvas
    canvas.update()

# Fungsi untuk menjalankan jam
def run_clock():
    while True:
        current_time = time.localtime()
        hour = current_time.tm_hour
        minute = current_time.tm_min
        second = current_time.tm_sec
        draw_clock(clock_canvas, hour, minute, second)
        root.update()
        time.sleep(1)

# GUI menggunakan Tkinter
root = tk.Tk()
root.title("Jadwal Me Time Nama kamu")

title_label = tk.Label(root, text="Jadwal Me Time Nama kamu", font=("Helvetica", 20))
title_label.pack()

clock_canvas = Canvas(root, width=400, height=400)
clock_canvas.pack()

# Tombol untuk memulai jam
start_button = tk.Button(root, text="Play", command=run_clock)
start_button.pack()

# Menjalankan aplikasi Tkinter
root.mainloop()