# Number-Classification-API
The Number Classification API is a RESTful API that classifies a given number based on its mathematical properties. It determines whether a number is prime, perfect, or an Armstrong number, calculates the sum of its digits, and fetches a fun fact from the Numbers API.

This API is built using Python (AWS Lambda) and deployed via AWS API Gateway.

# 📌 Features

Checks if a number is prime

Checks if a number is perfect

Checks if a number is an Armstrong number

Returns the sum of digits of the number

Fetches a fun fact about the number from Numbers API

Returns structured JSON responses

Handles CORS for cross-origin requests

Hosted on AWS Lambda + API Gateway

# 🛠️ Technology Stack

## Language: Python

## Cloud Provider: AWS

## Compute: AWS Lambda

## API Gateway: Public endpoint exposure

## Data Source: Numbers API for fun facts

# 📂 Project Structure

### number-classification-api/
### │── lambda_function.py  # Main API logic
### │── requirements.txt    # Dependencies
### │── README.md           # Documentation
### │── deployment_package/ # Lambda deployment package


# 🔧 Installation & Local Testing

## 1️⃣ Clone the Repository

git clone https://github.com/Adewale-Olakinye/Number-Classification-API.git
cd number-classification-API

## 2️⃣ Install Dependencies

pip install -r requirements.txt

## 3️⃣ Run Locally (Simulate Lambda Execution)

python lambda_function.py

# 🌍 Deployment to AWS Lambda

## Step 1: Package the Lambda Function

mkdir deployment_package
pip install -r requirements.txt -t deployment_package/
cp lambda_function.py deployment_package/
cd deployment_package
zip -r ../lambda_number_api.zip .

## Step 2: Upload to AWS Lambda

Go to AWS Lambda Console → Create a new function.

Choose "Author from Scratch" → Runtime: Python.

Upload lambda_number_api.zip as the Lambda function code.

## Step 3: Create API Gateway for Public Access

Open API Gateway in AWS Console.

Create a new REST API.

Add a GET method and link it to your Lambda function.

Enable CORS.

Deploy the API and get the Invoke URL.

# 🎯 Usage

## API Endpoint

https://f34f218ve4.execute-api.us-east-1.amazonaws.com/dev/classify-number?number=371

# 🚀 Testing via Browser

## 3️Response (200 OK)
{
#### number:	371
#### is_prime:	false
#### is_perfect:	false
#### properties:	
#### 0:	"armstrong"
#### 1:	"odd"
#### digit_sum:	11
#### fun_fact:	"371 is a narcissistic number."
}

## 4️Error Response (400 Bad Request)
{
   #### "number": "invalid",
  #### "error": true
}

# 🌟 Acknowledgments
    • Numbers API for fun facts.
    • AWS Lambda & API Gateway for serverless hosting.
    
