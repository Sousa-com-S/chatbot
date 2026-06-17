import bot
resposta1 = input("qual meu nome?")
nome_maquina = resposta1
bot.saudacoes(nome_maquina)

while True:
    texto = bot.recebetexto()
    resposta = bot.buscaresposta(nome_maquina, texto)
    if bot.exibaresposta(resposta, nome_maquina) == "fim":
        break