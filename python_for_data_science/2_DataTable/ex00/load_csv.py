import pandas as pd


def load(path: str) -> pd.DataFrame:
    """
    Load a CSV file into a pandas DataFrame and print its dimensions.

    Args:
        path: str - The path to the CSV file

    Returns:
        pd.DataFrame - The DataFrame containing the data from the CSV file
        None - If there's an error loading the file
    """
    try:
        df = pd.read_csv(path)
        print(f"Loading dataset of dimensions {df.shape}")
        return df
    except (FileNotFoundError, pd.errors.EmptyDataError,
            pd.errors.ParserError):
        return None
