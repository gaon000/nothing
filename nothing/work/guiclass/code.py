from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
class gui():
    def __init__(self):
        self.root = Tk(  )
        self. data = []
        Title = self.root.title( "File Opener")

        btn = Button(self.root, text = "파일선택", command = self.OpenFile) #파일 선택
        btn.pack()

    def OpenFile(self):#파일 열기
        name = askopenfilename(
                            filetypes =(("Text File", "*.txt"),("All Files","*.*")),
                            title = "Choose a file."
                            )
        print (name)

        UseFile = open(name, 'r')
        for i in UseFile.readlines():
            self.data.append(int(i))
        self.selectWindow()

    def classStats(self):#학급별 통계창
        toplevel = Toplevel(self.root)
        toplevel.geometry()
        btn1 = Button(toplevel, text = "1반", command = lambda: self.eachClass(1))
        btn1.pack()
        btn2 = Button(toplevel, text = "2반", command = lambda: self.eachClass(2))
        btn2.pack()
        btn3 = Button(toplevel, text = "3반", command = lambda: self.eachClass(3))
        btn3.pack()
        btn4 = Button(toplevel, text = "4반", command = lambda: self.eachClass(4))
        btn4.pack()

    def ascend(self):#오름차순
        c = 1
        for i in sorted(self.a):
            lbl = Label(self.toplevel, text = int(i))
            lbl.grid(row = 10, column = c)
            c = c+1

    def descend(self):#내림차순
        c = 1
        for i in sorted(self.a,reverse = True):
            lbl = Label(self.toplevel, text = int(i))
            lbl.grid(row = 15, column = c)
            c = c+1
    def avg(self):#평균
        lbl = Label(self.toplevel, text = int(sum(self.a)/len(self.a)))
        lbl.grid(row = 20, column = 5)

    def maxmin(self):#최고, 최저
        lbl = Label(self.toplevel, text = "%d %d"%(max(self.a),min(self.a)))
        lbl.grid(row = 25, column = 5)

    def eachClass(self,a):
        self.toplevel = Toplevel(self.root)
        self.toplevel.geometry()
        lbl1 = Label(self.toplevel, text = "%d반"%a)
        lbl1.grid()
        self.data
        c = 1
        for i in range(1,21):
            lbl = Label(self.toplevel, text = i)
            lbl.grid(row = 3, column = c)
            c=c+1
        c = 1
        if a == 1:
            self.a = self.data[:20]
            for i in self.a:
                lbl2 = Label(self.toplevel, text = "%d"%i)
                lbl2.grid(row = 5, column = c)
                c=c+1

        elif a == 2:
            self.a = self.data[20:40]
            for i in self.a:
                lbl2 = Label(self.toplevel, text = "%d"%i)
                lbl2.grid(row = 5, column = c)
                c=c+1

        elif a == 3:
            self.a = self.data[40:60]
            for i in self.a:
                lbl2 = Label(self.toplevel, text = "%d"%i)
                lbl2.grid(row = 5, column = c)
                c=c+1

        elif a == 4:
            self.a = self.data[60:80]
            for i in self.a:
                lbl2 = Label(self.toplevel, text = "%d"%i)
                lbl2.grid(row = 5, column = c)
                c=c+1

        btnAsc = Button(self.toplevel, text = "오름차순", command = self.ascend)#오름차순 버튼
        btnDes = Button(self.toplevel, text = "내림차순", command = self.descend)#내림차순 버튼
        btnAvg = Button(self.toplevel, text = "평균", command = self.avg)#평균 버튼
        btnMm = Button(self.toplevel, text = "최고점과 최저점", command = self.maxmin)#최고, 최저점 버튼
        btnAsc.grid(row = 10, column = 0)
        btnDes.grid(row = 15, column = 0)
        btnAvg.grid(row = 20, column = 0)
        btnMm.grid(row = 25, column = 0)



    def totStats(self):#전체 통계창
        x = 0#0보다 크거나 같고 20보다 작은 점수 득점자
        y = 0#20보다 크거나 같고 40보다 작은 점수 득점자
        z = 0#40보다 크거나 같고 60보다 작은 점수 득점자
        s = 0#60보다 크거나 같고 80보다 작은 점수 득점자
        v = 0#80보다 크거나 같고 100보다 작거나 같은 점수 득점자
        for i in self.data:
            if i <20:
                x = x+1
            elif i < 40:
                y = y+1
            elif i <60:
                z = z+1
            elif i < 80:
                s = s+1
            elif i<=100:
                v = v+1
        
        c = 1
        toplevel = Toplevel(self.root)
        toplevel.geometry()
        lblTot = Label(toplevel, text = "전체 통계창")
        lblTot.grid(row = 0, column = 0)
        
        lblX = Label(toplevel, text = "0보다 크거나 같고 20보다 작은 점수 득점자 수: %d"%x)
        lblX.grid(row = 5, column = 35)
        lblY = Label(toplevel, text = "20보다 크거나 같고 40보다 작은 점수 득점자 수: %d"%y)
        lblY.grid(row = 7, column = 35)
        lblZ = Label(toplevel, text = "40보다 크거나 같고 60보다 작은 점수 득점자 수: %d"%z)
        lblZ.grid(row = 9, column = 35)
        lblS = Label(toplevel, text = "60보다 크거나 같고 80보다 작은 점수 득점자 수: %d"%s)
        lblS.grid(row = 11, column = 35)
        lblV = Label(toplevel, text = "80보다 크거나 같고 100보다 작거나 같은 득점자 수: %d"%v)
        lblV.grid(row = 13, column = 35)
        lblAVG = Label(toplevel, text = "평균: %d"%int(sum(self.data)/len(self.data)))
        lblAVG.grid(row = 15, column = 35)
        lblMM = Label(toplevel, text = "최대값, 최솟값: %d %d"%(max(self.data),min(self.data)))
        lblMM.grid(row = 17, column = 35)

        for i in range(1,21):
            lbl = Label(toplevel, text = i)
            lbl.grid(row = 3, column = c)
            c=c+1
            
        lbl1 = Label(toplevel, text = "1반")
        lbl1.grid(row = 5, column = 0)
        c = 1
        for i in self.data[:20]:
            lbl = Label(toplevel, text = i)
            lbl.grid(row = 5, column = c)
            c = c+1

        lbl2 = Label(toplevel, text = "2반")
        lbl2.grid(row = 7, column = 0)
        c= 1
        for i in self.data[20:40]:
            lbl = Label(toplevel, text = i)
            lbl.grid(row = 7, column = c)
            c = c+1
        
        lbl3 = Label(toplevel, text = "3반")
        lbl3.grid(row = 9, column = 0)
        c = 1
        for i in self.data[40:60]:
            lbl = Label(toplevel, text = i)
            lbl.grid(row = 9, column = c)
            c = c+1

        lbl4 = Label(toplevel, text = "4반")
        lbl4.grid(row = 11, column = 0)
        c = 1
        for i in self.data[60:]:
            lbl = Label(toplevel, text = i)
            lbl.grid(row = 11, column = c)
            c = c+1


    def selectWindow(self):#통계 고르는 창
        toplevel = Toplevel(self.root)
        toplevel.geometry()
        btn1 = Button(toplevel, text = "학급별 통계", command = self.classStats)
        btn1.pack()
        btn2 = Button(toplevel, text = "전체통계", command = self.totStats)
        btn2.pack()




a = gui()
a.root.mainloop()