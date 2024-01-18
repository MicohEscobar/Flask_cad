import cv2
import numpy as np
from backend import load_tflite_model

interpreter = load_tflite_model()

def preprocess_image(image):
    # Resize the image to the desired input size of the model
    target_size = (150, 150)
    resized_image = cv2.resize(image, target_size)

    # Convert the image to grayscale (assuming BGR format)
    gray_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)

    # Normalize pixel values to the range [0, 1]
    normalized_image = (gray_image / 255.0).astype(np.float32)

    # Expand dimensions to match the model's expected input shape
    input_data = np.expand_dims(normalized_image, axis=-1)
    input_data = np.expand_dims(input_data, axis=0)

    return input_data


def predict_image(image_file):
    try:
        # Check if image_file is a string (file path)
        if isinstance(image_file, str):
            # Read the image content if it's a file path
            image = cv2.imread(image_file)
        else:
            # Load the image using OpenCV (assuming BGR format)
            image = cv2.imdecode(np.frombuffer(image_file.read(), np.uint8), cv2.IMREAD_COLOR)

        # Preprocess the image
        input_data = preprocess_image(image)

        # Make predictions using the TensorFlow Lite model
        interpreter.set_tensor(interpreter.get_input_details()[0]['index'], input_data)
        interpreter.invoke()
        output_data = interpreter.get_tensor(interpreter.get_output_details()[0]['index'])

        return output_data.tolist()

    except Exception as e:
        raise RuntimeError(f"Error during prediction: {str(e)}")
