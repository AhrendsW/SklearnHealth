"""
Script principal para execução do pipeline completo de análise e modelagem.

Este script orquestra todas as etapas do projeto:
1. Download dos dados
2. Análise exploratória
3. Pré-processamento
4. Treinamento do modelo
5. Avaliação do modelo
"""

import logging
from pathlib import Path
import sys
import time

# Adiciona o diretório src ao PYTHONPATH
sys.path.append(str(Path(__file__).resolve().parent))

# Importa os módulos do projeto
from src.data.download_data import main as download_data
from src.visualization.exploratory_analysis import main as analyze_data

# Configuração do logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('pipeline.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

def executar_pipeline():
    """
    Executa o pipeline completo do projeto em sequência.
    """
    inicio = time.time()
    logger.info("Iniciando pipeline completo do projeto...")

    try:
        # Etapa 1: Download dos dados
        logger.info("Etapa 1: Download dos dados")
        download_data()

        # Etapa 2: Análise exploratória
        logger.info("Etapa 2: Análise exploratória")
        analyze_data()

        # As próximas etapas serão implementadas conforme desenvolvimento
        # Etapa 3: Pré-processamento (a ser implementado)
        # Etapa 4: Treinamento do modelo (a ser implementado)
        # Etapa 5: Avaliação do modelo (a ser implementado)

        fim = time.time()
        tempo_total = fim - inicio
        logger.info(f"Pipeline concluído com sucesso! Tempo total: {tempo_total:.2f} segundos")

    except Exception as e:
        logger.error(f"Erro durante a execução do pipeline: {str(e)}")
        raise

def main():
    """Função principal do projeto."""
    try:
        executar_pipeline()
    except Exception as e:
        logger.error(f"Erro fatal na execução do projeto: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main() 