# Sistema de Escoamento de Unidades de Carga

Sistema de monitoramento de pressao em terminal desenvolvido em Python. O projeto processa leituras hidrodinamicas, aplica ajuste termico, classifica zonas de estabilidade, emite alerta de cristalizacao e interrompe o escoamento em caso de leituras criticas consecutivas.

Projeto academico desenvolvido para a disciplina de Algoritmos de Programacao, Projetos e Computacao, adaptado para apresentacao em portfolio.

## Funcionalidades

- Leitura da quantidade total de medicoes do turno.
- Entrada individual de pressoes hidrodinamicas em UPCs.
- Ajuste termico automatico das pressoes informadas.
- Classificacao das pressoes ajustadas em Zona Verde, Zona Amarela ou Zona Vermelha.
- Alerta de cristalizacao para pressoes ajustadas abaixo de `120 UPCs`.
- Contagem de leituras em cada zona de estabilidade.
- Travamento automatico ao detectar duas leituras consecutivas na Zona Vermelha.
- Calculo da media das pressoes ajustadas.
- Registro da menor pressao informada durante o processo.
- Calculo da porcentagem de leituras classificadas na Zona Verde.
- Exibicao do percentual de leituras realizadas caso ocorra travamento.

## Tecnologias

- Python
- Git e GitHub

## Estrutura do projeto

```text
seuc-4/
|-- main.py
|-- README.md
`-- LICENSE
```

## Como executar

1. Clone o repositorio

```bash
git clone https://github.com/yguioliveira/seuc-4.git
cd seuc-4
```

2. Execute o sistema

```bash
python main.py
```

3. Informe os dados solicitados

O sistema solicita o numero total de leituras do turno e, em seguida, pede cada pressao hidrodinamica em UPCs.

## Fluxo principal

- O sistema inicia pelo `main.py`.
- O operador informa a quantidade total de leituras.
- Para cada leitura, o sistema recebe a pressao original.
- A pressao passa pelo ajuste termico.
- O valor ajustado e classificado em uma zona de estabilidade.
- Caso o valor ajustado fique abaixo de `120 UPCs`, o sistema exibe alerta de cristalizacao.
- Caso duas leituras consecutivas fiquem na Zona Vermelha, o sistema interrompe o processo.
- Ao final, o sistema exibe as metricas calculadas durante a execucao.

## Regras do sistema

- Leituras acima de `150 UPCs` recebem acrescimo de `8%`.
- Leituras abaixo ou iguais a `150 UPCs` recebem reducao de `4%`.
- Zona Verde: valores ajustados entre `120` e `180 UPCs`.
- Zona Amarela: valores ajustados fora da Zona Verde e ate `250 UPCs`.
- Zona Vermelha: valores ajustados acima de `250 UPCs`.
- Duas leituras consecutivas na Zona Vermelha interrompem o processo.
- Leituras ajustadas abaixo de `120 UPCs` geram alerta de cristalizacao, mas nao interrompem o processo.

## Metricas finais

Ao encerrar por conclusao ou travamento, o sistema exibe:

- Quantidade de leituras na Zona Verde.
- Quantidade de leituras na Zona Amarela.
- Quantidade de leituras na Zona Vermelha.
- Quantidade de alertas de cristalizacao.
- Media das pressoes ajustadas.
- Menor pressao registrada.
- Porcentagem de leituras na Zona Verde.
- Percentual de leituras realizadas, caso ocorra travamento.

## Licenca

Este projeto esta licenciado sob a licenca MIT.
