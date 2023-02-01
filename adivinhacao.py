import random;#aleatoriza o numero secreto.

#inicializa.
def abertura():
    print("*********************************");
    print("Bem vindo ao jogo de Adivinhação!");
    print("*********************************");

#pergunta o nível e define as tentativas.
def define_tentativas():
    tentativas = 0;
    print("Qual nível de dificuldade?");
    print("(1) Fácil (2) Médio (3) Difícil");
    nivel = input("Defina o nível: ").upper().strip();
    if(nivel == '1' or nivel == 'FACIL'):
        tentativas = 20;
    elif(nivel == '2' or nivel == 'MEDIO'):
        tentativas = 15;
    else:
        tentativas = 10;
    return tentativas;

#pede para escolher um número.
def pede_chute():
    chute_str = input("Digite um número entre 1 e 1000: ");
    chute = int(chute_str);
    print("Você digitou ", chute);
    return chute;

#verifica se o chute é iqual, menor ou maior do que numero, determina o fator de vencedor ou perdedor e determina as rodadas.
def verifica_chute(tentativas, numero_secreto, pontos):
    for rodada in range(1, tentativas + 1):
        print("Tentativa {} de {}".format(rodada, tentativas));
        chute = pede_chute();
        if(chute < 1 or chute > 1000):
            print("Você deve digitar um número entre 1 e 100!");
            continue;
        if(chute == numero_secreto):
            vence(numero_secreto, pontos);
            exit();
        else:
            if(chute > numero_secreto):
                print("Você errou! O seu chute foi maior, tente um número menor.");
            elif(chute < numero_secreto):
                print("Você errou! O seu chute foi menor, tente um número maior.");
            pontos = pontuacao(pontos, numero_secreto, chute);

#arruma a pontuação para o final
def pontuacao(pontos, numero_secreto, chute):
    pontos_perdidos = abs(numero_secreto - chute);
    pontos = pontos - pontos_perdidos;
    return pontos;

#envia mensagem para o vencedor
def vence(numero_secreto, pontos):
    print("Você acertou!");
    print("       ___________      ");
    print("      '._==_==_=_.'     ");
    print("      .-\\:      /-.    ");
    print("     | (|:.     |) |    ");
    print("      '-|:.     |-'     ");
    print("        \\::.    /      ");
    print("         '::. .'        ");
    print("           ) (          ");
    print("         _.' '._        ");
    print("        '-------'       ");
    print("O numero secreto era {}.".format(numero_secreto));
    print("O total de pontos foi de {}.".format(pontos));

#envia mensagem para o perdedor
def fim(numero_secreto):
    print("Fim do jogo.");
    print("    _______________         ");
    print("   /               \        ");
    print("  /                 \       ");
    print("//                   \/\    ");
    print("\|   XXXX     XXXX   | /    ");
    print(" |   XXXX     XXXX   |/     ");
    print(" |   XXX       XXX   |      ");
    print(" |                   |      ");
    print(" \__      XXX      __/      ");
    print("   |\     XXX     /|        ");
    print("   | |           | |        ");
    print("   | I I I I I I I |        ");
    print("   |  I I I I I I  |        ");
    print("   \_             _/        ");
    print("     \_         _/          ");
    print("       \_______/            ");
    print("O numero secreto era {}.".format(numero_secreto));

#chama as funções, cria o número secreto e determina os pontos.
def principal():
    abertura();
    tentativas = define_tentativas();
    numero_secreto = random.randrange(1,1001);
    pontos = 10000;
    verifica_chute(tentativas, numero_secreto, pontos);
    fim(numero_secreto);

principal();
