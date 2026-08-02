output "bucket_name" {

  value = google_storage_bucket.raw_bucket.name

}

output "dataset_name" {

  value = google_bigquery_dataset.staged_dataset.dataset_id

}

output "bucket_url" {

  value = google_storage_bucket.raw_bucket.url

}