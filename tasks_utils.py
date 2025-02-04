import pandas as pd
import os



def task1_avg_temp_by_country(city_df):
    avg_temp_by_country_df = city_df.groupby(["country"])['avg_temp'].agg(avg_temp_by_country = 'mean').reset_index()
    
    return avg_temp_by_country_df



def task2_classify_temp(city_df):
    min_temp = city_df['avg_temp'].min()
    max_temp = city_df['avg_temp'].max()
    
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
    
    city_df["avg_temp_binned"] = city_df['avg_temp'].apply(classify)
    
    return city_df


def task3_diff_temp(city_df, global_avg_temp_df):
    # ------------- global_avg_temp_df -------------
    global_avg_temp_df = global_avg_temp_df.sort_values(by='year')
    
    # rolling window for previous 24 years
    global_avg_temp_df['avg_temp_24_years'] = global_avg_temp_df['avg_temp'].rolling(window=24, min_periods=1).mean()


    # ------------- city_df -------------
    city_df = city_df.groupby(["year","country"])['avg_temp'].agg(avg_temp_by_year_country = 'mean').reset_index()
    


    global_avg_temp_df.set_index('year', inplace=True)
    city_df.set_index('year', inplace=True)
    diff_df = city_df.join(global_avg_temp_df, on='year', how='inner').reset_index()

    diff_df['temp_diff'] = diff_df['avg_temp_24_years'] - diff_df['avg_temp_by_year_country']
    diff_df = diff_df.drop(columns=['avg_temp_24_years', 'avg_temp_by_year_country', 'avg_temp'])

    return diff_df



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