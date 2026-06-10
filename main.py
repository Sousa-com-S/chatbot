import bot

nome_maquina = "caio ribeiro"
bot.saudacoes(nome_maquina)

while True:
    texto = bot.recebetexto()
    resposta = bot.buscaresposta(nome_maquina, texto)
    if bot.exibaresposta(resposta, nome_maquina) == "fim":
        break