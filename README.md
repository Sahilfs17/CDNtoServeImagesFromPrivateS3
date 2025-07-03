# 🌐 Serverless CDN Proxy for Private S3-Compatible Buckets

> Securely serve private content globally using AWS CloudFront + Lambda Function URLs — without managing any servers.
---

## 🚀 Overview

This project demonstrates how to proxy and cache content from **any third-party S3-compatible object storage** (e.g., MinIO, Wasabi, Backblaze, Yotta) using:

- 🛠️ **AWS Lambda** for credentialed access to private buckets  
- ⚡ **CloudFront** as a global CDN with long-term edge caching  
- 🧰 **boto3** for S3-compatible API integration  
- 🔒 No EC2, NGINX, or load balancers required!

---

## 🧠 Use Cases

- Replace EC2-based proxies with a fully **serverless, zero-maintenance solution**
- Safely expose private assets to the public via **secure intermediaries**
- Seamlessly integrate with **custom websites or frontend apps**

---

## 🏗️ Architecture

CloudFront → Lambda Function URL → Authenticated S3-Compatible Bucket


---

## ⚙️ How It Works

1. CloudFront receives a request like:  
   `https://<distribution>.cloudfront.net/images/banner.webp`

2. It forwards the request to your **Lambda Function URL**

3. Lambda uses **boto3** and stored credentials to fetch the image object securely from a private S3-compatible store

4. It returns the image with proper headers (e.g., `Cache-Control`, `Content-Type`)

5. CloudFront caches and serves the response globally 🌍

---

## 🔧 Setup Instructions

### 1. Deploy Lambda

- Create a Lambda function (Python 3.12+)
- Add environment variables:
  - `AWS_ACCESS_KEY_ID`
  - `AWS_SECRET_ACCESS_KEY`
  - `S3_ENDPOINT_URL`
  - `S3_BUCKET_NAME`

- Copy code from `lambda/lambda_function.py`
- Enable **Function URL** with `Auth type = NONE`

### 2. Configure CloudFront

- Create a CloudFront distribution
- Set **origin domain** to your Lambda URL (without `https://`)
- Use **HTTPS only** for the origin protocol policy
- Add behavior for path pattern `/images/*` (or as needed)
- 

### 3. Test Your CDN URL
https://your-distribution.cloudfront.net/images/sample.img


---

## 🛡️ Security Considerations

- Use environment variables or AWS Secrets Manager for credentials
- Optionally implement:
  - Header-based access checks in Lambda
  - Signed URLs
  - Origin Access Control (OAC) in CloudFront

---

## 💡 Future Enhancements

- ✅ Add image transformation (resize/compress) on-the-fly
- ✅ Support for Signed CDN URLs
- ✅ CloudFormation/Terraform IaC templates
- ✅ Logging and analytics via CloudWatch

---

## 📚 Related Blog Post

👉 [Medium Post](https://medium.com/@sahilsayyedfs17/building-a-serverless-cdn-for-a-private-third-party-s3-bucket-using-aws-cloudfront-lambda-ae102347d51f) — “How I Built a Serverless CDN for S3-Compatible Storage Using Lambda and CloudFront”

---

## 🪪 License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

> Built with ☁️ AWS, 🔐 Python, and a passion for clean architecture.

