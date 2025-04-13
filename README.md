# 🛍️ Ecommerce Price Comparison Tool using AWS


This project is a serverless web application that allows users to compare prices of products across multiple e-commerce platforms. Built using AWS services, the tool provides real-time product price comparisons with a scalable, secure, and cost-effective architecture.

🚀 Features



🔍 Search for a product by name

💸 Compare prices across various online stores

📊 Fast and dynamic results powered by serverless compute

🗃️ Product data stored in DynamoDB

🌐 Deployed as a static website using Amazon S3 and CloudFront

🧰 AWS Services Used



Amazon S3 – For static website hosting (Frontend)

Amazon API Gateway – To expose REST APIs for frontend interaction

AWS Lambda – To handle backend logic and product price comparison

Amazon DynamoDB – To store product and price details

Amazon CloudFront – To serve frontend with low latency and high transfer speed

Amazon CloudWatch – To monitor application logs and metrics

💡 How it Works


User inputs a product name on the frontend.

API Gateway triggers a Lambda function.

Lambda queries DynamoDB for product details and pricing.

Results are returned and displayed on the frontend.

🛠️ Tech Stack


Frontend: HTML, CSS, JavaScript

Backend: AWS Lambda (Node.js)

Database: Amazon DynamoDB

API: Amazon API Gateway

Hosting: Amazon S3 + CloudFront or Only S3

📌 Setup Instructions


Deploy the frontend to an S3 bucket and enable static hosting.

Create API Gateway endpoints and link them to Lambda functions.

Write and deploy Lambda functions to process requests.

Set up DynamoDB tables and import product data.

Use CloudFront to serve the frontend globally.

Monitor using CloudWatch for debugging and performance.
