# Medic API Client

This Python client provides easy access to the Medic API, allowing you to interact with various endpoints for symptom tracking, AI-powered herbal advice, and more.

## Installation

Install the Medic client using pip:

```bash```
pip install medic-client


## Usage

Initialize the client:

```Python```

from medic_client import MedicClient

client = MedicClient('your-api-key-here')


## Tracking Symptoms
 
response = client.log_symptom('headache', severity=3)
    print(response)

## Retrieve user's symptom history:

symptoms = client.get_symptoms()
for symptom in symptoms:
    print(f"Symptom: {symptom['symptom']}, Severity: {symptom['severity']}, Date: {symptom['timestamp']}")


## AI-Powered Medical Advice

Get Medical advice:

question = "What are the good for headaches?"
ai_response = client.get_ai_response(question)
print(ai_response)


## Managing API Keys
Generate a new API key:

new_key = client.generate_api_key("My New Key")
print(f"New API Key: {new_key['key']}")

## List all API keys:

keys = client.list_api_keys()
for key in keys:
    print(f"Key: {key['key']}, Name: {key['name']}, Active: {key['is_active']}")


## Error Handling
It's recommended to use try-except blocks for error handling:


try:
    response = client.get_ai_response("What herbs help with sleep?")
    print(response)
except Exception as e:
    print(f"An error occurred: {str(e)}")


# Download locally then install with 

pip install .


