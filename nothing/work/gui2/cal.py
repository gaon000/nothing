from tkinter import *

class calc(Frame):
    def __init__(self, root):

        #숫자 입력란 만들기
        self.ent=Entry()
        self.ent.insert(0, ' ')
        self.ent.pack(pady=5)
        #숫자 버튼 만들기
        buttons = ['7410', '852=', '963+', 'C/*-']
        for col in buttons:
            frm=Frame()
            frm.pack(side=LEFT)
            for row in col :
                btn=Button(frm, text=row, command=(lambda char=row: self.enter(char)))
                btn.pack(fill=X, padx=5, pady=5)

    #이벤트 처리함수
    def enter(self , btn):
        if btn == 'C':
            self.ent.delete(0, END)
        elif btn == '=':
            ans = eval(self.ent.get())
            self.ent.delete(0, END)
            self.ent.insert(0, ans)
        else:
            self.ent.insert(END, btn)









def main():

    root = Tk()

    frame = calc(root)

    root.mainloop()

 

if __name__ == "__main__":

    main()