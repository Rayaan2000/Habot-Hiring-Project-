# Habot Hiring Project

## Junior Cloud & DevOps Engineer (GCP / Django / React)

---

# Project Description

This project was developed as part of the HabotConnect Hiring Project.

The solution demonstrates a secure cloud deployment architecture using Terraform, GitHub Actions, and Django REST Framework.

The project focuses on infrastructure automation, CI/CD validation, and strict schema validation.

---

# Objectives

- Provision secure cloud resources using Terraform
- Automate code quality checks using GitHub Actions
- Detect formatting, linting, and security issues
- Block insecure deployments
- Validate incoming student data using Django REST Framework

---

# Project Structure

```
Habot-Hiring-Project/

terraform/
    provider.tf
    variables.tf
    terraform.tfvars
    main.tf
    outputs.tf

.github/
    workflows/
        ci.yml

django/
    models.py
    serializers.py
    urls.py
    views.py

sample_data/
    student_payload.json

docs/
    architecture.md

README.md
```

---

# Technologies

- Terraform
- Google Cloud Platform
- GitHub Actions
- Python
- Django REST Framework
- BigQuery
- Google Cloud Storage
- YAML
- Git

---

# Terraform Resources

The Terraform configuration provisions:

- Google Cloud Storage Bucket
- BigQuery Dataset
- IAM Permissions
- Versioned Storage
- Public Access Prevention

---

# CI/CD Pipeline

The GitHub Actions workflow performs:

- Black Formatting Check
- Flake8 Linting
- Bandit Security Scan
- Detect-Secrets Scan
- Safety Dependency Scan

If any check fails, the pipeline immediately terminates.

---

# Django Validation

The serializer validates:

- Student Name
- Email
- Phone Number
- Age
- Grade
- Parent Consent
- Learning Difficulty Rules

Only valid requests are accepted.

---

# Security Features

- IAM Role-Based Access
- Public Bucket Protection
- Static Code Analysis
- Secret Detection
- Dependency Vulnerability Checks
- Fail-Closed Deployment Strategy

---

# Sample Workflow

Developer Push

↓

GitHub Repository

↓

GitHub Actions

↓

Validation

↓

Terraform Infrastructure

↓

Django API

↓

Validated Data

↓

BigQuery

---

# Deliverables

- Terraform Infrastructure
- GitHub Actions Workflow
- Django REST Framework Validation
- Architecture Documentation
- Sample JSON Payload

---


# Note

This project is a hiring assignment submission prepared for HabotConnect. It demonstrates Infrastructure as Code, CI/CD automation, cloud security practices, and backend validation logic. Cloud resources were defined using Terraform as required by the assignment.