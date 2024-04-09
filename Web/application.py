from flask import Flask, request, jsonify
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.densenet import preprocess_input
from tensorflow.keras.applications.vgg16 import preprocess_input as preprocess_input_mri
import numpy as np
from PIL import Image
import os
from flask_cors import CORS,cross_origin
import json
import h5py

app = Flask(__name__)
app.debug = False
CORS(app)
# CORS(app, resources={{"origins": ["http://localhost:3000", "http://127.0.0.1:3000"]}})
# app.config["CORS_HEADERS"] = "Content-Type"
# app.config["CORS_HEADERS"] = "Content-Type"

# # Load the ECG model
base_dir=os.path.dirname(os.path.abspath(__file__))
print(base_dir) 
joinedPath=os.path.join(base_dir,"final_model.hdf5")
ecgModel=load_model(joinedPath)
# ecgModel = load_model('C:\\Users\\Vinit\\Downloads\\OneDrive_2024-03-16\\ECG Project\\Dataset\\Web\\ecg-frontend\\final_model.hdf5')

class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)


@app.route('/model', methods=['POST'])
# @cross_origin()  # Enable CORS for this route
def predict_ct():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400,{"Access-Control-Allow-Origin": "*"}

    file = request.files['file']
    # Get the file from the request
    print(file)
    print(request.files)
    if file.filename.endswith('.h5') or file.filename.endswith('.hdf5'):
        try:
            # Read the ECG signal data from the HDF5 file
            
            with h5py.File(file, 'r') as hf:
                ecg_data = hf['tracings']  # Assuming the dataset is named 'data'
                print(ecg_data)
                x = np.array(hf['tracings'])
                print(x[0].shape)
                print(x)
        except Exception as e:
            return jsonify({'error': f'Error reading HDF5 file: {e}'}), 400, {"Access-Control-Allow-Origin": "*"}
    else:
        return jsonify({'error': 'File format not supported. Please provide an HDF5 file'}), 400, {"Access-Control-Allow-Origin": "*"}

    predictions = ecgModel.predict(x)
    print(predictions)
    threshold = 0.4
    y_pred = np.where(predictions > threshold, 1, 0)
    print(y_pred)
    # Make predictions on the image
    # predictions = ecgModel.predict(data)
    # print(predictions)

    # # Interpret the predictions
    # class_labels = ['Adenocarcinoma', 'Large.cell.carcinoma',
    #                 'Normal', 'Squamous.cell.carcinoma']
    # predicted_class_index = np.argmax(predictions, axis=1)
    # predicted_class_label = class_labels[predicted_class_index[0]]

    # print("CT SCAN Prediction: ", predicted_class_label, float(
    #     predictions[0][predicted_class_index[0]]) * 100)

    # # Prepare the response
    # response = {
    #     'predicted_class': predicted_class_label,
    #     'probability': float(predictions[0][predicted_class_index[0]]) * 100
    # }

    # # Remove the temporary image file
    # os.remove(img_path)



    # Return the response in JSON format
    return json.dumps({"data":y_pred},cls=NumpyEncoder),200,{"Access-Control-Allow-Origin": "*",
                       "Access-Control-Allow-Methods": "POST",
                       "Access-Control-Allow-Headers": "Content-Type",}




# @app.route('/pneumonia', methods=['POST'])
# def pneumonia_prediction():
#     if 'image' not in request.files:
#         return jsonify({'error': 'No image file provided'})

#     # Load and preprocess the image
#     img = request.files['image']
#     img_path = f"tmp/{img.filename}"  # Save the file temporarily
#     img.save(img_path)

#     test_image = image.load_img(img_path, target_size=(180, 180))
#     test_image = image.img_to_array(test_image)
#     test_image = np.expand_dims(test_image, axis=0)
#     test_image = test_image / 255.0
#     # test_image = preprocess_input_resnet(test_image)

#     prediction = pneumonia_model.predict(test_image)
#     print("Prediction: ", prediction[0][0])
#     if prediction[0][0] < 0.5:
#         statistic = (1.0-prediction[0]) * 100
#         result = {
#             'predicted_class': 'Normal',
#             'probability': float(statistic)
#         }
#     else:
#         statistic = prediction[0] * 100
#         result = {
#             'predicted_class': 'PNEUMONIA',
#             'probability': float(statistic)
#         }
#     # Remove the temporary image file
#     os.remove(img_path)

#     return jsonify(result)


@app.route('/', methods=['GET'])
def welcome():
    return "Hi"


if __name__ == '__main__':
    app.run(port=8000)
