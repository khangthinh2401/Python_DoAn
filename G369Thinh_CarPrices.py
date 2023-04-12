# speech
import speech_recognition as sr
from gtts import gTTS
import playsound

# tkinter
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# thư viện os
import os

# thư viện cần thiết EDA
import numpy as np  # thư viện về đại số tuyến tính
import pandas as pd  # thư viện xử lý dữ liệu
from scipy import stats  # thư viện cung cấp công cụ thống kê
from sklearn import preprocessing  # thư viện tiền xử lý dữ liệu
# Thư viện phân tích dữ liệu thăm dò
from sklearn.feature_selection import SelectKBest, chi2

# B2: Khai báo tên thư mục & File lưu thông tin bài làm
thinh69_FILE = os.path.abspath('') + '\\' + 'thinh69.mp3'  # lưu tên file input

# Các hàm thực hiện chức năng hệ thống


def Thoat():
    traloi = messagebox.askquestion(
        "Xác nhận", "Bạn có muốn thoát hay không (Y/N)?")
    if traloi == "yes":
        root.destroy()


# Các hàm thực hiện chức năng Speech

def Lenh():
    r = sr.Recognizer()
    with sr.Microphone() as Source:
        messagebox.showinfo("Nhắc nhở", "Hiệu chỉnh nhiễu trước khi nói!")
        r.adjust_for_ambient_noise(Source, duration=1)
        messagebox.showinfo(
            "Sẵn sàng", "Bấm OK để bắt đầu nói tiếng Việt trong 3 giây")
        audio_data = r.record(Source, duration=3)
        try:
            vlenh = r.recognize_google(audio_data, language="vi")
        except:
            vlenh = "Tôi không nghe rõ!"
        vText = gTTS(text=vlenh, lang='vi')
        vText.save(thinh69_FILE)
        lblBody.config(text=vlenh)
        lblBody.update()
        playsound.playsound(thinh69_FILE)


def EDA():
    # df = pd.read_csv('./G369Thinh_CarPrices/CarPrices.csv')
    # print(df.count().sort_values())
    pass


# B3: Lập GUI
# Tạo một cửa sổ mới
root = tk.Tk()
root.title(
    "69 Nguyễn Khang Thịnh, 211103C, Đồ Án Học Phần: Lập trình Python, T8.2023")
root.geometry('1200x800')
root.pack_propagate()
root.resizable(tk.FALSE, tk.FALSE)

# tạo frames
mainFrame = tk.Frame(root, width=1200, height=800, background='#a2d7de')
mainFrame.columnconfigure(0, weight=1)
mainFrame.columnconfigure(1, weight=1)
mainFrame.columnconfigure(2, weight=1)
mainFrame.pack()

# Tiêu đề form
t = "69 Nguyễn Khang Thịnh, 211103C, Đồ Án Học Phần: Lập trình Python: EDA Car Prices"
lblDT = tk.Label(mainFrame, text=t, background="yellow", fg="blue", relief=tk.SUNKEN, font=(
    "Arial Bold", 13), borderwidth=3, height=3, width=120)
lblDT.grid(row=0, column=0, columnspan=3, padx=5, pady=5)

# Các nút lệnh
btnThoat = tk.Button(mainFrame, text="Thoát",
                     width=15, height=3, command=Thoat)
btnThoat.grid(row=1, column=0)
btnNoi = tk.Button(mainFrame, text="Trợ Lý Ảo",
                   width=15, height=3, command=Lenh)
btnNoi.grid(row=1, column=1)
btnEDA = tk.Button(mainFrame, text="EDA",
                   width=15, height=3, command=EDA)
btnEDA.grid(row=1, column=2)

# Label hiển thị nội dung
lblBody = tk.Label(mainFrame, text='', relief=tk.SUNKEN,
                   borderwidth=3, width=150, height=35)
lblBody.grid(row=2, columnspan=3, padx=5, pady=10)

# Lặp vô tận để hiển thị cửa sổ
root.mainloop()
