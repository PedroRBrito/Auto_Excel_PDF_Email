import pandas as pd

class ExcelUtils:
    @staticmethod
    def ler_excel(caminho_arquivo, nome_planilha=None):
        try:
            df = pd.carregar_excel(caminho_arquivo, sheet_name=nome_planilha)
            return df
        except Exception as e:
            print(f"Erro ao ler o arquivo Excel: {e}")
            return pd.DataFrame()