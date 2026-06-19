import os
import time


ZONA_VERDE = 1
ZONA_AMARELA = 2
ZONA_VERMELHA = 3
SEM_ALERTA = 0
ALERTA_CRISTALIZACAO = 1


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


def ajustar_pressao(valor):
    if valor > 150:
        return valor * 1.08

    return valor * 0.96


def classificar(valor):
    if 120 <= valor <= 180:
        return ZONA_VERDE

    if valor > 250:
        return ZONA_VERMELHA

    return ZONA_AMARELA


def verificar_alerta(valor):
    if valor < 120:
        return ALERTA_CRISTALIZACAO

    return SEM_ALERTA


def mostrar_classificacao(zona, alerta):
    if zona == ZONA_VERDE:
        print("Classificacao: Zona VERDE")
    elif zona == ZONA_AMARELA:
        print("Classificacao: Zona AMARELA")
    else:
        print("Classificacao: Zona VERMELHA")

    if alerta == ALERTA_CRISTALIZACAO:
        print("Alerta: pressao abaixo da Zona Verde. Risco de cristalizacao do fluido.")


def ler_total_leituras():
    total = 0

    while total <= 0:
        total = int(input("Digite o numero total de leituras: "))

        if total <= 0:
            print("Valor invalido. Digite um numero maior que zero para continuar.\n")

    return total


def main():
    print("====================================")
    print("              SEUC-4")
    print("====================================")

    total_leituras = ler_total_leituras()

    soma_pressao = 0
    menor_pressao_registrada = 0
    cont_verde = 0
    cont_amarela = 0
    cont_vermelha = 0
    cont_alerta_cristalizacao = 0
    cont_vermelha_consecutiva = 0
    i = 0

    while i < total_leituras and cont_vermelha_consecutiva < 2:
        limpar_tela()

        print("====================================")
        print(f"        LEITURA {i + 1}")
        print("====================================")

        valor = float(input("Digite a pressao hidrodinamica em UPCs: "))

        ajustado = ajustar_pressao(valor)
        zona = classificar(ajustado)
        alerta = verificar_alerta(ajustado)

        print("\nResultado:")
        print(f"Pressao ajustada: {ajustado:.2f} UPCs")
        mostrar_classificacao(zona, alerta)

        if i == 0:
            menor_pressao_registrada = valor
        elif valor < menor_pressao_registrada:
            menor_pressao_registrada = valor

        soma_pressao += ajustado

        if zona == ZONA_VERDE:
            cont_verde += 1
        elif zona == ZONA_AMARELA:
            cont_amarela += 1
        else:
            cont_vermelha += 1

        if alerta == ALERTA_CRISTALIZACAO:
            cont_alerta_cristalizacao += 1

        if zona == ZONA_VERMELHA:
            cont_vermelha_consecutiva += 1
        else:
            cont_vermelha_consecutiva = 0

        i += 1

        if cont_vermelha_consecutiva < 2:
            input("\nPressione ENTER para continuar...")

    if cont_vermelha_consecutiva == 2:
        limpar_tela()
        print("=== TRAVAMENTO DO SISTEMA ===")
        print("Duas leituras consecutivas na Zona VERMELHA!")
        time.sleep(2)

    total_processadas = i
    media = soma_pressao / total_processadas
    perc_verde = (cont_verde / total_processadas) * 100

    limpar_tela()
    print("====================================")
    print("        RESULTADOS FINAIS")
    print("====================================")
    print(f"Leituras na Zona Verde: {cont_verde}")
    print(f"Leituras na Zona Amarela: {cont_amarela}")
    print(f"Leituras na Zona Vermelha: {cont_vermelha}")
    print(f"Alertas de cristalizacao: {cont_alerta_cristalizacao}")
    print(f"Media das pressoes ajustadas: {media:.2f} UPCs")
    print(f"Menor pressao registrada: {menor_pressao_registrada:.2f} UPCs")
    print(f"% na Zona Verde: {perc_verde:.2f}%")

    if cont_vermelha_consecutiva == 2:
        perc_realizadas = (total_processadas / total_leituras) * 100
        print(f"Percentual de leituras realizadas: {perc_realizadas:.2f}%")

    print("\nFim do programa.")


if __name__ == "__main__":
    main()
