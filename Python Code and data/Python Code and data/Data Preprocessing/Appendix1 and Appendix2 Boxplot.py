import pandas as pd
import matplotlib.pyplot as plt

file_path = r'pathToAppendix.xlsx'
excel_data = pd.ExcelFile(file_path)
df = excel_data.parse('Sheet1')

selected_df = df[['Price (USD)', 'Total number of households', 'Greening rate',
                  'Floor area ratio', 'Property management fee(/m²/month USD)',
                  'above-ground parking fee(/month USD)', 'underground parking fee(/month USD)']]
normalized_df = (selected_df - selected_df.min()) / (selected_df.max() - selected_df.min())

plt.figure(figsize=(10, 8))
boxprops = dict(facecolor="blue", color="blue", linewidth=1.5)  
medianprops = dict(color="red", linewidth=1.5) 
flierprops = dict(marker='o', markerfacecolor='black', markersize=4)  

normalized_df.boxplot(vert=False, patch_artist=True, boxprops=boxprops, 
                      medianprops=medianprops, flierprops=flierprops)
plt.xlabel("Normalized Value (0 to 1)")
plt.ylabel("Attributes")
plt.title("Normalized Box Plot of Selected Attributes2")

plt.show()