import json
import requests
import math

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    """Check if a number is a perfect number."""
    if n < 1:
        return False
    return sum(i for i in range(1, n) if n % i == 0) == n

def is_armstrong(n):
    """Check if a number is an Armstrong number."""
    num_str = str(n)
    num_length = len(num_str)
    return sum(int(digit) ** num_length for digit in num_str) == n

def get_fun_fact(n):
    """Fetch a fun fact from Numbers API."""
    try:
        response = requests.get(f"http://numbersapi.com/{n}/math?json")
        if response.status_code == 200:
            return response.json().get("text", "No fun fact available.")
    except requests.RequestException:
        return "Fun fact unavailable due to network issues."
    return "No fun fact available."

def lambda_handler(event, context):
    try:
        # Safely extract query parameters
        num_str = event.get("queryStringParameters", {}).get("number")

        # If 'number' is missing, return error
        if num_str is None:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "Missing 'number' parameter"})
            }

        # Validate if input is an integer
        if not num_str.isdigit():
            return {
                "statusCode": 400,
                "body": json.dumps({"number": num_str, "error": True})
            }

        number = int(num_str)

        # Determine properties
        properties = []
        if is_armstrong(number):
            properties.append("armstrong")
        properties.append("odd" if number % 2 != 0 else "even")

        # Prepare response
        response_data = {
            "number": number,
            "is_prime": is_prime(number),
            "is_perfect": is_perfect(number),
            "properties": properties,
            "digit_sum": sum(int(d) for d in str(number)),
            "fun_fact": get_fun_fact(number)
        }

        return {
            "statusCode": 200,
            "body": json.dumps(response_data)
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }

