def saudacoes(nome):
    import random
    frases = [f"bom dia! meu nome é pokelerolero. Como vai voçe?", "sai daqui pedro inutil!", "Ola oque posso fazer por voçê hoje?", "Hola, ¿en qué puedo ayudarte hoy?"]
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