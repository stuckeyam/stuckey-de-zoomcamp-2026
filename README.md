# stuckey-de-zoomcamp-2026
This repo is for my work realted to the Data Engineering Zoomcamp program. 


## Module 1 - Docker, SQL, and Terraform

### Homework Code

- Question 1

`docker exec -it 12ab8028cc2a0ba50f7c59f7bbb8003aeeedcf3464607f51606f597ada24d8dc pip --version` 
12ab8028cc2a0ba50f7c59f7bbb8003aeeedcf3464607f51606f597ada24d8dc = Container ID

- Question 3
```
SELECT COUNT(*)
FROM green_taxi_trips
where trip_distance <= 1
AND lpep_pickup_datetime >= '2025-11-01' 
and lpep_pickup_datetime < '2025-12-01'
```
- Question 4

```
SELECT lpep_pickup_datetime::DATE AS trip_date
    , MAX(trip_distance)
FROM green_taxi_trips
WHERE trip_distance < 100
GROUP BY 1
ORDER BY 2 DESC
LIMIT 10
```

- Question 5
```
SELECT  z."Zone"
    , SUM(total_amount) AS zone_total_amount
FROM green_taxi_trips gtt
JOIN zones z ON gtt."PULocationID" = z."LocationID"
WHERE lpep_pickup_datetime::DATE = '2025-11-18'::DATE
GROUP BY 1
ORDER BY 2 DESC
LIMIT 10
```

- Question 6
```
SELECT do_z."Zone"
    , MAX(tip_amount) AS zone_total_amount
FROM green_taxi_trips gtt
JOIN zones pu_z ON gtt."PULocationID" = pu_z."LocationID"
JOIN zones do_z ON gtt."DOLocationID" = do_z."LocationID"
WHERE pu_z."Zone" = 'East Harlem North'
GROUP BY 1
ORDER BY 2 DESC
LIMIT 10
```

## Module 2 - Orchestration

### Homework 

- Question 3
```
SELECT count(1)
FROM `zoomcamp.yellow_tripdata`
WHERE filename like '%2020%'
```

- Question 4
```
SELECT count(1)
FROM `zoomcamp.green_tripdata`
WHERE filename like '%2020%'
```

- Question 5
```
SELECT count(1)
FROM `zoomcamp.yellow_tripdata_2021_03`;
```


## Module 3 - Data Warehousing & BigQuery

### Homework 

- Question 2
```
SELECT DISTINCT PULocationID 
FROM `de-zoomcamp-2026-485420.zoomcamp.external_yellow_tripdata`;

SELECT DISTINCT PULocationID 
FROM `de-zoomcamp-2026-485420.zoomcamp.yellow_tripdata_2024`;
```
- Question 3
```
SELECT PULocationID
FROM `de-zoomcamp-2026-485420.zoomcamp.yellow_tripdata_2024`;

SELECT PULocationID, DOLocationID
FROM `de-zoomcamp-2026-485420.zoomcamp.yellow_tripdata_2024`;
```
- Question 4
```    
SELECT COUNT(1)
FROM de-zoomcamp-2026-485420.zoomcamp.external_yellow_tripdata
WHERE fare_amount = 0
```
- Question 5
```
CREATE TABLE de-zoomcamp-2026-485420.zoomcamp.yellow_tripdata_2024_w_partions_clusters
PARTITION BY DATE(tpep_pickup_datetime)
CLUSTER BY VendorID AS ( 
    SELECT * 
    FROM de-zoomcamp-2026-485420.zoomcamp.external_yellow_tripdata
)
```
- Question 6
```
SELECT DISTINCT VendorID
FROM de-zoomcamp-2026-485420.zoomcamp.yellow_tripdata_2024
WHERE DATE(tpep_dropoff_datetime) > DATE('2024-03-01')
    AND DATE(tpep_dropoff_datetime) < DATE('2024-03-16');

SELECT DISTINCT VendorID
FROM de-zoomcamp-2026-485420.zoomcamp.yellow_tripdata_2024_w_partions_clusters
WHERE DATE(tpep_dropoff_datetime) > DATE('2024-03-01')
    AND DATE(tpep_dropoff_datetime) < DATE('2024-03-16');
```