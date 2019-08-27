from tkinter import *
from tkinter import messagebox
import pickle

class gui(Frame):
    def __init__(self,root):
        self.count = 0
        lbl1 = Label(text = "이름")
        lbl1.grid(row = 0, column = 0)
        self.entry1 = Entry()#입력창1, 이름
        self.entry1.grid(row=0, column = 2)
        lbl2 = Label(text = "전화번호")
        lbl2.grid(row=10, column = 0)
        self.entry2 = Entry()#입력창2, 전화번호
        lbl3 = Label(text = "이메일")
        lbl3.grid(row = 13, column = 0)
        self.entry2.grid(row = 10, column = 2)
        self.entry3 = Entry()#입력창3, 이메일
        self.entry3.grid(row = 13, column = 2)
        button1 = Button(text = "입력", command = self.click)#입력창의 값을 받음(click함수)
        button1.grid(row = 15, column = 0)
        button2 = Button(text = "이전 데이터 출력", command = self.outputPre)
        button2.grid(row = 15,column = 2)
        button3 = Button(text = "현재 데이터 출력", command = self.output)
        button3.grid(row = 15, column = 4)
        button4 = Button(text = "다음 데이터 출력", command = self.outputNext)
        button4.grid(row = 15, column = 6)

 

        self.lblName = Label()

        self.lblName.grid(row = 20, column = 0)

        self.lblNo = Label()

        self.lblNo.grid(row = 25, column = 0)

        self.lblMail = Label()

        self.lblMail.grid(row = 30, column = 0)

        

    #     #계산기

    #     lblC = Label(text = "계산기")

    #     lblC.grid(row = 30, column = 0)

    #     lbl3 = Label(text = "입력창1")#입력창 1

    #     lbl3.grid(row = 33, column = 0)

    #     self.entry3 = Entry()

    #     self.entry3.grid(row = 33, column = 3)

    #     lbl4 = Label(text = "입력창2")#입력창 2

    #     lbl4.grid(row = 35, column = 0)

    #     self.entry4 = Entry()

    #     self.entry4.grid(row = 35, column = 3)

    #     buttonP = Button(text = "더하기", command = self.plus)

    #     buttonP.grid(row = 37, column = 0)

    #     buttonM = Button(text = "빼기", command = self.minus)

    #     buttonM.grid(row = 37, column = 3)

    #     buttonG = Button(text = "곱하기", command = self.multiple)

    #     buttonG.grid(row = 37, column = 5)

 

    # def plus(self):#더하기

    #     data1 = self.entry3.get()

    #     data2 = self.entry4.get()

    #     res = int(data1) + int(data2)

    #     lbl = Label(text = res)

    #     lbl.grid(row = 40, column = 0)

    

    # def minus(self):#빼기

    #     data1 = self.entry3.get()

    #     data2 = self.entry4.get()

    #     res = int(data1) - int(data2)

    #     lbl = Label(text = res)

    #     lbl.grid(row = 40, column = 0)

    

    # def multiple(self):#곱하기

    #     data1 = self.entry3.get()

    #     data2 = self.entry4.get()

    #     res = int(data1) * int(data2)

    #     lbl = Label(text = res)

    #     lbl.grid(row = 40, column = 0)

        

 

 

 

    def click(self):#입력창의 값을 받는 함수

        name = self.entry1.get()

        number = self.entry2.get()

        mail = self.entry3.get()

        dic = {"name":name, "number":number, "mail":mail}

        s = []

 

        try:

            with open("a.txt",'rb') as f:

                s = pickle.load(f)#기존 데이터 불러옴

            with open("a.txt",'wb') as f:

                s.append(dic)#리스트에 추가

                pickle.dump(s,f)#파일에 저장

        except EOFError:#파일에서 읽어 올 데이터가 없을 때 일어나는 오류

 

            with open("a.txt",'wb') as f:

                s.append(dic)

                pickle.dump(s,f)

        

        except FileNotFoundError:

            with open("a.txt","wb") as f:

                s.append(dic)

                pickle.dump(s,f)

        

        lbl = Label(text = "입력 완료")

        lbl.grid(row = 16, column = 0)

 

    def outputPre(self):#이전 데이터 출력

        if self.count == 0:

            messagebox.showerror(message = "data is not exist")

        else:

            try:

                with open("a.txt",'rb') as f:

                    s = pickle.load(f)

            except EOFError:

                messagebox.showerror(message="data is not exist")

            

            self.lblName.destroy()

            self.lblNo.destroy()

            self.lblMail.destroy()

            self.count = self.count - 1

            data = s[self.count]

            self.lblName = Label(text = data['name'])

            self.lblName.grid(row = 20, column = 0)

            self.lblNo = Label(text = data['number'])

            self.lblNo.grid(row = 25, column = 0)

            self.lblMail = Label(text = data['mail'])

            self.lblMail.grid(row = 30, column = 0)

    

    def output(self):#현재 데이터 출력

        try:

            with open("a.txt",'rb') as f:

                s = pickle.load(f)

        except EOFError:

            messagebox.showerror(message="data is not exist")

 

        self.lblName.destroy()

        self.lblNo.destroy()

        self.lblMail.destroy()

        data = s[self.count]

        self.lblName = Label(text = data['name'])

        self.lblName.grid(row = 20, column = 0)

        self.lblNo = Label(text = data['number'])

        self.lblNo.grid(row = 25, column = 0)

        self.lblMail = Label(text = data['mail'])

        self.lblMail.grid(row = 30, column = 0)

        

 

    def outputNext(self):#다음 데이터 출력

        try:
            with open("a.txt", 'rb') as f:
                s = pickle.load(f)

                try:
                    self.lblName.destroy()

                    self.lblNo.destroy()

                    self.lblMail.destroy()

                    self.count = self.count + 1

                    data = s[self.count]

                    self.lblName = Label(text = data['name'])

                    self.lblName.grid(row = 20, column = 0)

                    self.lblNo = Label(text = data['number'])

                    self.lblNo.grid(row = 25, column = 0)

                    self.lblMail = Label(text = data['mail'])

                    self.lblMail.grid(row = 30, column = 0)

 

 

                except IndexError:
                    messagebox.showerror(message="data is not exist")
                    self.count = self.count - 1

 

        except EOFError:

            messagebox.showerror(message="data is not exist")

        

 

 

def main():

    root = Tk()

    frame = gui(root)

    root.mainloop()

 

if __name__ == "__main__":

    main()


