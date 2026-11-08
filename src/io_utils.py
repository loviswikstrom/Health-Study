import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(42)

REQUIRED = [
    "id", "age", "sex", "height", "weight",
    "systolic_bp", "cholesterol", "smoker", "disease"
]

def load_data(path: str) -> pd.DataFrame:
    """
    Läser CSV-filen health_study_dataset
    """
    df = pd.read_csv("health_study_dataset.csv")
    missing = [c for c in REQUIRED if c not in df.columns] #för varje kolumn in så lägger vi in dom i missing
    if missing:
        raise ValueError(f"Missing columns: {missing}")
    return df
    