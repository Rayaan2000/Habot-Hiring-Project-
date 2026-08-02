variable "project_id" {
  description = "Google Cloud Project ID"
  type        = string
}

variable "region" {
  description = "Deployment Region"
  type        = string
  default     = "asia-south1"
}

variable "bucket_name" {
  description = "Raw Landing Storage Bucket"
  type        = string
}

variable "dataset_name" {
  description = "BigQuery Dataset"
  type        = string
  default     = "d1_staged_enforced"
}

variable "service_account_email" {
  description = "Service Account Email"
  type        = string
}