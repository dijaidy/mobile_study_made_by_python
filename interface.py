from tkinter import *

window = Tk()

window.title("MOBILE_STUDY")
window.geometry("400x800")

title_font = ("배달의민족 주아", 30)
label = Label(window, text="MOBILE\nSTUDY", font=title_font)
label.place(relx=0, relwidth=1, rely=0, height=150)


window.resizable(width=False, height=False)
window.mainloop()
