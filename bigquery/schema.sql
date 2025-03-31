CREATE TABLE `image_dataset.image_metadata`
(
    image_id STRING,
    upload_timestamp TIMESTAMP,
    image_format STRING,
    size INTEGER,
    category STRING
)
PARTITION BY DATE(upload_timestamp)
CLUSTER BY category
OPTIONS (
    description="Table storing metadata for images uploaded to the data lake"
);
