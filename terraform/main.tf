############################################
# Google Cloud Storage Bucket (D0 Raw Landing)
############################################

resource "google_storage_bucket" "raw_bucket" {

  name     = var.bucket_name
  location = var.region

  storage_class = "STANDARD"

  uniform_bucket_level_access = true

  public_access_prevention = "enforced"

  force_destroy = false

  versioning {
    enabled = true
  }

  lifecycle_rule {
    action {
      type = "Delete"
    }

    condition {
      age = 365
    }
  }

  labels = {
    environment = "staging"
    project     = "habot"
  }
}

############################################
# BigQuery Dataset (D1 Staged / Enforced)
############################################

resource "google_bigquery_dataset" "staged_dataset" {

  dataset_id = var.dataset_name

  friendly_name = "D1 Staged Enforced"

  description = "BigQuery Dataset for staged validated data"

  location = "asia-south1"

  delete_contents_on_destroy = false

  labels = {
    environment = "staging"
    project     = "habot"
  }
}

############################################
# Storage Bucket IAM
############################################

resource "google_storage_bucket_iam_member" "bucket_admin" {

  bucket = google_storage_bucket.raw_bucket.name

  role = "roles/storage.objectAdmin"

  member = "serviceAccount:${var.service_account_email}"

}

############################################
# BigQuery Dataset IAM
############################################

resource "google_bigquery_dataset_iam_member" "dataset_editor" {

  dataset_id = google_bigquery_dataset.staged_dataset.dataset_id

  role = "roles/bigquery.dataEditor"

  member = "serviceAccount:${var.service_account_email}"

}