from tkinter import *


root = Tk()

def printName():
    print(ent_1.get())#get: copia a entrada do usuário
    lab_2['text'] = 'Analisando...'

root.title('Bem vindo ao Programa!')
root.configure(background='#696969')
#LxA+E+T
#600x450+370+200
root.geometry('600x450+370+200')

lab_1 = Label(root,text='Informe o Alvo:',bg='#696969', font=('arial', 12))
lab_2 = Label(root,text='',bg='#696969')
ent_1 = Entry(root,width='16') #width: regula a resolução
Cap1 = PhotoImage(file='Cap1.GIF',)
rot_1= Label(root, image=Cap1,bg='#696969')

lab_1.place(x=248, y=255)
lab_2.place(x=350, y=280)
ent_1.place(x=250, y=279)
rot_1.place(x=175, y=1)

but_1 = Button(root,width='13', text='Start',bg='#696969', command=printName)
but_1.place(x=250, y=300)

#lab_1.grid(row=1, column=0, padx=250, pady=0)
#lab_2.grid(row=2, column=3, padx=250, pady=1)
#ent_1.grid(row=2, column=0, padx=250, pady=0)

#but_1 = Button(root,width='13', text='Start',bg='#696969', command=printName)
#but_1.grid(row=3, column=0, padx=250, pady=1)

root.mainloop()


















