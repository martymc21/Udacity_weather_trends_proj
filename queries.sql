/* This is the .sql file containing the queries used to extract the data used. */


SELECT *
FROM city_list
WHERE country like 'United States'


### Renaming the columns for joining
ALTER TABLE global_data RENAME COLUMN avg_temp to global_avg_temp;

ALTER TABLE city_data RENAME COLUMN avg_temp to city_avg_temp;


### Downloading the joined tables
SELECT global_data.year, global_data.global_avg_temp, city_avg_temp
FROM global_data INNER JOIN city_data
ON global_data.year=city_data.year
WHERE city like 'Austin';
### Saved as YearlyAvgTemp.csv
