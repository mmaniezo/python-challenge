def forca_opcao(lista_opcoes, msg): #Forçar o usuário a escolher uma opção
    msg_erro = '\n'.join(lista_opcoes)
    opcao = input(msg)
    while opcao not in lista_opcoes:
        print(f"Opção inválida! Somente essas:\n{msg_erro}")
        opcao = input(msg)
    return opcao

def meu_index(lista, elemento): #Encontrar um indice dentro de uma lista
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
    return

def tem_saldo(saldo, custo): #Verificar se o usuário ainda tem saldo suficiente
    if custo < saldo:
        return True
    print("Quantidade de créditos insuficente, escolha outra opção!")
    return False

print("====== Seja bem-vindo(a) ao HitRace Fantasy Formula E ======")
nome_equipe = input("Escolha um nome para a sua equipe:\n-> ")

pilotos = ["Mitch EVANS", "Antônio Felix DA COSTA", "Nyck DE VRIES"]
equipe_pilotos = ["Jaguar", "Porsche", "Mahindra"]
precos_pilotos = [17, 14, 9]
pilotos_num = ["1", "2", "3"]

creditos = 100
while True: #O usuário é apresentado a lista de pilotos e a sua quantidade atual de créditos, ao escolher um piloto a quantidade de créditos é retirada do usuário, e caso escolha uma opção que não exista ele é foeçado a responder corretamente, e se ele não tiver créditos suficientes, ele volta ao inicio do while. E por fim caso de certo, o piloto escolhido é removido.
    print("=== PILOTOS DISPONÍVEIS ===")
    for i in range(len(pilotos)):
        print(f"{pilotos_num[i]}) {pilotos[i]}, da {equipe_pilotos[i]} - {precos_pilotos[i]} créditos")
    print(f"Você possui {creditos} créditos.")

    escolha_piloto1 = forca_opcao(pilotos_num, "Escolha o seu primeiro piloto (digite o número correspondente):\n-> ")
    indice1 = meu_index(pilotos_num, escolha_piloto1)
    if tem_saldo(creditos, precos_pilotos[indice1]):
        piloto1 = pilotos[indice1]
        print(f"Seu piloto 1 é o {piloto1}!\n")
        preco_piloto1 = precos_pilotos[indice1]
        creditos -= preco_piloto1
        pilotos.remove(pilotos[indice1])
        equipe_pilotos.remove(equipe_pilotos[indice1])
        precos_pilotos.remove(precos_pilotos[indice1])
        pilotos_num.remove(pilotos_num[indice1])
        break

while True: #Bem parecido com a explicação dada anteriormente, o diferencial é que aqui não precisamos remover o piloto ainda não escolhido, já que a lista de pilotos não será apresentada novamente
    print("=== PILOTOS DISPONÍVEIS ===")
    for i in range(len(pilotos)):
        print(f"{pilotos_num[i]}) {pilotos[i]}, da {equipe_pilotos[i]} - {precos_pilotos[i]} créditos")
    print(f"Você possui {creditos} créditos.")

    escolha_piloto2 = forca_opcao(pilotos_num,
                                  "Escolha seu segundo piloto (digite o número correspondente):\n-> ")
    indice2 = meu_index(pilotos_num, escolha_piloto2)
    if tem_saldo(creditos, precos_pilotos[indice2]):
        piloto2 = pilotos[indice2]
        print(f"Seu piloto 2 é o {piloto2}!\n")
        preco_piloto2 = precos_pilotos[indice2]
        creditos -= preco_piloto2
        break

equipes = ["Porsche", "Jaguar", "Mahindra", "Maserati", "McLaren"]
equipes_num = ["1", "2", "3", "4", "5"]
precos_equipes = [17, 15, 13, 12, 13]
while True: #O usuário é apresentado a lista de equipes e a sua quantidade atual de créditos, ao escolher uma equipe a quantidade de créditos é retirada do usuário, e caso escolha uma opção que não exista ele é foeçado a responder corretamente, e se ele não tiver créditos suficientes, ele volta ao inicio do while.
    print("=== EQUIPES DISPONÍVEIS ===")
    for i in range(len(equipes)):
        print(f"{equipes_num[i]}) {equipes[i]} - {precos_equipes[i]} créditos")
    print(f"Você possui {creditos} créditos.")
    escolha_equipe = forca_opcao(equipes_num,
                                 "Escolha uma equipe para representar (digite o número correspondente):\n-> ")
    indice_equipe = meu_index(equipes_num, escolha_equipe)
    if tem_saldo(creditos, precos_equipes[indice_equipe]):
        equipe = equipes[indice_equipe]
        print(f"Sua equipe é a {equipe}!\n")
        preco_equipe = precos_equipes[indice_equipe]
        creditos -= preco_equipe
        break

motores = ["Porsche 99X Electric", "Mahindra M9Electro", "Jaguar I-Type 6"]
motores_num = ["1", "2", "3"]
precos_motores = [17, 11, 16]
while True: #A descrição do tópico anterior será aplicada também aos motores!
    print("=== MOTORES DISPONÍVEIS ===")
    for i in range(len(motores)):
        print(f"{motores_num[i]}) {motores[i]} - {precos_motores[i]} créditos")
    print(f"Você possui {creditos} créditos.")
    escolha_motor = forca_opcao(motores_num,
                                "Escolha um motor para seu carro (digite o número correspondente):\n-> ")
    indice_motor = meu_index(motores_num, escolha_motor)
    if tem_saldo(creditos, precos_motores[indice_motor]):
        motor = motores[indice_motor]
        print(f"Seu motor é o {motor}!\n")
        preco_motor = precos_motores[indice_motor]
        creditos -= preco_motor
        break

tecnicos = ["Thomas Biermaier", "Frederic Bertrand", "Florian Modlinger"]
tecnicos_equipe = ["ABT", "Mahindra", "Porsche"]
tecnicos_num = ["1", "2", "3"]
precos_tecnicos = [11, 12, 18]
while True: #A descrição do tópico retrasado será aplicada também aos técnicos!
    print("=== TÉCNICOS DISPONÍVEIS ===")
    for i in range(len(tecnicos)):
        print(f"{tecnicos_num[i]}) {tecnicos[i]}, da {tecnicos_equipe[i]} - {precos_tecnicos[i]} créditos")
    print(f"Você possui {creditos} créditos.")
    escolha_tecnico = forca_opcao(tecnicos_num,
                                "Escolha um técnico para a sua equipe (digite o número correspondente):\n-> ")
    indice_tecnico = meu_index(tecnicos_num, escolha_tecnico)
    if tem_saldo(creditos, precos_tecnicos[indice_tecnico]):
        tecnico = tecnicos[indice_tecnico]
        print(f"Seu tecnico é o {tecnico}!\n")
        preco_tecnico = precos_tecnicos[indice_tecnico]
        creditos -= preco_tecnico
        break

print(f"Sua equipe, a {nome_equipe}, está escalada assim:\n" #Um print mostrando todas as opções escolhidas pelo usuário e sua quantidade final de créditos.
      f"Piloto 1: {piloto1} - {preco_piloto1} créditos\n"
      f"Piloto 2: {piloto2} - {preco_piloto2} créditos\n"
      f"Equipe representante: {equipe} - {preco_equipe} créditos\n"
      f"Motor: {motor} - {preco_motor} créditos\n"
      f"Técnico: {tecnico} - {preco_tecnico} créditos\n"
      f"Seu saldo restante é de {creditos} créditos.")
