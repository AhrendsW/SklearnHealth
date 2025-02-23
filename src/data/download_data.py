"""
Script para download e organização dos dados de saúde do healthdata.gov.

Este script é responsável por:
1. Fazer o download dos dados de saúde
2. Salvar os dados brutos em um diretório específico
3. Criar a estrutura de diretórios necessária
"""

import os
import requests
from pathlib import Path
import logging

# Configuração do logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# URLs e caminhos
DATA_URL = 'https://healthdata.gov/api/views/879u-23sm/rows.csv?fourfour=879u-23sm&cacheBust=1739963846&date=20250222&accessType=DOWNLOAD'
BASE_DIR = Path(__file__).resolve().parent.parent.parent
RAW_DATA_DIR = BASE_DIR / 'data' / 'raw'
PROCESSED_DATA_DIR = BASE_DIR / 'data' / 'processed'

def criar_estrutura_diretorios():
    """Cria a estrutura de diretórios necessária para o projeto."""
    diretorios = [RAW_DATA_DIR, PROCESSED_DATA_DIR]
    
    for diretorio in diretorios:
        diretorio.mkdir(parents=True, exist_ok=True)
        logger.info(f'Diretório criado/verificado: {diretorio}')

def baixar_dados():
    """
    Realiza o download dos dados de saúde e salva no diretório de dados brutos.
    
    Returns:
        Path: Caminho do arquivo baixado
    """
    arquivo_saida = RAW_DATA_DIR / 'dados_saude.csv'
    
    if arquivo_saida.exists():
        logger.info('Arquivo já existe. Pulando download.')
        return arquivo_saida
    
    logger.info('Iniciando download dos dados...')
    try:
        response = requests.get(DATA_URL, stream=True)
        response.raise_for_status()
        
        with open(arquivo_saida, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        
        logger.info(f'Download concluído. Arquivo salvo em: {arquivo_saida}')
        return arquivo_saida
    
    except Exception as e:
        logger.error(f'Erro ao baixar os dados: {str(e)}')
        raise

def main():
    """Função principal que executa o processo de download e organização dos dados."""
    logger.info('Iniciando processo de download e organização dos dados')
    
    # Criar estrutura de diretórios
    criar_estrutura_diretorios()
    
    # Baixar dados
    arquivo_dados = baixar_dados()
    
    logger.info('Processo concluído com sucesso!')
    return arquivo_dados

if __name__ == '__main__':
    main() 