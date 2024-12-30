async function trainModel() {
    // Load preprocessed data from CSV
    const response = await fetch('model/preprocessed_data.csv');
    const csvData = await response.text();

    // Parse CSV data using PapaParse
    const parsedData = Papa.parse(csvData, {
        header: true,
    });

    // Filter out rows with missing or undefined messageContent or labels
    const filteredData = parsedData.data.filter(row => row.messageContent && row.label !== undefined);

    // Store the total number of SMS messages used for training
    const totalSMSCount = filteredData.length;

    // Save the total SMS count to local storage for later use
    localStorage.setItem('totalSMSCount', totalSMSCount);

    // Map the data to messages and labels
    const messages = filteredData.map(row => row.messageContent);
    const labels = filteredData.map(row => parseInt(row.label));

    // Create a word index
    const wordIndex = {};
    let index = 1;
    messages.forEach(msg => {
        msg.toLowerCase().split(' ').forEach(word => {
            if (!wordIndex[word]) {
                wordIndex[word] = index++;
            }
        });
    });

    console.log(wordIndex);
    // Save the word index to a JSON file
    await fetch('model/word_index.json', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(wordIndex),
    });

    // Convert messages to sequences of integers based on the word index
    const sequences = messages.map(msg =>
        msg.split(' ').map(word => wordIndex[word] || 0)
    );

    // Pad sequences to the same length
    const maxlen = 100;
    const paddedSequences = sequences.map(seq => {
        if (seq.length > maxlen) {
            return seq.slice(0, maxlen);
        } else {
            return [...seq, ...Array(maxlen - seq.length).fill(0)];
        }
    });

    // Convert data to tensors
    const inputTensor = tf.tensor2d(paddedSequences);
    const labelTensor = tf.tensor2d(labels, [labels.length, 1]);

    // Define the model
    const model = tf.sequential();
    model.add(tf.layers.embedding({ inputDim: Object.keys(wordIndex).length + 1, outputDim: 16, inputLength: maxlen }));
    model.add(tf.layers.globalAveragePooling1d());
    model.add(tf.layers.dense({ units: 16, activation: 'relu' }));
    model.add(tf.layers.dense({ units: 1, activation: 'sigmoid' }));

    // Compile the model
    model.compile({
        optimizer: 'adam',
        loss: 'binaryCrossentropy',
        metrics: ['accuracy'],
    });

    // Train the model
    const history = await model.fit(inputTensor, labelTensor, {
        epochs: 10,
        validationSplit: 0.2,
        batchSize: 32,
    });

    console.log('Model training complete.');

    // Save the model to local storage or IndexedDB
    await model.save('localstorage://phishing-detection-model');
}

// Call the training function
trainModel();