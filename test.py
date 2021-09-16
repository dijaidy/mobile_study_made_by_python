from tkinter import *

window=Tk()
window.title("YUN DAE HEE")
window.geometry("400x800+100+100")

listbow=Listbox(window, selectmode="extended", height=0)
listbow.insert(0, "사과")
listbow.insert(1, "딸기")
listbow.insert(2, '바나나')
listbow.pack()

btn=Button(window, text="click", command=lambda: print("선택된 항목:", listbow.curselection()))
btn.pack()

window.mainloop()