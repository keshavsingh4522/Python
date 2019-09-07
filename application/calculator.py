from tkinter import *
root=Tk()
s=StringVar()
def disp(x):
    global text
    text+=x
    s.set(text)
def equal():
    global text
    text=''
    try:
        text=eval(s.get())
    except Exception as e:
        s.set(e)
        text=''
    else:
        s.set(text)
        text=''
text=''
# root.geometry("300x300")
root.config(bg="purple")
color=['#12ff3f','#12ff67','#67ff67','#11deaf']
e=Entry(root,textvariable=s)
e.pack(side=TOP,expand='yes',fill='both')
for i in ['789/','456*','123+','.0-=']:
    f=Frame(root,bg=color.pop())
    for j in i:
        b=Button(f,text=j,command=lambda x=j:disp(x) if x!='=' else equal())
        b.pack(side='left',padx=10,pady=10,expand="yes",fill='both')
    f.pack(side='top',padx=10,pady=10,expand="yes",fill='both')
b=Button(root,text="Exit",command=root.destroy)
b.pack(side="bottom")
root.mainloop()
