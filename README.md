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

### 2. 🧪 O que ver funcionando

- Chat Copiloto com **4 agentes**:
  - Hygeia (bem-estar)
  - Atena (produtividade)
  - Gaia (energia)
  - Sophia (fairness & inclusão)
  - Pandora (Inteligência Emocional)
- Hygeia:
  - Pergunta o **nome do colaborador**
  - Realiza **check-in com 5 perguntas**
  - Grava tudo no banco via API `/checkin`
  - Calcula **stress_score contínuo** com modelo de ML
- Dashboard Plotly Dash com abas:
  - 👤 Pessoas
  - ⚙️ Operações
  - 🌍 Sustentabilidade
  - 🤝 Inclusão

3. **🧠 Arquitetura da Solução**

   - Diagramas C4 em `document/architecture/`
   - Fluxo completo: Bot/API → ML Engines → DB → Dashboard

### 4. 📁 Código principal

- `src/api/main.py` – API FastAPI
- `src/bot/hygeiacheckin.py` – Hygeia (versão integrada)
- `src/core/orchestrator.py` – Roteamento de intents e agentes
- `src/dashboard/app_dash.py` – Dashboard em Plotly Dash
- `src/ml/stress_model.py` – Modelo contínuo de stress
- `src/ml/energy_anomaly.py` – Modelo de anomalia de energia
- `scripts/init_db.py` – Criação/configuração do banco

5. **📄 Documentação**
   - `document/MASTER_DOCUMENTATION.md`
   - `document/AI_SPECIFICATIONS.md`
   - `document/DASHBOARD_SPECIFICATIONS.md`

---

## 🎯 Visão Geral da Solução

O **HUM.A.N OPS** é uma plataforma para tornar operações de trabalho:

- **Mais humanas** – acompanhando bem-estar e evitando burnout
- **Mais produtivas** – com suporte à priorização e automações
- **Mais sustentáveis** – medindo e analisando consumo de energia
- **Mais inclusivas** – monitorando fairness e disparidades

A solução integra:

- IA (copiloto conversacional)
- Modelos clássicos de Machine Learning
- Banco de dados relacional (SQLite)
- Dashboard analítico (Plotly Dash)

---

### 🤖 Atena – Agente de Produtividade

- Sugere priorização de tarefas
- Cria relatórios automáticos
- Auxilia no fluxo de trabalho

## 🤖 Agentes do Copiloto

### 🧠 Hygeia – Bem-Estar (Hygeia 2.0)

- Pergunta o **nome** do colaborador na primeira interação
- Realiza check-in com **cinco perguntas** (escala 1–5):

  1. Sono
  2. Dor de cabeça
  3. Desempenho
  4. Carga de trabalho
  5. Stress percebido

- Envia os dados para a API `POST /checkin`
- A API:
  - resolve/cria o colaborador (`colaborador`)
  - grava as respostas na tabela `checkin`
  - calcula `stress_score` usando modelo de ML
- Hygeia devolve uma resposta empática baseada em:
  - `risk_score` (0 a 1)
  - `risk_level` (`baixo`, `moderado`, `alto`)

### 🌍 Gaia – Agente Verde & Sustentável

- Analisa uso de energia
- Detecta anomalias com modelos de IA
- Fornece insights ambientais

### 🤝 Sophia – Agente Ético & Inclusivo

- Usa fairness analytics
- Compara taxas de aprovação entre grupos
- Exibe métricas acessíveis de diversidade

### 🤖 Pandora – Agente de Conversação Emocional

A **Pandora** é o agente voltado para conversas naturais, expressão emocional, desabafos e apoio humano não-clínico.  
Diferente dos outros agentes que têm funções técnicas (Hygeia, Gaia, Sophia, Atena), Pandora é:

- Livre, empática e aberta para diálogo
- Focada em acolhimento emocional **sem diagnósticos clínicos**
- Ideal para conversas sobre sentimentos, pressões do trabalho, motivação e reflexões pessoais
- Pode ser ativada automaticamente quando o usuário usa palavras emocionalmente carregadas (ex.: “tô mal”, “ansioso”, “estressado”), _sem precisar de comando manual_

### 🌟 Características

- Mantém **um estado de conversa** (session) dentro do `orchestrator`
- Entra em modo "Pandora" quando identificada a intenção emocional
- Nos casos de risco, segue boas práticas de segurança emocional:
  - Incentiva buscar apoio profissional
  - Reforça que o usuário não está sozinho
  - Nunca oferece conselho clínico

---

## 🧩 Arquitetura da Solução

- **Frontend:** Streamlit
- **Backend:** FastAPI
- **IA/ML:** scikit-learn
- **BD:** SQLite
- **R:** Quarto para relatórios
- **Infra:** Docker (opcional)

## 🧩 Arquitetura da Solução

Fluxo principal:

```text
Usuário → Copiloto (chat) → Orchestrator → API FastAPI → SQLite
                                           ↑
                                        Modelos de IA
Dashboard Plotly/Dash  ←──────────────  Leitura do SQLite
```

## 🧠 Modelos de IA

### 💚 Hygeia – Agente de Bem-Estar (Check-in + IA)

A **Hygeia** é o agente responsável pelo bem-estar emocional e fisiológico no HUM.A.N OPS.  
Ela realiza check-ins estruturados com colaboradores, registra dados no banco e utiliza um modelo de IA para estimar níveis de estresse.

---

## 🔍 Como Hygeia funciona

Quando o usuário digita **checkin**, Hygeia inicia um fluxo guiado:

1. Pergunta **o nome do colaborador** (na primeira interação)
2. Solicita **cinco respostas**, cada uma com valores de 1 a 5:
   - Sono
   - Dor de cabeça
   - Desempenho
   - Carga de trabalho
   - Stress percebido
3. Envia tudo para a API `POST /checkin`
4. A API grava no banco e roda o modelo de IA
5. Hygeia retorna recomendações empáticas baseadas no risco detectado

Hygeia identifica automaticamente o colaborador e mantém estado da conversa  
(`awaiting_name`, `awaiting_scores` etc.) para permitir uma experiência natural e fluida.

---

## ✨ O que Hygeia registra no banco

Na tabela `checkin` são gravados:

- `id_colab` – chave do colaborador
- `dt` – data e hora
- `q1` a `q5` – respostas do check-in (1–5)
- `texto_opcional` – comentários adicionais
- `stress_score` – valor contínuo (0 a 1) gerado pelo modelo
- `risk_level` – classificação (`baixo`, `moderado`, `alto`)

Na tabela `colaborador` são gravados:

- `nm_colaborador` – nome informado no chat
- IDs são criados automaticamente quando necessário

---

## 🤖 IA por trás da Hygeia

O modelo usado pela Hygeia é um preditor de risco de estresse treinado com dados simulados.

**Arquivo do modelo:**  
`src/ml/stress_model.py`

**Modelo:**

- `RandomForestRegressor`

**Entradas do modelo:**

```python
[sono, dor_cabeca, desempenho, carga_trabalho, stress]
```

Cada item vai de **1 a 5**, representando intensidade ou qualidade.

**Saída:**

- `stress_score` entre **0.0 e 1.0**
- Classificação derivada:
  - `baixo` → score < 0.33
  - `moderado` → score < 0.66
  - `alto` → score ≥ 0.66

Esse score orienta as respostas da Hygeia, que são empáticas, não-clínicas e orientadas à atenção e autocuidado.

---

## 📡 API da Hygeia

Hygeia utiliza o endpoint:

`POST /checkin`

A API:

- Resolve ou cria automaticamente o colaborador
- Grava o check-in no banco SQLite
- Executa o modelo de IA
- Retorna:
  - `risk_score`
  - `risk_level`

A Hygeia então compõe a resposta final com base nesses valores.

---

## 📊 Dashboard – Aba Pessoas

A aba **Pessoas** no dashboard exibe todos os check-ins registrados pela Hygeia.

Inclui:

- Nome do colaborador
- Data da leitura
- Respostas individuais (sono, dor, desempenho, carga, stress)
- `stress_score` calculado
- Gráfico da evolução do stress ao longo do tempo

Tudo é atualizado automaticamente conforme novos check-ins são realizados no chat.

---

## 📁 Arquivos importantes da Hygeia

- `src/bot/hygeiacheckin.py` — fluxo completo do agente
- `src/core/orchestrator.py` — roteamento de mensagens para a Hygeia
- `src/api/main.py` — endpoint `/checkin`
- `src/ml/stress_model.py` — treinamento do modelo
- `models/stress_model.pkl` — modelo salvo
- `config/db/human_ops.db` — banco contendo colaboradores e check-ins

---

## 💬 Conclusão

Hygeia é o pilar humano do HUM.A.N OPS.  
Ela permite:

- Acompanhamento contínuo de bem-estar
- Registro estruturado das condições dos colaboradores
- Identificação precoce de sinais de sobrecarga
- Apoio empático e não-clínico
- Visualização completa no dashboard

É a conexão entre IA, saúde ocupacional e gestão inteligente de pessoas.

# 🤖 Pandora – NLU Emocional (versão RNN / Deep Learning)

Na versão atual, a Pandora não utiliza mais modelos tradicionais como TF-IDF + Regressão Logística.

Agora ela utiliza **Deep Learning** com redes neurais recorrentes (RNN / LSTM), que são mais adequadas para entender padrões em texto e linguagem natural.

---

## 🧠 Como a Pandora funciona agora

1. O usuário envia uma mensagem.
2. O texto é convertido em números usando o **Tokenizer**:

   - `models/pandora_tokenizer.pkl` (ou tokenizer.json)

3. O vetor numérico é passado para a **RNN LSTM**:

   - `models/pandora_rnn.h5`

4. O modelo retorna uma **classe (índice da intenção)**.
5. A Pandora recupera a resposta correspondente no `intents.json`.

Fluxo:
input text → tokenizer → sequência → LSTM → classe → resposta

## 🔧 Tecnologias Utilizadas

### 1) 🔠 **Tokenizer (Keras Tokenizer)**

Transforma palavras em inteiros.  
Exemplo:

- "me sinto sozinho" → [42, 5, 318]

O arquivo do tokenizer é carregado no runtime:

- `models/pandora_tokenizer.pkl`

---

### 2)🧬 **Modelo RNN LSTM (.h5)**

O modelo é treinado com:

- Embedding layer
- LSTM (ou GRU)
- Dense final com softmax para classificar a intenção

Arquivo:

- `models/pandora_rnn.h5`

### 3) **Arquivos de Modelo**

| Arquivo                        | Descrição                         |
| ------------------------------ | --------------------------------- |
| `models/pandora_tokenizer.pkl` | tokenizer                         |
| `models/pandora_rnn.h5`        | RNN                               |
| `intents.json`                 | Padrões e respostas pré-definidas |

---

## 🆘 Detecção de Crise (Safety Layer)

A Pandora possui uma lista de palavras-chave em português e inglês.  
Se detectado algo como:

- “quero me matar”
- “não aguento mais viver”
- “suicide”

Ela envia uma resposta **fixa**, segura e protocolar, sempre incluindo:

- aviso de que não é profissional
- orientação para buscar ajuda especializada
- número 188 (CVV)

## 🧠 Como funciona a predição

```python
seq = tokenizer.texts_to_sequences([text])
padded = pad_sequences(seq, maxlen=MAXLEN)
pred = model.predict(padded)
tag_index = pred.argmax()
tag = labels[tag_index]
resposta = random.choice(intents[tag]["responses"])
```

---

### 🧠 Como funciona

1. O usuário envia uma mensagem emocional/livre.
2. A Pandora:
   - verifica **palavras de crise**
   - classifica a intenção usando:
     ```
     tag, prob = predict_intent(text)
     ```
3. Se `prob < 0.15`, envia resposta empática neutra.
4. Se `prob ≥ 0.15`, escolhe uma resposta do `intents.json`.

---

# 🧠 Explicação do RNN / LSTM

### 🔍 O que é uma RNN?

Uma **Recurrent Neural Network (RNN)** é um tipo de rede neural que:

- processa texto de forma sequencial,
- lembra do que veio antes,
- consegue capturar dependências temporais.

Enquanto modelos tradicionais (TF-IDF + LR):

- tratam as palavras isoladamente,
- não possuem memória,
- só reconhecem padrões estáticos,

As RNNs:

- trabalham palavra por palavra,
- carregam um estado interno (memória),
- entendem contexto.

### 🔄 Como ela lê texto

Exemplo de frase:

"me sinto muito triste"

Tokenized:

[12, 98, 40, 78]

Processamento:

t1 → hidden
t2 → hidden
t3 → hidden
t4 → hidden → output class

O estado interno carrega a memória do que já foi lido.

### 🧩 Componentes básicos

- **Input**: sequência de tokens
- **Hidden state (hₜ)**: memória do que já foi visto
- **Output**: classificação ou previsão de próxima palavra

### 🔄 Funcionamento

A cada palavra:

$$h_t = f(W \cdot x_t + U \cdot h_{t-1})$$

Isso cria a memória recorrente.

### 🆘 Problema das RNNs

- sofrem com _vanishing gradient_
- dificuldade em capturar longas dependências
- lentas para treinar

Por isso surgiram:

- LSTM
- GRU
- Transformers (GPT, T5, BERT…)

E hoje **RNN = legado**, mostrado mais como base teórica.

---

# 🚀 Arquivo de Exemplo – _Versão Generativa da Pandora_

Aqui está um arquivo completo **pandora_generativa.py**, simples, seguro e sem custos, usando uma LLM local ou API (placeholder). Idealizado para substituir o RNN.

> **É safe**, não gera risco, e pode ser plugado quando você quiser testar uma Pandora generativa real.

```python
# src/bot/pandora_generativa.py
"""
Pandora Generativa (Protótipo)
Versão conceitual que usaria um modelo generativo para respostas empáticas.
Não usada no projeto por questões de custo de inferência.
"""

from typing import Optional

SAFETY_PREFIX = """
Você é a Pandora, uma IA empática.
Nunca dê conselhos médicos.
Nunca encoraje comportamentos de risco.
Se detectar crise, mostre esta mensagem:

💛 Sinto muito que você esteja se sentindo assim.
Eu não posso oferecer ajuda de emergência.
Por favor, ligue 188 (CVV) ou procure atendimento profissional imediatamente.
"""

CRISIS = [
    "me matar", "suicidio", "suicídio", "tirar minha vida",
    "não quero mais viver", "kill myself", "suicide", "want to die"
]


def is_crisis(text: str) -> bool:
    t = text.lower()
    return any(k in t for k in CRISIS)


def generate_with_llm(prompt: str) -> str:
    """
    Mock para chamada generativa.
    Aqui poderia entrar qualquer LLM:
    - OpenAI
    - HuggingFace
    - Mistral
    - Llama.cpp local
    - GPT4All
    """

    # EXEMPLO SIMBÓLICO
    # (retorna uma resposta fixa só para teste)
    return (
        "Compreendo. Parece que você está passando por algo importante. "
        "Se quiser, posso te ajudar a explorar seus sentimentos."
    )


def handle_pandora_generativa(user_id: str, text: str) -> str:
    # 1) Safety first
    if is_crisis(text):
        return (
            "💛 Sinto muito que você esteja se sentindo assim.\n\n"
            "Eu sou apenas um assistente virtual e **não posso oferecer ajuda de emergência**.\n"
            "No Brasil, ligue **188** (CVV)."
        )

    # 2) Monta prompt seguro
    prompt = SAFETY_PREFIX + "\nUsuário: " + text + "\nPandora:"

    # 3) Chama modelo generativo (placeholder)
    resposta = generate_with_llm(prompt)

    return resposta
```

### 📁 Arquivos importantes

- src/bot/pandora.py # motor de resposta
- src/ml/pandora_nlu.py # NLU, treinamento e predição
- models/pandora_tokenizer.pkl # tokenizador
- models/pandora_rnn.h5l# RNN
- intents.json # padrões e respostas

Pandora é baseada em **IA clássica**, não generativa:  
ela classifica intenções emocionais e responde com base em intents pré-definidos no `intents.json`. A ideia da Pandora é uma demonstração de como a IA pode ajudar na saúde mental, temos a intenção de transformá-la em generativa e um esboço pode ser visto em src/bot/pandora_generativa.py que não foi usada devido custos.

## 🌍 Gaia – Agente de Sustentabilidade e Energia

**Gaia** é o agente responsável por monitorar, analisar e identificar padrões anômalos no consumo de energia do ambiente corporativo.  
Ela combina:

- Banco de dados real (SQLite)
- Modelos de Machine Learning (Isolation Forest)
- Dados simulados ou reais
- Dashboard em Plotly Dash
- API FastAPI para consultas em tempo real

Gaia fornece insights sobre eficiência energética e possíveis falhas operacionais causadas por consumo indevido.

---

## ⚡ Objetivos da Gaia

- Monitorar consumo energético (kWh) ao longo do tempo
- Detectar picos suspeitos ou consumo fora do padrão
- Alertar o usuário quando houver **anomalia**
- Exibir no dashboard o histórico de consumo
- Integrar com sensores/ESP32 ou simuladores para geração contínua de dados

---

## 🧠 Como Gaia funciona internamente

### 1. **Coleta dos dados**

Gaia utiliza as leituras armazenadas no banco:

- Tabela: energia
- Colunas: dt, kwh, equipamento, local, cd_area

As leituras podem vir de:

- Dispositivos reais (ESP32)
- API externa
- Ou do simulador `simulator_energy.py`

---

### 2. **Modelo de IA – Anomalias de Energia**

**Arquivo:**

- src/ml/energy_anomaly.py

**Modelo usado:**

- `IsolationForest`
- Especializado em detecção de outliers

**Como é treinado**:

- Gera 300 amostras simuladas com consumo normal (≈0.5 kWh)
- Insere ~5% de picos artificiais (≈2.0 kWh)
- Mistura, treina e salva o modelo:

**Arquivo salvo:**

- models/energy_anomaly.pkl

**Uso na prática:**

```python
pred = ENERGY_MODEL.predict([[kwh]])
anomaly_flag = (pred[0] == -1)
```

- Se -1 → é anomalia
- Se 1 → normal

### 3. API FastAPI – Endpoint de Monitoramento

**Gaia opera através do endpoint:**

```bash
GET /energia/status

```

**Este endpoint:**

- Busca a última leitura de energia no banco

- Soma o consumo total do dia

- Roda o modelo IsolationForest

- Retorna algo assim:

```json
{
  "current_kwh": 0.52,
  "daily_total": 6.32,
  "anomaly_flag": false
}
```

**Em caso de pico, retorna:**

```json
{
  "current_kwh": 2.01,
  "daily_total": 8.45,
  "anomaly_flag": true
}
```

### 🌍 4. Dashboard – Aba “Sustentabilidade”

No dashboard (`app_dash.py`), a aba **Sustentabilidade** apresenta:

- Uma tabela com as últimas leituras de energia registradas no banco
- Um gráfico de linha mostrando a evolução histórica do consumo (kWh)
- Destaque visual para picos anômalos detectados pelo modelo
- Atualização dinâmica sempre que uma nova leitura entra no banco

O gráfico utiliza diretamente os dados da tabela `energia` no SQLite.  
A consulta básica usada internamente é semelhante a:

```sql
SELECT dt, kwh, equipamento, local
FROM energia
ORDER BY dt DESC
LIMIT 200;
```

Assim, qualquer nova leitura — seja vinda do simulador, sensores reais ou inserções manuais — aparece imediatamente no dashboard, permitindo análise em tempo real das condições energéticas.

### 🌱 5. Simulação de Dados (opcional, para testes)

O arquivo responsável pela simulação de consumo energético é:

`src/ml/simulator_energy.py`

Ele insere leituras automáticas na tabela `energia` do banco SQLite, funcionando como um sensor de energia virtual.

**Comportamento do simulador:**

- Consumo normal varia entre aproximadamente **0.4 e 0.5 kWh**
- Ocasionalmente são inseridos **picos artificiais** (cerca de +1.5 kWh)
- Pode rodar apenas uma inserção ou em **modo contínuo**, gerando leituras a cada 30 segundos

**Como executar:**

```python
python src/ml/simulator_energy.py

```

```python
python src/ml/simulator_energy.py loop
```

---

### 🔗 Fluxo completo da Gaia

A arquitetura completa da Gaia segue o fluxo:

Simulador ou Sensor Real  
→ Banco SQLite (armazenamento das leituras)  
→ API `/energia/status` (consulta do último registro)  
→ Modelo IsolationForest (detecção de anomalias)  
→ Dashboard – Aba Sustentabilidade  
→ Alertas de consumo, insights e visualização histórica

Esse pipeline permite monitoramento contínuo e reativo do consumo energético.

---

### 📁 Arquivos importantes da Gaia

- `src/ml/energy_anomaly.py` – Treino do modelo de detecção de anomalias
- `models/energy_anomaly.pkl` – Modelo treinado
- `src/ml/simulator_energy.py` – Gerador de leituras simuladas
- `src/api/main.py` – Endpoint `GET /energia/status`
- `src/dashboard/app_dash.py` – Aba Sustentabilidade do dashboard
- `config/db/human_ops.db` – Banco de dados com as leituras reais ou simuladas

---

### 🌍 Conclusão

A Gaia oferece uma visão automatizada e inteligente do consumo de energia.  
Seus benefícios incluem:

- Detecção precoce de picos anômalos
- Suporte direto a iniciativas de sustentabilidade
- Redução de custos por meio de análise preditiva
- Monitoramento contínuo em tempo real
- Fácil integração com sensores físicos (ex.: ESP32)

Gaia é um dos pilares do **HUM.A.N OPS** na esfera de sustentabilidade corporativa, conectando IA, banco de dados e visualização para uma gestão energética moderna e eficiente.

## 🧱 Stack Técnica

### **Linguagem**

- Python 3.10+

### **API**

- FastAPI
- Endpoints principais:
  - `POST /checkin` – usado pela Hygeia
  - `GET /energia/status` – usado pela Gaia

### **Dashboard**

- Plotly Dash
- Abas:
  - Pessoas
  - Operações
  - Sustentabilidade
  - Inclusão

### **IA / Machine Learning**

- `scikit-learn`

Modelos:

- **Hygeia:** `RandomForestRegressor`
- **Gaia:** `IsolationForest`
- **Pandora:** `LogisticRegression` (NLU + TF-IDF)

### **Banco de Dados**

- SQLite (`config/db/human_ops.db`)
- Tabelas:
  - `colaborador`
  - `checkin`
  - `energia`

### **Orquestração**

- `src/core/orchestrator.py`
- Responsável por enviar cada mensagem para o agente correto:
  - Hygeia (bem-estar)
  - Pandora (emoções)
  - Atena (produtividade)
  - Gaia (energia)
  - Sophia (fairness)

### **Bots**

Local: `src/bot/`

- `hygeiacheckin.py`
- `pandora.py`
- `atena.py`
- `gaia.py`
- `sophia.py`

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
python src/dashboard/app_dash.py


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
