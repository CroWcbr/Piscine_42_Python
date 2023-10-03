import pandas as pd
from typing import Union


def load(file_path: str) -> Union[pd.DataFrame, None]:
    """ This function load a csv file."""
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print(f"Файл '{file_path}' не найден.")
        return None
    except Exception as e:
        print(f"Произошла ошибка при чтении файла CSV: {str(e)}")
        return None
