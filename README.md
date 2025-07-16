# 🌐 Cloud Resume Challenge

A personal resume site deployed entirely on AWS using modern cloud architecture.

## 🧠 Overview

This project implements the [Cloud Resume Challenge](https://d30w5pew8tzjk5.cloudfront.net/) to showcase real-world cloud engineering skills. It is a static website with a dynamic view counter built using serverless components.

---

## 🔧 Tech Stack

- **Frontend**: HTML/CSS (hosted on Amazon S3, served via CloudFront)
- **API**: AWS API Gateway + AWS Lambda (Python)
- **Database**: DynamoDB (stores page view count)
- **CDN & Hosting**: CloudFront
- **IaC**: (Planned) Terraform
- **Others**: Git, GitHub, GitHub Actions (for CI/CD)

## ⚙️ Functionality

- 🖥️ **Static Resume Website** hosted on **S3**
- 🌐 **HTTPS + CDN** via **CloudFront**
- 📊 **Page View Counter**:
  - Uses API Gateway + Lambda to increment view count
  - DynamoDB table stores current view total
- ✅ CORS and permissions configured for secure API interaction

---

## 🚀 How It Works

1. User visits resume site via a custom domain or S3/CloudFront URL.
2. On page load, JavaScript calls a Lambda API endpoint.
3. Lambda increments and fetches the view count from DynamoDB.
4. View count is displayed live on the page.
