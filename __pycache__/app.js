document.getElementById('imageForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const fileInput = document.getElementById('imageInput');
    const formData = new FormData();
    formData.append('image', fileInput.files[0]);

    fetch('/predict', {
        method: 'POST',
        body: formData,
    })
    .then(response => response.json())
    .then(data => {
        console.log('Prediction result:', data);
        // Handle the prediction result as needed
    })
    .catch(error => {
        console.error('Error:', error);
        // Handle errors
    });
});
