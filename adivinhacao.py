import random;

def abertura():
    print("*********************************");
    print("Bem vindo ao jogo de Adivinhação!");
    print("*********************************");

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

def pede_chute():
    chute_str = input("Digite um número entre 1 e 1000: ");
    chute = int(chute_str);
    print("Você digitou ", chute);
    return chute;

def pontuacao(pontos, numero_secreto, chute):
    pontos_perdidos = abs(numero_secreto - chute);
    pontos = pontos - pontos_perdidos;
    return pontos;

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

def verifica_chute():
    abertura();
    tentativas = define_tentativas();
    numero_secreto = random.randrange(1,1001);
    pontos = 10000;
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
    fim(numero_secreto);

verifica_chute();