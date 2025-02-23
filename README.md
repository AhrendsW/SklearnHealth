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
├── reports/         # Relatórios gerados
│   ├── figures/     # Visualizações e gráficos
│   └── *.txt        # Relatórios em texto
├── main.py          # Script principal do projeto
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

## Executando o Projeto

Para executar o pipeline completo do projeto, simplesmente rode:

```bash
python main.py
```

Este comando irá:
1. Baixar os dados necessários
2. Realizar análise exploratória
3. Gerar visualizações e relatórios
4. (Futuro) Treinar e avaliar modelos

Os resultados serão salvos em:
- `reports/figures/`: Visualizações e gráficos
- `reports/analise_exploratoria.txt`: Relatório detalhado da análise
- `pipeline.log`: Log de execução do pipeline

## Tecnologias Utilizadas

- Python 3.8+
- scikit-learn
- pandas
- numpy
- matplotlib
- seaborn
- requests
