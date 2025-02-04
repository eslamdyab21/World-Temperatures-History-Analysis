import pandas as pd
import os



def task1_avg_temp_by_country(df):
    avg_temp_by_country_df = df.groupby(["country"])['avg_temp'].agg(avg_temp_by_country = 'mean').reset_index()
    
    return avg_temp_by_country_df



def task2_classify_temp(df):
    min_temp = df['avg_temp'].min()
    max_temp = df['avg_temp'].max()
    
    # Define thresholds
    low_threshold = min_temp + (max_temp - min_temp) / 3
    mid_threshold = min_temp + 2 * (max_temp - min_temp) / 3
    
    # Classification function
    def classify(temp):
        if temp <= low_threshold:
            return "Low"
        elif temp <= mid_threshold:
            return "Mid"
        else:
            return "High"
    
    df["avg_temp_binned"] = df['avg_temp'].apply(classify)
    
    return df



def load_knime_output_dfs():
    base_dir = "knime-csv-output"
    knime_dfs = {'approach1':{}, 'approach2':{}}

    for subdir in os.listdir(base_dir):
        subdir_path = os.path.join(base_dir, subdir)
        
        if os.path.isdir(subdir_path):
            for file in os.listdir(subdir_path):
                if file.endswith(".csv"):  
                    key = file.split('.')[0]
                    file_path = os.path.join(subdir_path, file)
                    knime_dfs[subdir][key] = pd.read_csv(file_path)
    
    return knime_dfs