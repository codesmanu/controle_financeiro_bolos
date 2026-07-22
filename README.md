# 🍰 Bolos Finanças — Automação e Gestão Financeira

Projeto desenvolvido em **Python** para automatizar o controle financeiro de uma confeitaria, facilitando o gerenciamento de vendas, custos, lucros e relatórios.

O sistema permite criar planilhas financeiras automaticamente, atualizar preços, calcular indicadores de lucro, gerar dashboards com gráficos e exportar relatórios em PDF.

---

# 📂 Estrutura do Projeto

```text
bolos_financas/
│
├── precos.json                     # Fonte única dos preços dos ingredientes (dados)
├── precos.py                       # Funções para ler/gravar o precos.json
├── ficha_tecnica.py                 # Monta a aba "Ficha Técnica" (usado por gerar_planilha.py e gerar_dashboard.py)
│
├── atualizar_planilha.py           # Atualiza um preço em precos.json e regenera as planilhas
├── calcular_lucro.py               # Calcula custos, receitas e lucros (usado também pelo gerar_pdf.py)
├── gerar_dashboard.py               # Gera a planilha completa: ficha técnica + vendas + dashboard com gráfico
├── gerar_pdf.py                     # Exporta relatório em PDF
├── gerar_planilha.py                # Cria a planilha simples, só com a ficha técnica
│
├── Minha_Planilha_Completa.xlsx    # Planilha consolidada (gerada)
├── Minha_Planilha_Gerada.xlsx      # Planilha simples (gerada)
├── requirements.txt                 # Dependências do projeto
└── README.md                        # Documentação
```

> **Sobre a fonte única de preços:** antes, os preços dos ingredientes estavam
> duplicados dentro de `gerar_planilha.py`, `gerar_dashboard.py` e
> `calcular_lucro.py`. Agora eles moram só em `precos.json`, e todo mundo lê
> dali. Isso significa que **atualizar um preço com `atualizar_planilha.py`
> afeta automaticamente todos os arquivos gerados depois** — planilhas,
> cálculo de lucro e PDF.

---

# 🛠️ Instalação e Configuração

## Pré-requisitos

Antes de iniciar, certifique-se de possuir:

- Python 3.10 ou superior
- Pip instalado

Verifique a instalação com:

```bash
python --version
```

ou

```bash
py --version
```

---

## Criando um Ambiente Virtual (Opcional)

É recomendado utilizar um ambiente virtual para isolar as dependências do projeto.

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## Instalando as Dependências

Caso exista o arquivo **requirements.txt**, execute:

```bash
pip install -r requirements.txt
```

Caso ainda não exista, instale manualmente as bibliotecas utilizadas:

```bash
pip install openpyxl reportlab
```

---

## Gerando o arquivo `requirements.txt`

Após instalar as bibliotecas, você pode salvar todas as dependências do projeto executando:

```bash
pip freeze > requirements.txt
```

---

# 🚀 Como Executar

## 1️⃣ Gerar a Planilha Simples (opcional)

Cria só a ficha técnica, sem vendas nem dashboard.

```bash
python gerar_planilha.py
```

Gera: `Minha_Planilha_Gerada.xlsx`

---

## 2️⃣ Gerar a Planilha Completa

Cria a ficha técnica + o controle de vendas + o dashboard com gráfico, tudo no mesmo arquivo.

```bash
python gerar_dashboard.py
```

Gera: `Minha_Planilha_Completa.xlsx`

---

## 3️⃣ Atualizar um Preço

Quando um ingrediente mudar de preço no mercado, rode:

```bash
python atualizar_planilha.py
```

Esse script atualiza `precos.json` e pergunta se você quer regenerar as duas
planilhas (`Minha_Planilha_Gerada.xlsx` e `Minha_Planilha_Completa.xlsx`) na
hora com o preço novo. Se você disser não, é só rodar os passos 1 e 2 de
novo quando quiser aplicar o preço.

---

## 4️⃣ Calcular Lucros

Executa os cálculos financeiros no terminal.

```bash
python calcular_lucro.py
```

São calculados automaticamente:

- Custo por bolo (massa, recheio, calda, embalagem, margem de segurança)
- Lucro por venda a R$ 12 e R$ 13
- Fechamento do mês (faturamento, custo consumido, lucro real)

Pra fechar outro mês, edite as três primeiras linhas de `gerar_pdf.py`
(`NOME_MES`, `BOLOS_VENDIDOS`, `FATURAMENTO_TOTAL`) — o resto é recalculado
sozinho a partir do `precos.json`.

---

## 5️⃣ Gerar Relatório em PDF

Exporta um relatório financeiro completo, com os números vindos direto do
`calcular_lucro.py`.

```bash
python gerar_pdf.py
```

O arquivo PDF será salvo automaticamente na pasta do projeto.

---

# 📋 Funcionalidades

| Script | Descrição |
|---------|-----------|
| **precos.py** | Fonte única dos preços dos ingredientes (leitura/escrita do precos.json). |
| **ficha_tecnica.py** | Monta a aba de ficha técnica, reaproveitada pelos dois geradores de planilha. |
| **gerar_planilha.py** | Cria a planilha simples, só com a ficha técnica. |
| **gerar_dashboard.py** | Cria a planilha completa: ficha técnica + vendas + dashboard com gráfico. |
| **atualizar_planilha.py** | Atualiza um preço em precos.json e oferece regenerar as planilhas na hora. |
| **calcular_lucro.py** | Calcula custos, receitas e lucro das vendas. |
| **gerar_pdf.py** | Exporta um relatório financeiro em PDF. |

---

# 📊 Recursos

O projeto permite:

- 📄 Criação automática de planilhas Excel
- 💰 Controle financeiro com preço único e sincronizado em todos os arquivos
- 📈 Cálculo automático de lucro
- 📊 Dashboard financeiro
- 📉 Gráficos de desempenho
- 📑 Exportação de relatórios em PDF

---

# 🧰 Tecnologias Utilizadas

- Python
- OpenPyXL
- ReportLab

---

# 🎯 Objetivo

O projeto foi desenvolvido para automatizar tarefas financeiras de uma confeitaria familiar, reduzindo erros em controles manuais e proporcionando uma visão clara dos resultados financeiros através de planilhas, dashboards e relatórios simples de entender. 

Além disso, demonstra a utilização prática do Python para automação de processos administrativos e análise de dados.

---

# 👩‍💻 Desenvolvedora

**Emanuelly Rackel**

---
