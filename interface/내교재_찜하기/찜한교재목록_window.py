from tkinter import *
import sys
import os
import json

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
sys.path.append(
    os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))))
)
from information_management.user_information import 찜한교재_manage_information

class 찜한교재목록_window:
    def __init__(self):
        # 창 설정
        self.window = Tk()
        self.window.title("찜한교재현황")
        self.window.geometry("400x800")
        self.window.resizable(False, False)
        frame=Frame(self.window)
        scrollbar=Scrollbar(frame)
        scrollbar.pack(self="right", fill="y")