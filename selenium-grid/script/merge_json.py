import pandas as pd
from datetime import datetime
from pathlib import Path

def process_json_to_csv(input_directory, output_directory):
 
    json_files = sorted(Path(input_directory).glob('*.json'))

    dataframes = []

    for file_ in json_files:
        df = pd.read_json(file_)
        df['airline_id'] = file_.name[:2]
        df['aircraft_registration'] = file_.name[3:9]
        dataframes.append(df)

    df_all = pd.concat(dataframes)
    currentDateTime = datetime.today().strftime("%m-%d-%Y")
    
    output_file = Path(output_directory) / f"flight_history_{currentDateTime}.csv"
    df_all.to_csv(output_file, index=False)
    
    print(f"File CSV berhasil disimpan di {output_file}")

