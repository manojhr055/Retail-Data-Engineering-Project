import pandas as pd

df = pd.read_excel("final_retail_dataset.xlsx")

print("===== SALES BY CATEGORY =====")
print(
    df.groupby("Category")["Sales"]
      .sum()
      .sort_values(ascending=False)
)

print("\n===== SALES BY REGION =====")
print(
    df.groupby("Region")["Sales"]
      .sum()
      .sort_values(ascending=False)
)

print("\n===== PAYMENT METHOD ANALYSIS =====")
print(
    df.groupby("PaymentMethod")["Sales"]
      .sum()
      .sort_values(ascending=False)
)

print("\n===== TOP 5 STORES =====")
print(
    df.groupby("StoreName")["Sales"]
      .sum()
      .sort_values(ascending=False)
      .head(5)
)