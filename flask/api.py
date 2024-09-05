import json
import requests

headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiOTVlYjI0NTktN2FhMi00MjQxLThkN2MtMmE2NWFlMjkxNmRlIiwidHlwZSI6ImFwaV90b2tlbiJ9.hnR156RVg2I6LRwwfO4BShrSCK0demW0dVHSv-su3_8"}


def ner(text):
    url = "https://api.edenai.run/v2/text/named_entity_recognition"
    payload = {
        "providers": "google,amazon",
        "language": "en",
        "text": text
    }
    response = requests.post(url, json=payload, headers=headers)
    result = json.loads(response.text)
    entities = result.get('amazon', {}).get('items', [])
    simplified_entities = [{'entity': item['entity'], 'category': item['category']} for item in entities]

    return simplified_entities

def sentimetal_analysis(text):
    url = "https://api.edenai.run/v2/text/sentiment_analysis"
    payload = {
        "providers": "google,amazon",
        "language": "en",
        "text": "this is a test",
    }
    response = requests.post(url, json=payload, headers=headers)
    result = json.loads(response.text)
    return result.get('google', {}).get('items', [])