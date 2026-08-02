# Habot Hiring Project – Architecture Overview

## Project Overview

This project demonstrates a secure cloud deployment architecture for a Django REST Framework backend using Infrastructure as Code (Terraform), an automated GitHub Actions CI/CD pipeline, and strict data validation.

The objective is to provision cloud resources securely, prevent insecure deployments, and validate incoming application data before it reaches the database.

---

# High-Level Architecture

                    Developer
                        │
                        ▼
              GitHub Repository
                        │
                Push / Pull Request
                        │
                        ▼
          GitHub Actions CI/CD Pipeline
                        │
      ┌─────────────────┼─────────────────┐
      │                 │                 │
      ▼                 ▼                 ▼
  Black Formatter    Flake8 Linter    Bandit Security Scan
      │                 │                 │
      └─────────────────┼─────────────────┘
                        │
                        ▼
              Detect Hardcoded Secrets
                        │
          ┌─────────────┴─────────────┐
          │                           │
      Validation Pass            Validation Fail
          │                           │
          ▼                           ▼
   Deployment Approved          Build Blocked
          │
          ▼
 Terraform Infrastructure
          │
          ├───────────────┐
          │               │
          ▼               ▼
Cloud Storage Bucket   BigQuery Dataset
          │               │
          └───────┬───────┘
                  ▼
          Django REST API
                  │
                  ▼
          Student JSON Payload
                  │
                  ▼
        Serializer Validation
                  │
          ┌───────┴────────┐
          │                │
      Valid Data      Invalid Data
          │                │
          ▼                ▼
      Save Record      Return Error

---

# Components

## 1. Terraform

Terraform provisions:

- Google Cloud Storage Bucket (Raw Landing Zone)
- BigQuery Dataset
- IAM Access Permissions
- Secure cloud infrastructure

---

## 2. GitHub Actions

The CI/CD pipeline automatically executes:

- Black
- Flake8
- Bandit
- Detect-Secrets
- Safety

If any validation fails, the deployment immediately stops.

---

## 3. Django REST Framework

The serializer validates:

- Required fields
- Email format
- Phone number
- Age limits
- Grade limits
- Parent consent
- Learning difficulty rules

Only validated data is accepted.

---

# Security Controls

- Least Privilege IAM
- Public Access Prevention
- Versioned Storage Bucket
- Static Code Analysis
- Secret Detection
- Dependency Vulnerability Scan
- Fail-Closed CI/CD Pipeline

---

# Data Flow

Student Form

↓

JSON Request

↓

Serializer Validation

↓

Business Rules

↓

Database

↓

BigQuery Analytics

---

# Folder Structure

Habot-Hiring-Project/

terraform/

.github/workflows/

django/

sample_data/

docs/

README.md

---

# Technologies Used

Terraform

Google Cloud Platform

GitHub Actions

Python

Django REST Framework

BigQuery

Cloud Storage

Git

YAML

---

# Outcome

This project demonstrates how Infrastructure as Code, CI/CD automation, and strict validation can be combined to build a secure, scalable, and maintainable cloud deployment workflow.