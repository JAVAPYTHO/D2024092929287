import pandas as pd
import re

file_path_appendix1 = r'pathToAppendix1.xlsx'
file_path_appendix2 = r'pathToAppendix2.xlsx'

output_path_appendix1 = r'PathToTheFile\Processed_Appendix_1.xlsx'
output_path_appendix2 = r'PathToTheFile\Processed_Appendix_2.xlsx'

def extract_numeric(value):
    if isinstance(value, str) and '-' in value:
        numbers = [float(num) for num in re.findall(r"\d+\.\d+|\d+", value)] 
        return sum(numbers) / len(numbers) if numbers else None  
    elif isinstance(value, str) and value.replace('.', '', 1).isdigit():
        return float(value)
    return value  

numeric_cols = ['Price (USD)', 'Total number of households', 'Greening rate', 
                'Floor area ratio', 'Property management fee（/m²/month USD）', 
                'above-ground parking fee（/month USD）', 'underground parking fee（/month USD）']
categorical_cols = ['Building type', 'property type']
geo_cols = ['citycode', 'adcode', 'lon', 'lat', 'X', 'Y']

def preprocess_data(file_path, output_path):
    data = pd.read_excel(file_path)
    
    for col in numeric_cols:
        if col in data.columns:  
            data[col] = data[col].apply(extract_numeric)  
            if pd.api.types.is_numeric_dtype(data[col]):  
                median_value = data[col].median()  
                data[col] = data[col].fillna(median_value)  
    for col in categorical_cols:
        if col in data.columns:  
            mode_value = data[col].mode()[0] if not data[col].mode().empty else 'Unknown'  
            data[col] = data[col].fillna(mode_value)  

    for col in geo_cols:
        if col in data.columns:
            if pd.api.types.is_numeric_dtype(data[col]):  
                median_value = data[col].median()  
                data[col] = data[col].fillna(median_value)  

    data.to_excel(output_path, index=False)  

preprocess_data(file_path_appendix1, output_path_appendix1)
preprocess_data(file_path_appendix2, output_path_appendix2)
