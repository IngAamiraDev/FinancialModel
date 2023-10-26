import pandas as pd
import os

def remove_existing_file(file):
    if os.path.exists(file):
        os.remove(file)
        print(f"Existing file removed: {file}")

def read_xlsx_and_clean(file_xlsx):
    data_xlsx = pd.read_excel(file_xlsx)
    data_xlsx = data_xlsx.applymap(lambda x: x.strip() if isinstance(x, str) else x)
    return data_xlsx

def save_as_csv(data_xlsx, file_csv):
    data_xlsx.to_csv(file_csv, index=False, sep=',', encoding='utf-8')
    print(f"CSV file created successfully at: {file_csv}")

def main():
    file_xlsx = './data/input/db.xlsx'
    file_csv = './data/output/data.csv'
    
    remove_existing_file(file_csv)
    
    data_xlsx = read_xlsx_and_clean(file_xlsx)
    
    save_as_csv(data_xlsx, file_csv)

if __name__ == "__main__":
    main()