import pandas as pd
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.model_selection import train_test_split
import numpy as np
import json
import tensorflowjs as tfjs

# Load the preprocessed data
data = pd.read_csv('preprocessed_data.csv')

# Debug: Display the first few rows of the data
print(data.head())

# Preprocess the data
texts = data['messageContent'].astype(str).tolist()
labels = data['label'].tolist()

# Tokenize the text data
tokenizer = Tokenizer(oov_token='<OOV>')
tokenizer.fit_on_texts(texts)
sequences = tokenizer.texts_to_sequences(texts)
word_index = tokenizer.word_index

# Save the word index for later use in the web app
with open('word_index.json', 'w') as f:
    json.dump(word_index, f)

# Pad sequences to ensure uniform input size
maxlen = 100  # This should be the same as in your web app
padded_sequences = pad_sequences(sequences, maxlen=maxlen, padding='post')

# Convert labels to numpy array
labels = np.array(labels)

# Split the data into training and validation sets
X_train, X_val, y_train, y_val = train_test_split(padded_sequences, labels, test_size=0.2, random_state=42)

# Build the model
model = tf.keras.Sequential([
    tf.keras.layers.Embedding(input_dim=len(word_index) + 1, output_dim=16, input_length=100),  # Added input_length
    tf.keras.layers.GlobalAveragePooling1D(),
    tf.keras.layers.Dense(16, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
history = model.fit(X_train, y_train, epochs=10, validation_data=(X_val, y_val), batch_size=32)

# Save the model in TensorFlow.js format
tfjs.converters.save_keras_model(model, 'tfjs_model')

print("Model training complete and saved in TensorFlow.js format.")