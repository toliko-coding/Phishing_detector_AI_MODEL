import pandas as pd
import json
import tensorflow as tf


def convert_csv_to_json(csv_file_path, json_file_path, max_sequence_length=100, num_words=5000):
    # Load the CSV file
    data = pd.read_csv(csv_file_path)

    # Ensure all messageContent entries are strings and handle NaN values
    data['messageContent'] = data['messageContent'].astype(str).fillna('')

    # Preprocess the text data
    tokenizer = tf.keras.preprocessing.text.Tokenizer(num_words=num_words, oov_token='<OOV>')
    tokenizer.fit_on_texts(data['messageContent'])
    sequences = tokenizer.texts_to_sequences(data['messageContent'])
    padded_sequences = tf.keras.preprocessing.sequence.pad_sequences(sequences, maxlen=max_sequence_length, padding='post', truncating='post')

    # Convert to a list of dictionaries for JSON format
    json_data = []
    for i, seq in enumerate(padded_sequences):
        json_data.append({
            "sequence": seq.tolist(),
            "label": int(data['label'].iloc[i])  # Assuming the label is an integer
        })

    # Save the processed data to a JSON file
    with open(json_file_path, 'w') as json_file:
        json.dump(json_data, json_file)

    print(f"Data successfully converted and saved to {json_file_path}")

if __name__ == '__main__':
    convert_csv_to_json('preprocessed_data.csv', 'preprocessed_data.json')