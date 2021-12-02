def cadastrar_vaga(vagas, num_vagas):
    vaga = []
    vaga.append(num_vagas)
    vaga.append(0)
    vagas.append(vaga)

    print(f"\nCadastro finalizado...\nSua vaga foi criada com sucesso: {num_vagas}\n")
    input("\nAperte enter para continuar...\n")

def listar_vagas(vagas, num_vagas):

    for i in range(0, num_vagas):
        if vagas[i][1] == 0:
            print(f"\nA Vaga {i} esta desocupada e disponível!\n")
        else:
            print(f"\nA vaga {i} está ocupada pelo carro: {vagas[i][2]}")
    input("\nAperte enter para continuar...\n")

def novo_carro(vagas, num_vagas, historico, num_carro):

    print("\nDigite algumas informações sobre o carro abaixo...")
    marca  = input("\nQual a marca do carro? > ")
    modelo = input("Qual o modelo do carro? > ")
    cor    = input("Qual a cor do carro? > ")
    num_placa = input("Qual o número da placa? > ")
    hora_entrada = input("Qual foi o horário de entrada? > ")
    
    listar_vagas(vagas, num_vagas)

    vaga = int(input("\nEm qual vaga ele irá estacionar? > "))    
    carro = [marca, modelo, cor, num_placa, vaga, hora_entrada]
    
    historico.append(carro)
    vagas[vaga].append(num_carro)
    vagas[vaga][1] = 1

def retirar_carro(vagas, num_vagas, historico):

    print("\nInforme algumas informações a seguir...")
    hora_saida = input("\nQual foi horário de saída? > ")
    
    listar_vagas(vagas, num_vagas)

    carro = int(input("Qual foi o carro que saiu? > "))
    vaga = int(input("Em qual vaga ele estava? > "))

    input("\nAperte enter para continuar...\n")

    historico[carro].append(hora_saida)
    vagas[vaga][1]=0

def visualisar_historico(historico):

    for i in range(0, len(historico)):
        print("\n\t    Histórico de carros")
        print(f"\nO carro da marca {historico[i][0]}\nModelo: {historico[i][1]}\nCor: {historico[i][2]}\nPlaca: {historico[i][3]}")
        print(f"\nDeu entrada na vaga: {historico[i][4]} às {historico[i][5]}\nDeu saída ás: {historico[i][6]}\n")

def main():

    vagas = []
    historico = []
    num_vagas = 0
    numcarro = 0

    while True:
        print("\n\t    Gerenciamento de Estacionamento")
        print("\n\t    Cadastrar vagas     - [1]\n\t    Listar vagas        - [2]\n\t    Cadastrar carros    - [3]\n\t    Remover carros      - [4]")
        print("\t    Histórico de carros - [5]\n\n\t    Sair - [0]") 
    
        escolha = int(input("\nDigite o número da opção que deseja acessar:\n>>> "))

        if escolha   == 1:
            cadastrar_vaga(vagas, num_vagas)
            num_vagas += 1
        elif escolha == 2:
            listar_vagas(vagas, num_vagas)
        elif escolha == 3:
            novo_carro(vagas, num_vagas, historico, numcarro)
            numcarro += 1
        elif escolha == 4:
            retirar_carro(vagas, num_vagas, historico)
        elif escolha == 5:
            visualisar_historico(historico)
        elif escolha == 0:
            return 0

main()