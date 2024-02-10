document.getElementById('predictButton').addEventListener('click', function(event) {
    const fileInput = document.getElementById('imageInput');
    const formData = new FormData();
    formData.append('image', fileInput.files[0]);

    fetch('/predict', {
        method: 'POST',
        body: formData,
    })
    .then(response => response.json())
    .then(data => {
        // Handle the prediction result
        console.log('Prediction result:', data);

        // Display the prediction result in the log section
        const logSection = document.getElementById('logSection');
        logSection.innerHTML = `<p>Prediction Result: ${JSON.stringify(data)}</p>`;
    })
    .catch(error => {
        // Handle errors
        console.error('Error:', error);

        // Display the error in the log section
        const logSection = document.getElementById('logSection');
        logSection.innerHTML = `<p>Error: ${error.message}</p>`;
    });
});

// Function to update the visualization board
function updateVisualizationBoard(predictionData) {
    const visualizationBoard = document.getElementById('visualizationBoard');

    // Create a new image element
    const imgElement = document.createElement('img');
    imgElement.src = URL.createObjectURL(fileInput.files[0]);
    imgElement.alt = 'Predicted Image';

    // Create a paragraph element to display prediction result
    const resultParagraph = document.createElement('p');
    resultParagraph.textContent = `Prediction Result: ${JSON.stringify(predictionData.result)}`;

    // Append the image and result to the visualization board
    visualizationBoard.appendChild(imgElement);
    visualizationBoard.appendChild(resultParagraph);
}

function predict() {
    // This function can be empty or can contain additional logic as needed
}
