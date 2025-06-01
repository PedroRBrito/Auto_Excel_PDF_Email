import pandas as pd

class ExcelUtils:
    @staticmethod
    def ler_excel(caminho_arquivo, nome_planilha=None):
        try:
            df = pd.read_excel(caminho_arquivo, sheet_name=nome_planilha or 0)
            return df
        except Exception as e:
            print(f"Erro ao ler o arquivo Excel: {e}")
            return pd.DataFrame()