import tensorflow as tf

def load_tflite_model():
    model_path = 'model/32bit_model.tflite'
    interpreter = tf.lite.Interpreter(model_path=model_path)
    interpreter.allocate_tensors()
    return interpreter
