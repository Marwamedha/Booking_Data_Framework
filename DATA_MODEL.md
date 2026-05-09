# Data Model

## Tables

### fact_rides
- ride_id
- ride_timestamp
- datetime_key
- payment_type_key
- location_zone_key
- passenger_count_key
- trip_distance_key
- fare_amount
- tip_amount
- total_amount
- distance_miles

### dim_datetime
- datetime_key
- ride_date
- ride_hour
- day_of_week
- month
- quarter
- year

### dim_payment_type
- payment_type_key
- payment_type

### dim_location_zone
- location_zone_key
- pickup_zone
- dropoff_zone
- region

### dim_passenger_count
- passenger_count_key
- passenger_count

### dim_trip_distance
- trip_distance_key
- distance_bucket
