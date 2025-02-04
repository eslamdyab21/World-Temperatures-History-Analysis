import pandas as pd
import unittest
import os
from tasks_utils import load_knime_output_dfs
from tasks_utils import task1_avg_temp_by_country
from tasks_utils import task2_classify_temp
from tasks_utils import task3_diff_temp
from tasks_utils import task4_top5_diff_temp
from tasks_utils import task6_chart




class TestOrionTasks(unittest.TestCase):
    def __init__(self, methodName = "runOrionTests"):
        super().__init__(methodName)
        self.APPROACH = os.getenv("APPROACH", "approach1")

        self.city_df = pd.read_csv(f'city_data_{self.APPROACH}.csv')
        self.global_avg_temp_df = pd.read_csv('global_data_table.csv')

        self.knime_dfs = load_knime_output_dfs()


    def test_task1_avg_temp_by_country(self):
        expected_df = self.knime_dfs[self.APPROACH]['avg_temp_by_country']
        actual_df = task1_avg_temp_by_country(self.city_df)

        # ignore different column names
        expected_df.columns = [''] * len(expected_df.columns)
        actual_df.columns = [''] * len(actual_df.columns)


        pd.testing.assert_frame_equal(actual_df, expected_df)


    def test_task2_classify_temp(self):
        expected_df = self.knime_dfs[self.APPROACH]['classify_temp']
        actual_df = task2_classify_temp(self.city_df)

        # ignore different column names
        expected_df.columns = [''] * len(expected_df.columns)
        actual_df.columns = [''] * len(actual_df.columns)


        pd.testing.assert_frame_equal(actual_df, expected_df)

    
    def test_task3_diff_temp(self):
        expected_df = self.knime_dfs[self.APPROACH]['diff_temp']
        actual_df = task3_diff_temp(self.city_df, self.global_avg_temp_df)

        # ignore different column names
        expected_df.columns = [''] * len(expected_df.columns)
        actual_df.columns = [''] * len(actual_df.columns)


        pd.testing.assert_frame_equal(actual_df, expected_df)

    
    def test_task4_top5_diff_temp(self):
        expected_df = self.knime_dfs[self.APPROACH]['top5_diff_temp']
        actual_df = task4_top5_diff_temp(self.city_df, self.global_avg_temp_df)

        # ignore different column names
        expected_df.columns = [''] * len(expected_df.columns)
        actual_df.columns = [''] * len(actual_df.columns)


        pd.testing.assert_frame_equal(actual_df, expected_df)


    def test_task6_chart(self):
        expected_df = self.knime_dfs[self.APPROACH]['chart']
        actual_df = task6_chart(self.city_df, self.global_avg_temp_df)

        # ignore different column names
        expected_df.columns = [''] * len(expected_df.columns)
        actual_df.columns = [''] * len(actual_df.columns)


        pd.testing.assert_frame_equal(actual_df, expected_df)