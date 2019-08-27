
#Book 클래스 : 제목, 저자, 출판사  끝

#Book_rental 클래스 : book 클래스를 상속받아서 일련번호, 대출인

#Book_rental_list 객체에 book_rental 객체를 리스트 형태로 저장

#tkinter를 이용하여 새로운 book_rental 객체를 book_rental_list에 추가할 수 있도록 구현

#tkinter를 이용하여 처음, 다음, 이전, 마지막으로 book_rental_list를 탐색할 수 있도록 구현

#menu에는 파일>(열기,저장하기, 종료) 구현끝

#menu>파일>열기를 통해 book_rental_list 객체를 파일에서 불러올 수 있도록 구현끝

#menu>파일>저장을 통해 book_rental_list 객체를 자신이 원하는 이름의 파일로 저장할 수 있도록 구현 구현 끝

#menu>파일>종료를 통해 프로그램 종료되도록 구현 구현 끝

#주석처리 및 코드 가독성


from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename, asksaveasfile
book_rental_list = []



import pickle

class Book():
    bookname = "어린왕자"
    bookwriter = "앙투안"
    bookPublisher = "출판사"

class Book_rental(Book):
    name = "김철수"
    no = "123412"

root = Tk()
menubar=Menu(root)
count = 0
a = ""

def OpenFile():#파일 열기
    global count
    global a
    name = askopenfilename(
                        filetypes =(("Text File", "*.txt"),("All Files","*.*")),
                        title = "Choose a file."
                        )
    print (name)

    UseFile = open(name, 'rb')
    a = pickle.load(UseFile)
    btn1 = Button(root, text = "앞 데이터", command = preD)
    btn1.grid(row = 6, column = 0)
    btn2 = Button(root, text = "현재 데이터", command = D)
    btn2.grid(row = 6, column = 5)
    btn3 = Button(root, text = "다음 데이터", command = nexD)
    btn3.grid(row = 6, column = 10)
    lbl1 = Label(root, text = a[count])
    lbl1.grid(row = 4, column = 0)

def preD():
    global a
    global count
    if count == 0:
        messagebox.showerror(root, "데이터 없음")
    else:   
        count = count-1
        lbl = Label(root, a[count])
        lbl.grid(row = 10, column = 0)

def D():
    global a
    global count 
    lbl = Label(root, a[count])
    lbl.grid(row = 10, column = 0)

def nexD():
    global a
    global count
    count = count+1
    lbl = Label(root, a[count])
    lbl.grid(row = 10, column = 0)

def file_save(): #파일 저장
    global book_rental_list
    f = asksaveasfile(mode='wb', defaultextension=".txt") 
    if f is None: # asksaveasfile return `None` if dialog closed with "cancel". 
     return 
    # text2save = str(text.get(1.0, END)) # starts from `1.0`, not `0.0` 
    pickle.dump(book_rental_list,f) 
    f.close() # `()` was missing. 

def quit():#종료
    root.quit()

a = Book_rental()
book_rental_list.append({"bookname":a.bookname, "writer":a.bookwriter, "출판사":a.bookPublisher, "빌린이":a.name, "일련번호":a.no})
menu_1=Menu(menubar, tearoff=0)#메뉴바
menu_1.add_command(label="열기", command = OpenFile)#열기
menu_1.add_command(label="저장하기", command = file_save)#저장하기
menu_1.add_separator()#칸 분류
menu_1.add_command(label="종료", command = quit)#종료
menubar.add_cascade(label="메뉴", menu=menu_1)

root.config(menu=menubar)

root.mainloop()

print("Window Close")