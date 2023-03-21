# speech
import speech_recognition as sr
from gtts import gTTS
import playsound

# tkinter
import tkinter
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


df = pd.read_csv('./G369Thinh_EPLStats/EPLStats.csv')
print('Độ lớn của bảng: ', df.shape)
print(df[0:5])
