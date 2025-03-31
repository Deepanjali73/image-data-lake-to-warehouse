# Solution Guide: Data Lake to Data Warehouse

## Architecture
- **GCS**: `image-data-lake` bucket stores raw images.
- **Cloud Functions**: `extract_metadata` extracts metadata on upload.
- **Data Catalog**: Tags metadata for discoverability.
- **Cloud Composer**: Runs `image_etl_dag.py` for ETL.
- **BigQuery**: `image_dataset.image_metadata` stores structured data.
- **Data Studio**: Visualizes analytics.

## Setup Steps
1. **GCS**: Create `image-data-lake`, upload images to `raw-images/`.
2. **Cloud Function**: Deploy `extract_metadata.py` with GCS trigger.
3. **Data Catalog**: Create `ImageMetadata` tag template.
4. **Composer**: Set up environment, upload `image_etl_dag.py`.
5. **BigQuery**: Create `image_dataset`, run `schema.sql`.
6. **Data Studio**: Connect to BigQuery, create charts (e.g., image types, trends).

## Choices
- **GCS**: Scalable storage for unstructured data.
- **Composer**: UI-managed ETL orchestration.
- **BigQuery**: Optimized for analytics with partitioning/clustering.

## Automation
- Cloud Function triggers on upload.
- Composer DAG runs hourly to process new metadata.

## Dashboard
- Pie chart: Image types.
- Bar chart: Categories.
- Line chart: Upload trends.
- Scorecard: Average size.
