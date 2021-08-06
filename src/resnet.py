from tensorflow.keras.applications.resnet50 import ResNet50
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions
import numpy as np
# from src.service import get_response


class Resnet50_model:
    def __init__(self):
        self.image_height = 224
        self.image_width = 224
        self.model = ResNet50(include_top=True, weights='imagenet')

    def preprocess_image(self, img):
        output_image = img.resize((self.image_height, self.image_width))
        output_image = image.img_to_array(output_image)
        output_image = np.expand_dims(output_image, axis=0)
        output_image = preprocess_input(output_image)
        return output_image

    def predict_resnet50(self, image):
        preprocessed_image = self.preprocess_image(image)
        prediction = self.model.predict(preprocessed_image)
        class_predicted = decode_predictions(prediction, top=1)[0][0][1]
        probability = decode_predictions(prediction, top=1)[0][0][2]
        # response = get_response(probability, class_predicted)
        response = [{"probability": str(probability),
                     "classname": class_predicted}
                    ]
        return response
