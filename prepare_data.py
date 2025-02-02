import pandas as pd
import logging


def approach_1(df, output_fname):
    # drop null values (3.5%)
    df = df.dropna()

    # save new df
    df.to_csv(output_fname, index = False)


def approach_2(df, output_fname):
    # filter by year
    df = df[df['year'] >= 1882]

    # drop null values (0.087%)
    df = df.dropna()

    # save new df
    df.to_csv(output_fname, index = False)



if __name__ == "__main__":
    logging.basicConfig(level = "INFO")

    # read dataframe
    logging.info(f"Reading city_data_table.csv....")
    city_df = pd.read_csv("city_data_table.csv")


    # Approach 1
    logging.info(f"Approach 1....")

    output_fname = 'city_data_approach1.csv'
    approach_1(df = city_df, output_fname = output_fname)

    logging.info(f"Saved {output_fname}")
    logging.info(f"Approach 1 is done")


    # Approach 2
    logging.info(f"Approach 2....")
    
    output_fname = 'city_data_approach2.csv'
    approach_2(df = city_df, output_fname = output_fname)

    logging.info(f"Saved {output_fname}")
    logging.info(f"Approach 2 is done")