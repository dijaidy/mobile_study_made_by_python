import tkinter as tk
import json as js

window=tk.Tk()
window.title("YUN DAE HEE")
window.geometry("400x800+100+100")
window.resizable(False, False)

frame=tk.Frame(window)

scrollbar=tk.Scrollbar(frame)
scrollbar.pack(side="right", fill="y")
with open("information\chosen_book_file.json", "r", encoding="UTF-8") as out_file:
            dictionary = js.load(out_file)

listbox=tk.Listbox(frame, yscrollcommand = scrollbar.set)
for line in range(1,1001):
   listbox.insert(line, str(line) + str(dictionary) + "/1000")
listbox.pack(side="left")

scrollbar["command"]=listbox.yview

frame.pack()

window.mainloop()