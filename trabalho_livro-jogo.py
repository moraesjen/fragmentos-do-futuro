#Trabalho de Lógica e Algoritimo - Livro Jogo

def escolha_valida(pergunta): #função usada para criar um laço de repetição caso o usuario entre com um valor invalido (diferente de a ou b)
    while True: 
        escolha = input(pergunta).lower() #exibe a pergunta e converte a entrada para minusculo
        if escolha in ['a', 'b'] : #verifica se a entrada do usuario é valida
            return escolha #retorna a escolha feita, encerrando a função
        else:
            print("Escolha inválida. Digite apenas 'a' ou 'b'.\n")
            
print("\t\t\tFragmentos de um Futuro Perdido")
print("Ano de 2061. A Terra está devastada após um vírus misterioso dizimar a humanidade.")
print("Você é um cientista sobrevivente, com memórias fragmentadas e uma missão que pode salvar ou condenar o mundo.")

print("\nVocê acorda em um laboratório destruído. Sua cabeça lateja e pedaços da memória começam a voltar.")
print("Primeira decisão: O que você faz?")
print("a) Vasculhar o laboratório em busca de pistas.") #Leva para a linha 22
print("b) Sair imediatamente e procurar seu antigo parceiro.") #Leva para a linha 79

escolha1 = escolha_valida("Escolha (a/b): ").lower()  #chama a função escolha_valida e passando como argumento o texto "Escolha (a/b): ". Esse texto entra na função no lugar do parâmetro (pergunta).

if escolha1 == "a": 
    print("\nVocê encontra registros dos seus últimos experimentos e descobre coordenadas de uma instalação militar.")
    print("Segunda decisão: Você...")
    print("a) Segue para a instalação militar em busca de recursos.") #Leva para a linha 30
    print("b) Tenta entrar em contato com outros sobreviventes pela rádio.") #Leva para a linha 61

    escolha2 = escolha_valida("Escolha (a/b): ").lower()

    if escolha2 == "a":
        print("\nA instalação está fortemente vigiada por drones do governo.")
        print("Terceira decisão: Você...")
        print("a) Tenta se infiltrar furtivamente.") #Leva para Linha 38
        print("b) Recua e procura outro caminho.") #Leva para Linha 56 (FINAL ALTERNATIVO)

        escolha3 = escolha_valida("Escolha (a/b): ").lower()

        if escolha3 == "a":
            print("\nVocê consegue entrar, mas ativa um alarme.")
            print("Seu antigo parceiro aparece de repente, ele estava escondido ali.")
            print("Quarta decisão: Ele oferece uma chance de usar a máquina do tempo. Você aceita?")
            print("a) Sim, tentar mudar o passado.") #Leva para Linha 47 (FINAL 1)
            print("b) Não, focar em criar a cura no presente.") #Leva para Linha 51 (FINAL 2)

            escolha4 = escolha_valida("Escolha (a/b): ").lower()

            if escolha4 == "a": #FINAL 1
                print("\nVocês ativam a máquina... mas algo dá errado.") 
                print("Você é lançado para um futuro ainda pior, onde a humanidade já não existe.")
                print("FINAL RUIM: A tentativa de mudar o passado falhou e piorou tudo.") 
            elif escolha4 == "b": #FINAL 2
                print("\nVocês combinam esforços e usam os dados recuperados para sintetizar uma vacina.")
                print("Após semanas de trabalho, conseguem imunizar um pequeno grupo.")
                print("FINAL BOM: Um novo começo para a humanidade.")
           
        elif escolha3 == "b": #FINAL ALTERNATIVO 
            print("\nAo tentar fugir, você é capturado pelos drones do governo.")
            print("Eles te levam para um centro de interrogatório.")
            print("FINAL NEUTRO: Você sobrevive, mas perde sua liberdade.")

    elif escolha2 == "b":
        print("\nVocê consegue sinal na rádio e recebe uma resposta.")
        print("Uma comunidade secreta de sobreviventes te convida.")
        print("Terceira decisão: Você...")
        print("a) Aceita o convite e segue para a comunidade.") #Leva para a Linha 70 (FINAL 3)
        print("b) Desconfia e decide investigar antes.") #Leva para a Linha 74 (FINAL 4)

        escolha3 = escolha_valida("Escolha (a/b): ").lower()

        if escolha3 == "a": #FINAL 3
            print("\nChegando lá, você descobre que eles estão trabalhando em uma cura coletiva.")
            print("Com sua ajuda, aceleram o processo e salvam centenas de pessoas.")
            print("FINAL BOM: Uma chance real de reconstruir a civilização.")
        elif escolha3 == "b": #FINAL 4
            print("\nVocê descobre que era uma armadilha dos soldados do governo.")
            print("Você é capturado e nunca mais ouvido.")
            print("FINAL RUIM: A busca pela verdade te custou a vida.")

elif escolha1 == "b":
    print("\nVocê parte em busca de seu antigo parceiro.")
    print("Após horas, o encontra isolado, cercado de equipamentos estranhos.")
    print("Ele te revela que aperfeiçoou uma máquina do tempo, mas ela não é estável.")
    print("Segunda decisão: Você...")
    print("a) Concorda em usar a máquina para impedir o surgimento do vírus.") #Leva para a Linha 89
    print("b) Sugere trabalhar juntos em uma vacina no presente.") #Leva para a Linha 107

    escolha2 = escolha_valida("Escolha (a/b): ").lower()

    if escolha2 == "a":
        print("\nVocês ativam a máquina e viajam para 2020.")
        print("Terceira decisão: Você encontra o laboratório onde tudo começou.")
        print("a) Destruir o laboratório imediatamente.") #Leva para a Linha 97
        print("b) Roubar os dados e buscar outra solução.") #Leva para a Linha 101

        escolha3 = escolha_valida("Escolha (a/b): ").lower()

        if escolha3 == "a": #FINAL 3
            print("\nA explosão impede o surgimento do vírus, mas altera outras linhas do tempo.")
            print("O mundo volta ao normal, mas com estranhas mudanças históricas.")
            print("FINAL BOM: O vírus nunca existiu, mas... algo está diferente.")
        elif escolha3 == "b": #FINAL 4
            print("\nVocê descobre que o vírus não foi um acidente, mas sim uma arma.")
            print("Ao retornar, traz dados suficientes para expor e derrubar o governo autoritário.")
            print("FINAL EXCELENTE: Você não só salva a humanidade, como também liberta as pessoas da opressão.") 
        

    elif escolha2 == "b": 
        print("\nVocês começam a trabalhar na vacina.")
        print("De repente, são atacados por agentes do governo que querem silenciá-los.")
        print("Terceira decisão: Você...")
        print("a) Luta contra eles.") #LEVA PARA A LINHA 116 (FINAL 5)
        print("b) Foge e tenta salvar os dados.") #Leva para a linha 120 (FINAL 6)

        escolha3 = input("Escolha (a/b): ").lower()

        if escolha3 == "a": #FINAL 5
            print("\nA luta é intensa, mas vocês são capturados.")
            print("Os dados são destruídos.")
            print("FINAL RUIM: O governo vence, e a esperança morre com vocês.")
        elif escolha3 == "b": #FINAL 6
            print("\nVocê foge levando os dados, consegue transmiti-los para outros grupos de resistência.")
            print("Graças a você, a cura é desenvolvida por cientistas escondidos.")
            print("FINAL BOM: A humanidade sobrevive e o governo perde força.")
      

print("\n\t\t\tFim da Jornada") #FINISH!