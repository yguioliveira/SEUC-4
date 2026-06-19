# SEUC-4

Sistema de Escoamento de Unidades de Carga desenvolvido em Python para simular o monitoramento imediato de pressoes hidrodinamicas em um duto industrial.

O programa processa cada leitura no momento em que ela e informada, aplica o ajuste termico definido pelas regras do sistema, classifica a estabilidade da pressao e calcula metricas finais sem armazenar todo o historico de leituras.

## Funcionalidades

- Ajuste termico automatico das leituras de pressao.
- Classificacao das pressoes ajustadas em Zona Verde, Zona Amarela ou Zona Vermelha.
- Alerta de cristalizacao para pressoes ajustadas abaixo de `120 UPCs`.
- Travamento automatico ao detectar duas leituras consecutivas na Zona Vermelha.
- Calculo da media das pressoes ajustadas.
- Registro da menor pressao informada.
- Porcentagem de leituras classificadas na Zona Verde.
- Percentual de leituras realizadas quando ocorre travamento.

## Regras do Sistema

- Leituras acima de `150 UPCs` recebem acrescimo de `8%`.
- Leituras abaixo ou iguais a `150 UPCs` recebem reducao de `4%`.
- Zona Verde: valores ajustados entre `120` e `180 UPCs`.
- Zona Amarela: valores ajustados fora da Zona Verde e ate `250 UPCs`.
- Zona Vermelha: valores ajustados acima de `250 UPCs`.
- Duas leituras consecutivas na Zona Vermelha interrompem o processo.
- Leituras ajustadas abaixo de `120 UPCs` geram alerta de cristalizacao, mas nao interrompem o processo.

## Como Executar

Requisitos:

- Python 3 instalado.

No terminal, dentro da pasta do projeto, execute:

```bash
python main.py
```

Em seguida, informe o numero total de leituras e digite cada pressao solicitada pelo sistema.

## Estrutura

```text
.
|-- main.py
|-- README.md
`-- LICENSE
```

## Licenca

Este projeto esta licenciado sob a licenca MIT. Consulte o arquivo `LICENSE` para mais detalhes.
