from tkinter import *
from functools import partial
from sqlalchemy import true

w = Tk()

w.geometry("750x600")
w.title("Genshin Impact - Cálculo de dano")

#caixas de entrada:
baseAtq = Entry(w, width=20, font=("Times New Roman", 13))
baseAtq.place(relx=0.7, rely=0.02, anchor=NW)

atq = Entry(w, width=20, font=("Times New Roman", 13))
atq.place(relx=0.7, rely=0.09, anchor=NW)

flatAtq = Entry(w, width=20, font=("Times New Roman", 13))
flatAtq.place(relx=0.7, rely=0.16, anchor=NW)

bonusDmg = Entry(w, width=20, font=("Times New Roman", 13))
bonusDmg.place(relx=0.7, rely=0.23, anchor=NW)

skill = Entry(w, width=20, font=("Times New Roman",13))
skill.place(relx=0.7, rely=0.3, anchor=NW)

charLvl = Entry(w, width=20, font=("Times New Roman", 13))
charLvl.place(relx=0.7, rely=0.37, anchor=NW)

enemyLvl = Entry(w, width=20, font=("Times New Roman", 13))
enemyLvl.place(relx=0.7, rely=0.44, anchor=NW)

defenseDrop = Entry(w, width=20, font=("Times New Roman", 13))
defenseDrop.place(relx=0.7, rely=0.51, anchor=NW)

resistence = Entry(w, width=20, font=("Times New Roman", 13))
resistence.place(relx=0.7, rely=0.58, anchor=NW)

critDmg = Entry(w, width=20, font=("Times New Roman", 13))
critDmg.place(relx=0.7, rely=0.65, anchor=NW)

critRate = Entry(w, width=20, font=("Times New Roman", 13))
critRate.place(relx=0.7, rely=0.72, anchor=NW)

#texto:
t1 = Label(w, text="Ataque Base (arma + personagem):", font=("Times New Roman",13), bg='#5CE36A')
t1.place(relx=0.68, rely=0.02, anchor=NE)

t2 = Label(w, text="Valor % de atq (em arma + artefatos, ex: 46.6 (não incluir %)):", font=("Times New Roman",13),bg='#5CE36A')
t2.place(relx=0.68, rely=0.09, anchor=NE)

t3 = Label(w, text="Flat ataque (artefatos):", font=("Times New Roman",13),bg='#5CE36A')
t3.place(relx=0.68, rely=0.16, anchor=NE)

t4 = Label(w, text="Valor % de bonus damage (ex: 61.4 (não incluir %)):", font=("Times New Roman",13),bg='#5CE36A')
t4.place(relx=0.68, rely=0.23, anchor=NE)

t5 = Label(w, text="Multiplicador da skill (ex: 312.4 (não incluir %)):", font=("Times New Roman",13),bg='#5CE36A')
t5.place(relx=0.68, rely=0.3, anchor=NE)

t6 = Label(w, text="Level do seu personagem:", font=("Times New Roman",13),bg='#5CE36A')
t6.place(relx=0.68, rely=0.37, anchor=NE)

t7 = Label(w, text="Level do inimigo:", font=("Times New Roman",13),bg='#5CE36A')
t7.place(relx=0.68, rely=0.44, anchor=NE)

t8 = Label(w, text="Defesa reduzida no inimigo (se não tiver reduzido digite 0):", font=("Times New Roman",13),bg='#5CE36A')
t8.place(relx=0.68, rely=0.51, anchor=NE)

t9 = Label(w, text="Resistência do inimigo (ex: 20 (não incluir %)):", font=("Times New Roman",13),bg='#5CE36A')
t9.place(relx=0.68, rely=0.58, anchor=NE)

t13 = Label(w, text="Dano crítico do personagem (ex: 170 (não incluir %)):", font=("Times New Roman",13),bg='#5CE36A')
t13.place(relx=0.68, rely=0.65, anchor=NE)

t11 = Label(w, text="Taxa crítica do personagem (ex: 50 (não incluir %)):", font=("Times New Roman",13),bg='#5CE36A')
t11.place(relx=0.68, rely=0.72, anchor=NE)

def calcularDano(evento):
    noCritDmg = (float(baseAtq.get())*(1 + float(atq.get())/100)+ float(flatAtq.get()))*(1 + float(bonusDmg.get())/100)* (float(skill.get())/100)* ((100 + float(charLvl.get()))/((100 + float(charLvl.get()))+(100+float(enemyLvl.get()))*(1 - float(defenseDrop.get())/100)))* (1 - float(resistence.get())/100)
    CritDmg = (float(baseAtq.get())*(1 + float(atq.get())/100)+ float(flatAtq.get()))*(1 + float(bonusDmg.get())/100)* (float(skill.get())/100)* ((100 + float(charLvl.get()))/((100 + float(charLvl.get()))+(100+float(enemyLvl.get()))*(1 - float(defenseDrop.get())/100)))* (1 - float(resistence.get())/100)* (1+float(critDmg.get())/100)
    media_ponderada = (noCritDmg*(100 - float(critRate.get())) + CritDmg* (float(critRate.get())))/100
    margCrit = CritDmg/100
    margNoCrit = noCritDmg/100
    d1['state'] = 'normal'
    d2['state'] = 'normal'
    d3['state'] = 'normal'
    margErro['state'] = 'normal'
    margErroCrit['state'] = 'normal'
    d1.delete(0,END)
    d2.delete(0,END)
    d3.delete(0,END)
    margErro.delete(0,END)
    margErroCrit.delete(0,END)
    d1.insert(0, round(noCritDmg,2))
    d2.insert(0, round(CritDmg,2))
    d3.insert(0, round(media_ponderada,2))
    margErro.insert(0, round(margNoCrit,2))
    margErroCrit.insert(0, round(margCrit,2))
    d1['state'] = 'disabled'
    d2['state'] = 'disabled'
    d3['state'] = 'disabled'
    margErro['state'] = 'disabled'
    margErroCrit['state'] = 'disabled'

#botão:
calculo = Button(w, text="Calcular Dano", font=("Times New Roman", 15), command= partial(calcularDano, ""))
calculo.place(relx=0.7, rely=0.79, anchor=CENTER)

#respostas:
#textos:
noCRITDMG = Label(w, text="Dano sem crítico:", font=('Times New Roman', 13),bg='#5CE36A')
noCRITDMG.place(relx=0.68, rely=0.84, anchor=NE)

critico = Label(w, text='Dano com crítico:', font=('Times New Roman', 13),bg='#5CE36A')
critico.place(relx=0.68, rely=0.88, anchor=NE)

media = Label(w, text='Média ponderada do Dano:', font=('Times New Roman', 13),bg='#5CE36A')
media.place(relx=0.68, rely= 0.92, anchor=NE)

erro = Label(w, text='Margem de Erro sem DanoCrit:', font=('Times New Roman',13),bg='#5CE36A')
erro.place(relx=0.16, rely=0.83, anchor=CENTER)

erroCrit = Label(w, text='Margem de Erro DanoCrit:', font=('Times New Roman',13),bg='#5CE36A')
erroCrit.place(relx=0.18, rely=0.93, anchor=CENTER)

#caixa de resposta:
d1 = Entry(w, width=20, font=('Times New Roman', 13), state="disabled")
d1.place(relx=0.7, rely=0.84, anchor=NW)

d2 = Entry(w, width=20, font=('Times New Roman', 13), state="disabled")
d2.place(relx=0.7, rely=0.88, anchor=NW)

d3 = Entry(w, width=20, font=('Times New Roman', 13), state="disabled")
d3.place(relx=0.7, rely=0.92, anchor=NW)

margErro = Entry(w, width=10, font=('Times New Roman', 13), state='disabled')
margErro.place(relx=0.37, rely=0.83, anchor=CENTER)

margErroCrit = Entry(w, width=10, font=('Times New Roman', 13), state='disabled')
margErroCrit.place(relx=0.37, rely=0.93, anchor=CENTER)

#pressionar Enter para executar o cálculo:
w.bind('<Return>',calcularDano)

#cor de fundo:
w.configure(bg='#5CE36A')

w.mainloop()