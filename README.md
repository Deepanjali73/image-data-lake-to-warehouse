# Image Data Lake to Data Warehouse Solution

This repository contains the implementation of a Data Lake to Data Warehouse solution using Google Cloud Platform (GCP) UI. It processes raw image data, extracts metadata, and loads it into a structured data warehouse for analytics.

## Architecture
- **Google Cloud Storage**: Data lake for raw images.
- **Cloud Functions**: Metadata extraction on upload.
- **Cloud Composer**: ETL orchestration.
- **BigQuery**: Data warehouse.
- **Data Studio**: Reporting.

## Setup Instructions
1. **GCS Bucket**: Create `image-data-lake` in GCP Storage.
2. **Cloud Function**: Deploy `extract_metadata.py` with a GCS trigger.
3. **Cloud Composer**: Upload `image_etl_dag.py` to the DAGs folder.
4. **BigQuery**: Create `image_dataset` and run `schema.sql`.
5. **Data Studio**: Connect to BigQuery and create a report.

## Files
- `cloud_functions/extract_metadata.py`: Extracts metadata from uploaded images.
- `composer_dags/image_etl_dag.py`: ETL pipeline for loading data into BigQuery.
- `bigquery/schema.sql`: BigQuery table schema.
- `docs/solution_guide.md`: Detailed solution documentation.
- `sample_data/`: Sample images for testing.

## Demo
- Upload images from `sample_data/` to `image-data-lake/raw-images`.
- Verify metadata in `metadata/` folder.
- Trigger the ETL DAG in Composer.
- Check BigQuery and refresh Data Studio report.
