from urllib.request import urlopen
from PIL import Image
from PIL import ImageFile
from src.model_initializer import ModelFactory
ImageFile.LOAD_TRUNCATED_IMAGES = True
initializer = None


def initialize():
    global initializer
    initializer = ModelFactory()


def get_image_from_url(image_url):
    with urlopen(image_url) as im:
        img = Image.open(im)
        return img


# def get_response(probability, class_predicted):
#     response = [{"probability": probability,
#                  "classname": class_predicted}
#                 ]
#     return response


def predict_image(request_data):
    img = None
    img = get_image_from_url(image_url=request_data["imageUrl"])
    model = initializer.get_model()
    prediction_result = model.predict_resnet50(img)
    return {"output_result": prediction_result}

