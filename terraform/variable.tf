variable "region" {
  description = "aws region"
  default     = "us-east-2"
}

variable "account_id" {
  default = 654654318164
}

variable "prefix" {
  description = "objects prefix"
  default     = "tcc"
}

# Prefix configuration and project common tags
locals {
  glue_bucket = "${var.prefix}-${var.bucket_names[6]}-${var.account_id}"
  prefix      = var.prefix
  common_tags = {
    Project = "trn-cc-bg-aws"
  }
}

variable "bucket_names" {
  description = "s3 bucket names"
  type        = list(string)
  default = [
    "landing-zone-s3",
    "domain-bronze-s3",
    "domain-silver-s3",
    "domain-gold-s3",
    "processing-zone-s3",
    "consumer-zone-s3",
    "aws-glue-scripts"
  ]
}

variable "glue_job_role_arn" {
  description = "The ARN of the IAM role associated with this job."
  default     = null
}