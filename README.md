# RAG Mutation Testing

Projeto experimental para avaliar a eficácia de testes em sistemas baseados em **RAG (Retrieval-Augmented Generation)** utilizando **Mutation Testing**.

A ideia é criar diferentes mutações no funcionamento do sistema RAG e verificar se os testes conseguem detectar essas alterações.

O projeto utiliza o **Gemini** para geração das respostas e **Sentence Transformers** para geração local dos embeddings.

---

## Requisitos

- Python 3.10 ou superior
- Git
- Chave da API do Gemini

---

## Instalação

### 1. Clonar o projeto

```bash
git clone https://github.com/JoseFortunato90/RAG-Mutation-Test.git
cd "RAG Mutation Testing"
```

### 2. Criar a Virtual Environment

#### Linux

Crie a Virtual Environment:

```bash
python3 -m venv venv
```

Ative a Virtual Environment:

```bash
source venv/bin/activate
```

#### Windows

Crie a Virtual Environment:

```cmd
python -m venv venv
```

No CMD:

```cmd
venv\Scripts\activate
```

No PowerShell:

```powershell
venv\Scripts\Activate.ps1
```

### 3. Instalar as dependências

Com a Virtual Environment ativada, execute:

```bash
pip install -r requirements.txt
```

### 4. Configurar a API do Gemini

Crie um arquivo chamado `.env` na raiz do projeto:

```env
GEMINI_API_KEY=sua_chave_aqui
```

### 5. Adicionar o documento

Crie uma pasta chamada `data` na raiz do projeto:

```bash
mkdir data
```

Coloque um arquivo PDF dentro dela com o nome:

```text
document.pdf
```

A estrutura do projeto deverá ficar assim:

```text
RAG Mutation Testing/
│
├── data/
│   └── document.pdf
│
├── rag.py
├── mutantes.py
├── tests.py
├── run.py
├── requirements.txt
├── .env
└── README.md
```

### 6. Executar o projeto

Com a Virtual Environment ativada:

```bash
python run.py
```

O sistema irá executar os mutantes definidos no projeto e verificar se os testes conseguem detectar as alterações.

---

## Mutation Testing

**Mutation Testing** é uma técnica utilizada para avaliar a qualidade de uma suíte de testes.

A ideia é criar pequenas alterações intencionais no sistema, chamadas de **mutações**, e verificar se os testes conseguem detectar essas alterações.

Neste projeto, a técnica é aplicada a um sistema **RAG**.

Algumas mutações utilizadas podem envolver:

- Alteração do tamanho dos chunks;
- Alteração do `chunk_overlap`;
- Alteração do `top_k`;
- Alteração dos documentos recuperados;
- Remoção de documentos relevantes;
- Alterações no processo de recuperação de informações.

---

## RAG

**RAG (Retrieval-Augmented Generation)** combina recuperação de informações com modelos de linguagem.

O funcionamento básico do projeto é:

```text
PDF
 ↓
Divisão em chunks
 ↓
Geração dos embeddings
 ↓
Armazenamento no Chroma
 ↓
Recuperação dos documentos relevantes
 ↓
Gemini
 ↓
Resposta
```

Os embeddings são gerados localmente utilizando **Sentence Transformers**, enquanto o **Gemini** é utilizado para gerar a resposta final.

---

## Mutation Score

O projeto pode utilizar o **Mutation Score** para medir a eficácia dos testes.

A fórmula é:

```text
Mutation Score = (Mutações detectadas / Total de mutações) × 100
```

Por exemplo, se existirem 10 mutações e os testes detectarem 8:

```text
Mutation Score = (8 / 10) × 100 = 80%
```

Quanto maior o Mutation Score, maior é a capacidade da suíte de testes de detectar alterações no sistema.

---

## Estrutura do projeto

```text
RAG Mutation Testing/
│
├── data/
│   └── document.pdf
│
├── rag.py
│   └── Implementação do sistema RAG
│
├── mutantes.py
│   └── Definição das mutações
│
├── tests.py
│   └── Testes utilizados para avaliar o RAG
│
├── run.py
│   └── Execução dos mutantes e testes
│
├── requirements.txt
│   └── Dependências do projeto
│
├── .env
│   └── Chave da API do Gemini
│
└── README.md
    └── Documentação do projeto
```

---

## Observações

Na primeira execução, o **Sentence Transformers** poderá baixar o modelo de embeddings utilizado pelo projeto.

Esse download ocorre apenas na primeira utilização. Depois disso, o modelo ficará armazenado localmente.

Também é necessário possuir uma chave válida da API do Gemini para utilizar o modelo de geração de respostas.

---

## Objetivo

O objetivo deste projeto é investigar a aplicação de **Mutation Testing em sistemas RAG**, verificando se uma suíte de testes é capaz de detectar alterações que podem comprometer o comportamento do sistema.

O projeto serve como um protótipo para experimentação e avaliação de diferentes estratégias de teste para sistemas baseados em Inteligência Artificial.
