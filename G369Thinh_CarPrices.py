# speech
import speech_recognition as sr
from gtts import gTTS
import playsound

# tkinter
import tkinter as tk
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
thinh69_FILE = "thinh69.mp3"  # lưu tên file input
thinh69_DIR = 'thinh69'      # thư mục lưu các file [trên]
os.makedirs(thinh69_DIR, exist_ok=True)  # tạo thư mục lưu

# Các hàm thực hiện chức năng hệ thống


def Thoat():
    traloi = messagebox.askquestion(
        "Xác nhận", "Bạn có muốn thoát hay không (Y/N)?")
    if traloi == "yes":
        wn.destroy()


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
        vText.save(thinh69_DIR)
        lbSpeech.config(text=vlenh)
        lbSpeech.update()
        playsound.playsound(thinh69_FILE)


# B3: Lập GUI
# Tạo một cửa sổ mới
wn = tk.Tk()
# Thêm tiêu đề cho cửa sổ
wn.title("69 Nguyễn Khang Thịnh, 211103C, Đồ Án Học Phần: Lập trình Python, T8.2023")
# Đặt kích thước cho cửa sổ
wn.geometry('800x600')
# Không cho thay đổi size
wn.resizable(tk.FALSE, tk.FALSE)

# Tiêu đề form = Lập trình Python phân tích dữ liệu các đội bóng Ngoại hạng Anh mùa 06/07 đến mùa 17/18
t = "69 Nguyễn Khang Thịnh, 211103C, Đồ Án Học Phần: Lập trình Python: EDA Car Prices"
lblDT = tk.Label(wn, text=t, background="yellow", fg="blue", relief=tk.SUNKEN, font=(
    "Arial Bold", 13), borderwidth=3, width=70, height=3)
lblDT.place(x=10, y=10)

# Các nút lệnh
# Thoát
btnThoat = tk.Button(wn, text="Thoát", width=10, height=5, command=Thoat)
btnThoat.place(x=100, y=135)
# Xử lý lời nói
btnNoi = tk.Button(wn, text="Trợ Lý Ảo", width=15, height=5, command=Lenh)
btnNoi.place(x=200, y=135)

lbSpeech = tk.Label(wn, text='', relief=tk.SUNKEN,
                    borderwidth=2, width=80, height=3)
lbSpeech.place(x=10, y=250)

# Lặp vô tận để hiển thị cửa sổ
wn.mainloop()
