# SklearnHealth

Projeto de Machine Learning para previsões médicas utilizando scikit-learn.

## Descrição

Este projeto tem como objetivo desenvolver modelos de machine learning para realizar previsões médicas com base em dados clínicos, utilizando a biblioteca scikit-learn.

## Estrutura do Projeto

```
SklearnHealth/
│
├── data/
│   ├── raw/          # Dados brutos baixados
│   └── processed/    # Dados processados para análise
│
├── src/
│   ├── data/         # Scripts para download e processamento de dados
│   ├── features/     # Scripts para engenharia de features
│   ├── models/       # Scripts para treinamento e avaliação de modelos
│   └── visualization/# Scripts para visualização de dados
│
├── models/           # Modelos treinados salvos
├── notebooks/        # Jupyter notebooks para análise exploratória
└── requirements.txt  # Dependências do projeto
```

## Configuração do Ambiente

1. Clone o repositório
2. Crie um ambiente virtual:
```bash
python -m venv .venv
```

3. Ative o ambiente virtual:
```bash
# Windows
.venv\Scripts\activate

# Linux/Mac
source .venv/bin/activate
```

4. Instale as dependências:
```bash
pip install -r requirements.txt
```

## Download dos Dados

Para baixar os dados do projeto, execute:

```bash
python src/data/download_data.py
```

## Tecnologias Utilizadas

- Python 3.8+
- scikit-learn
- pandas
- numpy
- matplotlib
- seaborn
- requests
