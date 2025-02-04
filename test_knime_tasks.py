import pandas as pd
import unittest
from tasks_utils import load_knime_output_dfs
from tasks_utils import task1_avg_temp_by_country


class TestOrionTasks(unittest.TestCase):
    def __init__(self, methodName = "runOrionTests"):
        super().__init__(methodName)
        self.city_approach1_df  = pd.read_csv('city_data_approach1.csv')
        self.city_approach2_df  = pd.read_csv('city_data_approach2.csv')
        self.global_avg_temp_df = pd.read_csv('global_data_table.csv')

        self.knime_dfs = load_knime_output_dfs()


    def test_task1_avg_temp_by_country_approach1(self):
        expected_df = self.knime_dfs['approach1']['avg_temp_by_country']
        actual_df = task1_avg_temp_by_country(self.city_approach1_df)

        # ignore different column names
        expected_df.columns = [''] * len(expected_df.columns)
        actual_df.columns = [''] * len(actual_df.columns)


        pd.testing.assert_frame_equal(actual_df, expected_df)


    def test_task1_avg_temp_by_country_approach2(self):
        expected_df = self.knime_dfs['approach2']['avg_temp_by_country']
        actual_df = task1_avg_temp_by_country(self.city_approach2_df)

        # ignore different column names
        expected_df.columns = [''] * len(expected_df.columns)
        actual_df.columns = [''] * len(actual_df.columns)


        pd.testing.assert_frame_equal(actual_df, expected_df)