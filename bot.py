def saudacoes(nome):
    import random
    frases = [f"bom dia. Como vai voçe?", "sai daqui pedro inutil!", "Ola oque posso fazer por voçê hoje?", "Hola, ¿en qué puedo ayudarte hoy?"]
    print(frases[random.randint(0, len(frases)-1)])


def recebetexto():
    texto = "cliente: " + input("cliente: ")
    palavraproibida = ["troxa", "burro", "bobo", "catapimbas", "caio ribeiro!"]
    for p in palavraproibida:
        if p in texto:
            print(f"seu peba!, vem me chamar de {p} não")
            return recebetexto()
    return texto


def buscaresposta(nome, texto):
    with open("contexto.txt", "a+", encoding="utf-8") as conhecimento:
        conhecimento.seek(0)
        while True:
            viu = conhecimento.readline()
            if viu != "":
                if texto.replace("cliente: ", "") == "tchau":
                    print(f"{nome} volte sempre!")
                    return "fim"
                elif viu.strip() == texto.strip():
                    proximalinha = conhecimento.readline()
                    if "chatbot" in proximalinha:
                        return proximalinha
            else:
                print("me desculpe, sou burro!")
                conhecimento.write(f"\n{texto}")
                resposta_user = input("o que esperava?\n")
                conhecimento.write(f"\nchatbot: " + resposta_user)
                return "hum..."

def exibaresposta(resposta, nome):
    print(resposta.replace("chatbot",nome))
    if resposta == "fim":
        return "fim"
    return "continua"


def exibeResposta_GUI(texto, resposta, nome):
    return resposta.replace("Chatbot", nome)


def saudacao_GUI(nome):
    import random
    frases = ["Bom dia! Meu nome é " + nome + ". Como vai você?", "Olá!", "Oi, tudo bem?"]
    return frases[random.randint(0, 2)]


def salva_sugestao(sugestao):
    with open("contexto.txt", "a+") as conhecimento:
        conhecimento.write("Chatbot: " + sugestao + "\n")


def buscaResposta_GUI(texto):
    with open("BaseDeConhecimento.txt", "a+") as conhecimento:
        conhecimento.seek(0)
        while True:
            viu = conhecimento.readline()
            if viu != "":
                if jaccard(texto, viu) > 0.3:
                    proximalinha = conhecimento.readline()
                    if "Chatbot: " in proximalinha:
                        return proximalinha
            else:
                conhecimento.write('\n' + texto)
                return "Me desculpe, não sei o que falar"


def jaccard(textoUsuario, textoBase):
    textoUsuario = limpa_frase(textoUsuario)
    textoBase = limpa_frase(textoBase)
    if len(textoBase) < 1:
        return 0
    else:
        palavras_em_comum = 0
        for palavra in textoUsuario.split():
            if palavra in textoBase.split():
                palavras_em_comum += 1
        return palavras_em_comum / (len(textoBase.split()))


def limpa_frase(frase):
    tirar = ["?", "!", "...", ".", ",", "Cliente: ", "\n"]
    for t in tirar:
        frase = frase.replace(t, "")
    frase = frase.upper()
    return frase