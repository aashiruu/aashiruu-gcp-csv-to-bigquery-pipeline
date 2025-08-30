
# Serverless CSV to BigQuery Pipeline on GCP

A completely serverless, event-driven data pipeline on Google Cloud Platform that automatically processes CSV files uploaded to Cloud Storage, transforms them, and loads them into BigQuery for analysis. This is a foundational pattern for building cost-effective, scalable ETL (Extract, Transform, Load) workflows without managing any servers.

## Architecture Overview

The pipeline is triggered automatically by a simple file upload, making it both powerful and easy to use.

1.  **Trigger:** A user (or system) uploads a CSV file to a designated Google Cloud Storage (GCS) bucket.
2.  **Event Capture:** The GCS bucket emits an event notification.
3.  **Processing & Transformation:** The event triggers a **Cloud Function** (2nd Gen).
4.  **Data Load:** The Cloud Function reads the CSV, performs validation/transformation, and streams the data into **BigQuery**.
5.  **Analysis:** The data is immediately available in BigQuery for querying and visualization.

   
## Features

*   **Fully Serverless:** No infrastructure to manage. Scales automatically with usage.
*   **Event-Driven:** Processing begins within seconds of a file being uploaded.
*   **Flexible Schema Handling:** The function can be modified to handle different CSV formats and perform data cleansing.
*   **Cost-Effective:** Pay only for the compute time and storage/query costs used.

## Quick Start

### Prerequisites

- A Google Cloud Project with billing enabled.
- The `gcloud` CLI installed and authenticated.
- Basic knowledge of Python and GCP services.

### 1. Enable Required APIs

Enable the necessary Google Cloud APIs:

```bash
gcloud services enable \
  cloudfunctions.googleapis.com \
  eventarc.googleapis.com \
  cloudbuild.googleapis.com \
  logging.googleapis.com \
  bigquery.googleapis.com \
  storage.googleapis.com
