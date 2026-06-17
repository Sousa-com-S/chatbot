import bot
from tkinter import *
from tkinter.ttk import *

from bot import saudacoes

main_window = Tk()

main_window.title("eduardo adora lopunnys")

main_window.geometry("300x300")

frame = Frame(main_window)
frame.grid()

main_window.grid()

l_indentify = Label(frame, text="insira uma mensagem aqui")
l_indentify.grid(column=0, row=0)

e_mensagem = Entry(frame)
e_mensagem.grid(column=1, row=0)

frame2 = Frame(main_window)
frame2.grid(column=0, row=1)
v = StringVar()
Label(frame2, textvariable=v).grid()

nome_maquina = "eduardo fa de sino placebo"
v.set("qual seu nome?")
entrada_sugestao = False
entrada_nome_sugestao = True
nome_usuario = ""

def roda_chatbot():
    global entrada_sugestao
    global entrada_nome_sugestao
    global nome_usuario
    global historico_conversa

    if entrada_nome_sugestao:
        nome_usuario = e_mensagem.get()
        saudacao = bot.saudacoes(nome_usuario)
        historico_conversa = f"{nome_maquina}: {saudacao}"
        v.set(historico_conversa)
        entrada_nome_sugestao = False
    else:
        texto = e_mensagem.get()
        historico_conversa += f"\n{nome_maquina}: {texto}"
        v.set(historico_conversa)

        if entrada_sugestao:
            bot.salva_sugestao(texto)
            entrada_sugestao = False
            historico_conversa += f"\nagora eu entendi\n"
            v.set(historico_conversa)

        else:
            resposta = bot.buscaresposta_GUI()(f"cliente: {texto}\n")
            if resposta == "me desculpa, eu sou burro!":
                historico_conversa += "me desculpa, eu sou burro! o que esperava?"
                v.set(historico_conversa)
                entrada_sugestao = True

            else:
                historico_conversa += f"\n{bot.exibeResposta_GUI(texto)}"
                v.set(historico_conversa)

Button(frame, text="clique", command=roda_chatbot).grid(column=0, row=1)
















































































































































































main_window.mainloop()
