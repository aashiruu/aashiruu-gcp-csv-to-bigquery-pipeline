import functions_framework
from google.cloud import bigquery
from google.cloud import storage
import csv
import io
import logging

# Initialize clients
bq_client = bigquery.Client()
storage_client = storage.Client()

@functions_framework.cloud_event
def csv_to_bigquery(cloud_event):
    """Triggered by a new CSV file uploaded to GCS."""
    data = cloud_event.data

    # Get the bucket and file name from the event
    bucket_name = data['bucket']
    file_name = data['name']
    
    logging.info(f"New file detected: gs://{bucket_name}/{file_name}")

    # 1. Read the CSV file from GCS
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(file_name)
    csv_data = blob.download_as_text()

    # 2. Prepare the data for BigQuery
    csv_reader = csv.reader(io.StringIO(csv_data))
    next(csv_reader)  # Skip header row

    rows_to_insert = []
    for row in csv_reader:
        # Transform row if necessary
        rows_to_insert.append({"name": row[0], "age": int(row[1]), "city": row[2]})

    # 3. Insert rows into BigQuery
    table_id = "your-project-id.csv_ingestion.user_data"  # TODO: Replace with your full table ID
    errors = bq_client.insert_rows_json(table_id, rows_to_insert)

    if errors:
        logging.error(f"Encountered errors while inserting rows: {errors}")
        raise Exception(f"BigQuery insert errors: {errors}")
    else:
        logging.info(f"Successfully inserted {len(rows_to_insert)} rows from {file_name} into BigQuery.")
