# Orion360-Technical-Test
In this repo I'm going to solve the technical task of **Orion Digital solutions**.

Before we start answering the task analytical questions let's first explore the dataset and make sure we understand the data.

The dataset represents the history of temperatures of the world in around 270 years.

<br/>

## Exploring The Dataset
We have `71311` records in the `city_data_table.csv` where `2547` of which are null values with a presentage of about `3.5%`.

![](images/nulls.png)

We have gaps of missing values from 1 to up to 85 gap in `Port Louis` city in `Mauritius`.

<br/>

We have a number of approaches to handle this missing data:
1. Simply dropping the null values.
2. Filling the null values:
	1. With zeros.
	2. With mean.
	3. With city-wise mean.
	4. With Interpolation

<br/>

Let's farther investigate the dataset years, eventually we will do analytics based on the years, so let's make sure they all have the same years to aggregate on.

![](images/investigate1.png)
![](images/investigate2.png)
As we can see not all cities have records starting from the same `start_date` `(std is 42 in start_year)` but all of them end with the same `end_date` `2013` `(std is 0 in end_year)`.

- All cities have data until `2013`
- The oldest data starts in `1743` and the most recent city's data starts in `1882`
- Cities have between `132` and `271` years of recorded temperature data.
- Most cities have around `190–206` years of data.


To have the same ground-truth base data for all cities and countries to compare them against each other, we can filter the dataset with the start date as `1882` 
![](images/investigate3.png)
![](images/investigate4.png)

<br/>

### Conclusion on handling the null values and start date
We have a number of options here:
1. Drop the `3.5%` null records from the original `71311` records of data and continue the analysis with that, we are left with `96.5%` of the original data here.
2. Filter the original data with either start date as `1841` resulting in about `80%` of the original data, or  filtering with start date as `1882` to have the same years for all cities and counties for best accurate comparison, this will result in about `63.5%` of the original data.

We will go with the following two approaches and compare the results at the end:
1. Drop the `3.5%` null records (this option minimizes the data loss), dropping this `3.5%` null records verses filling them with whatever approach we mentioned above won't make mush of a difference here, so will go with the easier approach.
2. Filter the original data with start date as `1882` (this option same ground-truth base of comparison)

<br/>

A python script `prepare_data.py` is written to output two csv files for the two approaches to be used in analytics with  `KNIME`
```bash
(orion) Orion360-Technical-Test$ python3 prepare_data.py 
INFO:root:Reading city_data_table.csv....
INFO:root:Approach 1....
INFO:root:Saved city_data_approach1.csv
INFO:root:Approach 1 is done
INFO:root:Approach 2....
INFO:root:Saved city_data_approach2.csv
INFO:root:Approach 2 is done


(orion) Orion360-Technical-Test$ ls
city_data_approach1.csv  city_data_table.csv    global_data_table.csv  orion            README.md
city_data_approach2.csv  explor_datasets.ipynb  images                 prepare_data.py
```

