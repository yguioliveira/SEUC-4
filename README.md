# 📡 SEUC-4

Sistema de monitoramento de pressão hidrodinâmica desenvolvido em Python, responsável por processar leituras, classificar condições operacionais e emitir alertas automáticos para situações críticas.

O projeto simula o funcionamento de um sistema de supervisão industrial, realizando ajustes nos valores recebidos, identificando zonas de operação e interrompendo o processo quando condições perigosas são detectadas.

---

## 🎯 Objetivo

Desenvolver uma solução capaz de monitorar leituras de pressão hidrodinâmica, classificando automaticamente os resultados e auxiliando na identificação de riscos operacionais.

---

## 🚀 Funcionalidades

### 📊 Processamento das leituras
- Registro de múltiplas leituras de pressão;
- Ajuste automático dos valores conforme regras estabelecidas;
- Armazenamento e processamento dos dados coletados.

### 🟢 Classificação automática
As leituras ajustadas são classificadas em três zonas operacionais:

- 🟢 Zona Verde: operação dentro dos parâmetros ideais;
- 🟡 Zona Amarela: condição de atenção;
- 🔴 Zona Vermelha: condição crítica.

### ⚠️ Alertas automáticos
- Identificação de risco de cristalização do fluido;
- Emissão de alertas para leituras abaixo do limite seguro;
- Contabilização do número total de alertas emitidos.

### 🚨 Tratamento de falhas críticas
- Monitoramento de leituras consecutivas na Zona Vermelha;
- Travamento automático do sistema após duas ocorrências consecutivas;
- Interrupção preventiva do processamento para preservar a integridade operacional.

### 📈 Estatísticas finais
Ao final da execução, o sistema apresenta:

- Quantidade de leituras em cada zona;
- Total de alertas de cristalização;
- Média das pressões ajustadas;
- Menor pressão registrada;
- Percentual de leituras classificadas na Zona Verde;
- Percentual de leituras realizadas antes do travamento do sistema (quando aplicável).

---

## ⚙️ Regras implementadas

### Ajuste da pressão

- Valores acima de **150 UPCs** recebem ajuste de **+8%**;
- Valores iguais ou inferiores a **150 UPCs** recebem ajuste de **-4%**.

### Classificação das zonas

| Faixa de pressão ajustada | Classificação |
|---------------------------|---------------|
| 120 a 180 UPCs | 🟢 Zona Verde |
| 181 a 250 UPCs ou abaixo de 120 UPCs | 🟡 Zona Amarela |
| Acima de 250 UPCs | 🔴 Zona Vermelha |

### Alerta de cristalização

O alerta é emitido quando a pressão ajustada fica abaixo de **120 UPCs**, indicando risco de cristalização do fluido.

### Travamento do sistema

O sistema é encerrado automaticamente após o registro de **duas leituras consecutivas na Zona Vermelha**.

---

## 🛠️ Tecnologias utilizadas

- Python 3
- Bibliotecas padrão do Python:
  - `os`
  - `time`
- VS Code

---

## 🧠 Conceitos aplicados

Durante o desenvolvimento deste projeto foram aplicados conceitos como:

- Estruturas condicionais;
- Estruturas de repetição;
- Modularização por funções;
- Definição e utilização de constantes;
- Tratamento de cenários críticos;
- Processamento e análise de dados;
- Simulação de sistemas de monitoramento.

---

## ▶️ Como executar

1. Clone este repositório:

```bash
git clone https://github.com/yguioliveira/seuc4.git
```

2. Acesse a pasta do projeto:

```bash
cd seuc4
```

3. Execute o programa:

```bash
python seuc4.py
```

---

## 📷 Demonstração

Adicione capturas de tela do sistema em execução, como:

- Tela inicial;
- Processamento das leituras;
- Exemplo de alerta de cristalização;
- Exemplo de travamento do sistema;
- Resultados finais.

---

## 🎓 Contexto acadêmico

Projeto desenvolvido como atividade acadêmica do curso de Engenharia de Software da Pontifícia Universidade Católica de Campinas (PUC Campinas).

---

## 📚 Aprendizados

Este projeto contribuiu para o desenvolvimento de habilidades relacionadas ao processamento de dados, implementação de regras de classificação, identificação de situações críticas e construção de sistemas capazes de auxiliar na tomada de decisão em cenários simulados de monitoramento industrial.
