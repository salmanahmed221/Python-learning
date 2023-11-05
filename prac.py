import pandas as pd
import pandera as pa

f7: pd.Series = pd.Series([1, 2, 3, 4, 5], index=["a", "b", "c", "d", "e"])
print(f7)
print("Applying sliding")
print(f7.at["d"])  # index location (label) extract one cell value and you can update it
