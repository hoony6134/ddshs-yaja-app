import socket
import tkinter
import tkinter.ttk

def idset(event):
    global student_id
    student_id=idinput.get()

def tset(event):
    global teacher
    teacher=tinput.get()

def lset(event):
    global location
    location=linput.get()

def dateset(event):
    global date
    date=linput.get()

def teamset(event):
    global team
    team=[]
    temp=teaminput.get()
    team=temp.split(",")

timedrop=[
    "야자 1교시",
    "야자 2교시",
    "야자 전체",
    "방과후",
    "방과후 + 야자 전체"
]

window=tkinter.Tk()
window.title("대전동신과학고 야자이동 신청 시스템")
window.geometry("640x400+100+100")
window.resizable(True, True)
window.configure(bg='white')

timeopt=tkinter.StringVar(window)
timeopt.set("옵션을 선택해 주세요.")

addr = ('<broadcast>', 33333)                              # broadcast address

UDPSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Create socket
UDPSock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

# Tkinter Title ~ ip address
titlelabel = tkinter.Label(window, text="대전동신과학고 야자이동 신청 시스템", font=("Nanum Gothic", 20), fg="green")
titlelabel.grid(row=0, column=0)

info=tkinter.Label(window, text="v.1.0 Beta").grid(row=1, column=0)
info2=tkinter.Label(window, text="Developed by Cyan").grid(row=1, column=1)

ipaddrtext=tkinter.Label(window, text="현재 IP주소:").grid(row=2, column=0)
ipaddr=tkinter.Label(window, text=socket.gethostbyname(socket.gethostname())).grid(row=2, column=1)

idlabel=tkinter.Label(window, text="학번").grid(row=3, column=0)
idinput=tkinter.Entry(window)
idinput.bind("<Motion>", idset)
idinput.grid(row=3, column=1)

datelabel=tkinter.Label(window, text="날짜").grid(row=4, column=0)
dateinput=tkinter.Entry(window)
dateinput.bind("<Motion>", dateset)
dateinput.grid(row=4, column=1)
teamplabel=tkinter.Label(window, text="MM/DD 형식으로 작성").grid(row=4, column=2)

teacherlabel=tkinter.Label(window, text="지도교사 선생님").grid(row=5, column=0)
tinput=tkinter.Entry(window)
tinput.bind("<Motion>", tset)
tinput.grid(row=5, column=1)

locationlabel=tkinter.Label(window, text="신청 장소").grid(row=6, column=0)
linput=tkinter.Entry(window)
linput.bind("<Motion>", lset)
linput.grid(row=6, column=1)

timelabel=tkinter.Label(window, text="신청 시간대").grid(row=7, column=0)
opt1 = tkinter.OptionMenu(window, timeopt, *timedrop)
opt1.config(width=12, font=('Helvetica', 12))
opt1.grid(row=7, column=1)

# debuglabel1=tkinter.Label(window, text=timeopt)
# debuglabel1.grid(row=3, column=2)
def timecallback(*args):
    global time
    # debuglabel1.configure(text=timeopt.get())
    time = timeopt.get()
    print(time)

timeopt.trace("w", timecallback)

teamlabel=tkinter.Label(window, text="추가 팀원").grid(row=8, column=0)
teaminput=tkinter.Entry(window)
teaminput.bind("<Motion>", teamset)
teaminput.grid(row=8, column=1)
teamplabel=tkinter.Label(window, text="쉼표로 구분, 없으면 '없음' 기재").grid(row=8, column=2)

def senddata():
    print('전송 서버 연결됨')
    tempdata="student_id:"+student_id, "date:"+date, "teacher:"+teacher, "location:"+location, "team_members:",team
    data = str(tempdata)
    if UDPSock.sendto(data.encode(), addr):
        print("야자 이동 신청 정보 전송중.." % data)
        messagebox.showinfo("야자 이동 신청 완료", "야자 이동 신청이 완료되었습니다.")

sendbutton = tkinter.Button(window, text="신청하기", overrelief="solid", width=10, command=senddata, repeatdelay=1000, repeatinterval=100)
sendbutton.grid(row=9,column=0)

window.mainloop()


UDPSock.close()             # Close socket
print('야자이동 신청 완료')