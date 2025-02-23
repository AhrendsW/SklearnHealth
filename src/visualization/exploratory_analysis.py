"""
Script para análise exploratória dos dados de saúde.

Este módulo é responsável por:
1. Carregar os dados brutos
2. Realizar análise estatística descritiva
3. Gerar visualizações relevantes
4. Salvar os resultados da análise
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import logging
import os

# Configuração do logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Configuração dos diretórios
BASE_DIR = Path(__file__).resolve().parent.parent.parent
RAW_DATA_PATH = BASE_DIR / 'data' / 'raw' / 'dados_saude.csv'
FIGURES_DIR = BASE_DIR / 'reports' / 'figures'

# Configuração do estilo dos gráficos
sns.set_theme(style="whitegrid")
sns.set_palette("husl")

def carregar_dados():
    """
    Carrega os dados brutos e realiza limpeza básica dos nomes das colunas.
    
    Returns:
        pd.DataFrame: DataFrame com os dados limpos
    """
    logger.info("Carregando dados brutos...")
    
    # Definindo tipos de dados para evitar warnings de tipos mistos
    dtype_dict = {
        'coluna_12': str,  # Ajustando para string para evitar tipos mistos
        'coluna_13': str   # Ajustando para string para evitar tipos mistos
    }
    
    df = pd.read_csv(RAW_DATA_PATH, low_memory=False, dtype=dtype_dict, sep=',')
    
    # Padronização dos nomes das colunas conforme regras do projeto
    df.columns = df.columns.str.lower().str.replace(' ', '_')
    
    logger.info(f"Dados carregados com sucesso. Shape: {df.shape}")
    return df

def analise_estatistica_descritiva(df):
    """
    Realiza análise estatística descritiva dos dados.
    
    Args:
        df (pd.DataFrame): DataFrame com os dados
    
    Returns:
        dict: Dicionário com diferentes análises estatísticas
    """
    logger.info("Realizando análise estatística descritiva...")
    
    analise = {
        'descricao_numerica': df.describe(),
        'info_tipos': df.dtypes,
        'valores_nulos': df.isnull().sum(),
        'contagens_categoricas': {col: df[col].value_counts() 
                                for col in df.select_dtypes(include=['object']).columns}
    }
    
    return analise

def criar_visualizacoes(df):
    """
    Cria visualizações dos dados e salva em arquivos.
    
    Args:
        df (pd.DataFrame): DataFrame com os dados
    """
    logger.info("Gerando visualizações...")
    
    # Criar diretório para as figuras se não existir
    FIGURES_DIR.mkdir(parents=True, exist_ok=True)
    
    # 1. Mapa de correlação para variáveis numéricas
    plt.figure(figsize=(12, 8))
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
    sns.heatmap(df[numeric_cols].corr(), annot=True, cmap='coolwarm', center=0)
    plt.title('Mapa de Correlação - Variáveis Numéricas')
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / 'correlacao.png')
    plt.close()
    
    # 2. Distribuição das variáveis numéricas
    for col in numeric_cols:
        plt.figure(figsize=(10, 6))
        sns.histplot(data=df, x=col, kde=True)
        plt.title(f'Distribuição - {col}')
        plt.tight_layout()
        plt.savefig(FIGURES_DIR / f'distribuicao_{col}.png')
        plt.close()
    
    # 3. Contagem de valores para variáveis categóricas
    categorical_cols = df.select_dtypes(include=['object']).columns
    for col in categorical_cols:
        plt.figure(figsize=(12, 6))
        sns.countplot(data=df, y=col, order=df[col].value_counts().index[:20])
        plt.title(f'Contagem - {col}')
        plt.tight_layout()
        plt.savefig(FIGURES_DIR / f'contagem_{col}.png')
        plt.close()

def gerar_relatorio_analise(df, analise_estatistica):
    """
    Gera um relatório em texto com os principais insights da análise e exibe no terminal.
    
    Args:
        df (pd.DataFrame): DataFrame com os dados
        analise_estatistica (dict): Resultado da análise estatística
    """
    logger.info("Gerando relatório de análise...")
    
    report_path = BASE_DIR / 'reports' / 'analise_exploratoria.txt'
    report_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Criando o conteúdo do relatório
    relatorio = []
    relatorio.append("RELATÓRIO DE ANÁLISE EXPLORATÓRIA")
    relatorio.append("=" * 50 + "\n")
    
    relatorio.append("1. VISÃO GERAL DOS DADOS")
    relatorio.append(f"- Número de registros: {df.shape[0]}")
    relatorio.append(f"- Número de características: {df.shape[1]}")
    relatorio.append(f"- Colunas: {', '.join(df.columns)}\n")
    
    relatorio.append("2. ANÁLISE DE VALORES NULOS")
    relatorio.append(analise_estatistica['valores_nulos'].to_string())
    relatorio.append("\n")
    
    relatorio.append("3. ESTATÍSTICAS DESCRITIVAS")
    relatorio.append(analise_estatistica['descricao_numerica'].to_string())
    relatorio.append("\n")
    
    # Salvando no arquivo
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write("\n".join(relatorio))
    
    # Exibindo no terminal
    logger.info("=== RESUMO DA ANÁLISE EXPLORATÓRIA ===")
    print("\n".join(relatorio))
    logger.info(f"Relatório completo salvo em: {report_path}")

def main():
    """Função principal que executa toda a análise exploratória."""
    logger.info("Iniciando análise exploratória...")
    
    # Carregar dados
    df = carregar_dados()
    
    # Realizar análise estatística
    analise_estatistica = analise_estatistica_descritiva(df)
    
    # Gerar visualizações
    criar_visualizacoes(df)
    
    # Gerar relatório
    gerar_relatorio_analise(df, analise_estatistica)
    
    logger.info("Análise exploratória concluída com sucesso!")

if __name__ == '__main__':
    main() 