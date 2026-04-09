
import pandas as pd
from pathlib import Path

def load_price_data():
    
    project_root = Path(__file__).resolve().parent.parent
    data_path = project_root / "data" / "price_data.csv"

    
    data = pd.read_csv(
        data_path,
        index_col=0,
        parse_dates=True,
        date_format="%Y-%m-%d"
    )

    
    data = data.apply(pd.to_numeric, errors="coerce")
    data = data.dropna()

    return data

