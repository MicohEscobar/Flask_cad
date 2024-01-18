from flask import Flask, request, jsonify, render_template
from predict import predict_image  # Assuming you have a predict.py file with the predict_image function
import os
from werkzeug.utils import secure_filename


app = Flask(__name__)

# Set the upload folder and allowed extensions
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}

# Function to check if a file has an allowed extension
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def create_uploads_folder():
    uploads_folder = app.config['UPLOAD_FOLDER']
    if not os.path.exists(uploads_folder):
        os.makedirs(uploads_folder)
    else:
        print(f"Folder already exists: {uploads_folder}")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Create the 'uploads' folder if it doesn't exist
        create_uploads_folder()

        # Check the content of the 'uploads' folder
        print(f"Content of 'uploads' folder: {os.listdir(app.config['UPLOAD_FOLDER'])}")

        # Check if the post request has the file part
        if 'image' not in request.files:
            return jsonify({'error': 'No file part'})

        file = request.files['image']

        # If the user does not select a file, browser also
        # submit an empty part without filename
        if file.filename == '':
            return jsonify({'error': 'No selected file'})

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

            # Save the file
            file.save(file_path)

            # Check if the file is present after saving
            print(f"Content of 'uploads' folder after saving: {os.listdir(app.config['UPLOAD_FOLDER'])}")

            # Make predictions using the predict_image function
            result = predict_image(file_path)

            # Return the prediction results
            return jsonify({'result': result})

        else:
            return jsonify({'error': 'Invalid file format'})

    except Exception as e:
        # Log the exception for debugging purposes
        app.logger.error(f"An error occurred: {str(e)}")
        return jsonify({'error': 'Internal server error.'}), 500

if __name__ == '__main__':
    app.run(debug=True)
