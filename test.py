from tkinter import *


class 메인(Tk):
    def __init__(self):
        self._frame = None
        # 창 설정
        self.window = Tk()
        self.window.title("메인")
        self.window.geometry("400x800")

        self.button1 = Button(self.window, text="프레임 버튼", command=self.show_frame)
        self.button1.pack()

        self.window.mainloop()

    def switch_frame(self, frame_class):

        new_frame = frame_class(self.window)
        if self._frame != new_frame:
            if self._frame is not None:
                self._frame.destroy()
            self._frame = new_frame
            self._frame.pack()

    def show_frame(self):
        self.switch_frame(프레임)


class 프레임(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        Label(self, text="안녕").pack()


메인()

# 테스트
