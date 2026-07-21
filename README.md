# 🍰 Bolos Finanças — Automação e Gestão Financeira

Projeto desenvolvido em **Python** para automatizar o controle financeiro de uma confeitaria, facilitando o gerenciamento de vendas, custos, lucros e relatórios.

O sistema permite criar planilhas financeiras automaticamente, atualizar registros, calcular indicadores de lucro, gerar dashboards com gráficos e exportar relatórios em PDF.

---

# 📂 Estrutura do Projeto

```text
bolos_financas/
│
├── atualizar_planilha.py          # Atualiza os dados de uma planilha existente
├── calcular_lucro.py              # Calcula custos, receitas e lucros
├── gerar_dashboard.py             # Gera gráficos e dashboard financeiro
├── gerar_pdf.py                   # Exporta relatórios em PDF
├── gerar_planilha.py              # Cria a planilha base de finanças
│
├── Minha_Planilha_Completa.xlsx   # Planilha consolidada
├── Minha_Planilha_Gerada.xlsx     # Planilha criada pelos scripts
├── requirements.txt               # Dependências do projeto
└── README.md                      # Documentação
```

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
pip install openpyxl reportlab pandas matplotlib
```

---

## Gerando o arquivo `requirements.txt`

Após instalar as bibliotecas, você pode salvar todas as dependências do projeto executando:

```bash
pip freeze > requirements.txt
```

---

# 🚀 Como Executar

Os scripts foram separados por funcionalidades específicas.

A ordem recomendada de execução é apresentada abaixo.

---

## 1️⃣ Gerar a Planilha Base

Cria a estrutura inicial da planilha financeira.

```bash
python gerar_planilha.py
```

Será criado o arquivo:

```text
Minha_Planilha_Gerada.xlsx
```

---

## 2️⃣ Atualizar a Planilha

Atualiza os dados financeiros existentes.

```bash
python atualizar_planilha.py
```

Este script atualiza o arquivo:

```text
Minha_Planilha_Completa.xlsx
```

---

## 3️⃣ Calcular Lucros

Executa os cálculos financeiros.

```bash
python calcular_lucro.py
```

São calculados automaticamente:

- Receita
- Custos
- Lucro Bruto
- Lucro Líquido
- Margem de Lucro

---

## 4️⃣ Gerar Dashboard

Cria gráficos e indicadores financeiros.

```bash
python gerar_dashboard.py
```

O dashboard apresenta informações como:

- Faturamento
- Custos
- Lucro
- Comparativos financeiros
- Indicadores de desempenho

---

## 5️⃣ Gerar Relatório em PDF

Exporta um relatório financeiro completo.

```bash
python gerar_pdf.py
```

O arquivo PDF será salvo automaticamente na pasta do projeto.

---

# 📋 Funcionalidades

| Script | Descrição |
|---------|-----------|
| **gerar_planilha.py** | Cria a estrutura inicial da planilha financeira. |
| **atualizar_planilha.py** | Atualiza registros e informações financeiras. |
| **calcular_lucro.py** | Calcula custos, receitas e lucro das vendas. |
| **gerar_dashboard.py** | Gera gráficos e dashboard financeiro. |
| **gerar_pdf.py** | Exporta um relatório financeiro em PDF. |

---

# 📊 Recursos

O projeto permite:

- 📄 Criação automática de planilhas Excel
- 💰 Controle financeiro
- 📈 Cálculo automático de lucro
- 📊 Dashboard financeiro
- 📉 Gráficos de desempenho
- 📑 Exportação de relatórios em PDF

---

# 🧰 Tecnologias Utilizadas

- Python
- OpenPyXL
- Pandas
- Matplotlib
- ReportLab

---

# 🎯 Objetivo

O projeto foi desenvolvido para automatizar tarefas financeiras de uma confeitaria, reduzindo erros em controles manuais e proporcionando uma visão clara dos resultados financeiros através de planilhas, dashboards e relatórios.

Além disso, demonstra a utilização prática do Python para automação de processos administrativos e análise de dados.

---

# 👩‍💻 Desenvolvedora

**Emanuelly Rackel**

---

# 📄 Licença

Este projeto foi desenvolvido para fins de estudo, portfólio e demonstração de conhecimentos em automação com Python.