# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# Nome do projeto

## Nome do grupo

## 👨‍🎓 Integrantes:

- <a href="https://www.linkedin.com/company/inova-fusca">Nome do integrante 1</a>
- <a href="https://www.linkedin.com/company/inova-fusca">Nome do integrante 2</a>
- <a href="https://www.linkedin.com/company/inova-fusca">Nome do integrante 3</a>
- <a href="https://www.linkedin.com/company/inova-fusca">Nome do integrante 4</a>
- <a href="https://www.linkedin.com/company/inova-fusca">Nome do integrante 5</a>

## 👩‍🏫 Professores:

### Tutor(a)

- <a href="https://www.linkedin.com/company/inova-fusca">Nome do Tutor</a>

### Coordenador(a)

- <a href="https://www.linkedin.com/company/inova-fusca">Nome do Coordenador</a>

# HUM.A.N OPS – Human-Aware & Sustainable Operations

## ⭐ Guia Rápido para Avaliadores (3–5 minutos)

Caso possua pouco tempo, avalie nesta ordem:

1. **🎥 Vídeo da Demonstração (YouTube – não listado)**

   - _Cole o link aqui_

2. **📊 MVP Funcional**

   - Bot Copiloto executando check-ins e comandos de produtividade
   - Dashboard Streamlit com abas: Pessoas, Operações, Sustentabilidade, Inclusão
   - Modelos de IA funcionando: risco de estresse e anomalia de energia

3. **🧠 Arquitetura da Solução**

   - Diagramas C4 em `document/architecture/`
   - Fluxo completo: Bot/API → ML Engines → DB → Dashboard

4. **📁 Código Principal**

   - `src/api/main.py` – API FastAPI
   - `src/dashboard/app.py` – Dashboard Streamlit
   - `src/ml/*.py` – Modelos de Machine Learning
   - `scripts/init_db.py` – Inicialização do projeto

5. **📄 Documentação**
   - `document/MASTER_DOCUMENTATION.md`
   - `document/AI_SPECIFICATIONS.md`
   - `document/DASHBOARD_SPECIFICATIONS.md`

---

## 🎯 Visão Geral

O **HUM.A.N OPS** é um sistema inteligente projetado para tornar o ambiente de trabalho:

- **Mais humano**: monitoramento ético de bem-estar, fadiga e sobrecarga.
- **Mais produtivo**: automação de tarefas e assistente virtual.
- **Mais sustentável**: análise de consumo energético e uso consciente de recursos.
- **Mais inclusivo**: métricas de fairness e auditoria de dados.

A solução é composta por **quatro agentes inteligentes**:

---

### 🤖 Atena – Agente de Produtividade

- Sugere priorização de tarefas
- Cria relatórios automáticos
- Auxilia no fluxo de trabalho

### 🧠 Hygeia – Agente de Bem-Estar

- Realiza check-ins
- Reúne dados de motivação, cansaço e estresse
- Usa IA para prever risco de sobrecarga

### 🌍 Gaia – Agente Verde & Sustentável

- Analisa uso de energia
- Detecta anomalias com modelos de IA
- Fornece insights ambientais

### 🤝 Sophia – Agente Ético & Inclusivo

- Usa fairness analytics
- Compara taxas de aprovação entre grupos
- Exibe métricas acessíveis de diversidade

---

## 🧩 Arquitetura da Solução

- **Frontend:** Streamlit
- **Backend:** FastAPI
- **IA/ML:** scikit-learn
- **BD:** SQLite
- **R:** Quarto para relatórios
- **Infra:** Docker (opcional)

Fluxo:

1. Usuário interage com o **Bot Copiloto**
2. O Bot aciona a **API FastAPI**
3. A API grava/consulta dados no **SQLite**
4. Modelos de ML são executados (stress/energia)
5. O **Dashboard Streamlit** consome esses dados

---

## 🚀 Como Executar

### 1. Criar ambiente virtual

```bash
python -m venv .venv
.\.venv\Scripts\activate
```

### 2. Instalar dependências

```bash
pip install -r config/requirements.txt

```

### 3. Inicializar banco e IA

```bash
python scripts/init_db.py

```

### 4. Rodar API

```bash
uvicorn src.api.main:app --reload

Acesse:

http://127.0.0.1:8000/docs

http://127.0.0.1:8000/health

```

### 5. Rodar Dashboard

```bash
streamlit run src/dashboard/app.py


```

### 6. (Opcional) Simular energia

```bash
python src/data/simulator_energy.py



```

## 🧠 Modelos de IA

### 🔹 Hygeia – Risco de Estresse

- **Modelo:** Regressão Logística
- **Dados:** gerados sinteticamente
- **Input:** `[motivação, cansaço, estresse]`
- **Output:** probabilidade de risco

### 🔹 Gaia – Anomalia de Energia

- **Modelo:** Isolation Forest
- **Dados:** valores de kWh simulados
- **Output:** normal ou anômalo

---

## 📊 Dashboard Streamlit

**Abas:**

- 👤 **Pessoas** – check-ins, níveis de stress/motivação
- ⚙️ **Operações** – workload e produtividade
- 🌍 **Sustentabilidade** – consumo energético e picos
- 🤝 **Inclusão** – análises de fairness com dados simulados

---

## 📁 Estrutura de pastas

```bash
GS2/
├── assets/
├── config/
│   ├── db/
│   ├── docker/
│   └── requirements.txt
├── document/
│   ├── r_reports/
│   ├── architecture/
│   └── *.md
├── scripts/
│   └── init_db.py
├── src/
│   ├── api/
│   ├── bot/
│   ├── dashboard/
│   ├── data/
│   ├── ml/
│   └── core/
└── README.md
```

## 🎥 Vídeo de Demonstração

Cole aqui o link do YouTube (não listado).

## 🗃 Histórico de lançamentos

- ## 0.5.0 - XX/XX/2024
- ## 0.4.0 - XX/XX/2024
- ## 0.3.0 - XX/XX/2024
- ## 0.2.0 - XX/XX/2024
- ## 0.1.0 - XX/XX/2024

## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>
