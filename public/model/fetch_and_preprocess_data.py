import requests
import json
import pandas as pd

# Replace with your Firebase Realtime Database URL
firebase_url = 'https://smsnet2024-default-rtdb.europe-west1.firebasedatabase.app'
phishing_reports_endpoint = '/phishingReports.json'
not_phishing_reports_endpoint = '/notPhishingReports.json'

def get_data_from_firebase(endpoint):
    try:
        response = requests.get(firebase_url + endpoint)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from Firebase: {e}")
        return None

def preprocess_data(data, label):
    # Convert to DataFrame and add label
    if data is None:
        return pd.DataFrame()

    records = []
    for key, value in data.items():
        value['label'] = label
        records.append(value)
    
    df = pd.DataFrame(records)
    return df

def main():
    # Fetch data from Firebase
    phishing_data = get_data_from_firebase(phishing_reports_endpoint)
    not_phishing_data = get_data_from_firebase(not_phishing_reports_endpoint)

    # Debug: Print fetched data to understand its structure
    print("Phishing Data:", phishing_data)
    print("Not Phishing Data:", not_phishing_data)

    # Preprocess data
    phishing_df = preprocess_data(phishing_data, 1)
    not_phishing_df = preprocess_data(not_phishing_data, 0)

    # Combine datasets and create labels
    data = pd.concat([phishing_df, not_phishing_df])

    # Save preprocessed data to CSV
    data.to_csv('preprocessed_data.csv', index=False)
    print("Data saved to preprocessed_data.csv")

if __name__ == '__main__':
    main()