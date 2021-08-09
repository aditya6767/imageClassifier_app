from resnet import Resnet50_model


class ModelFactory:
    def __init__(self):
        self.resnet_model = Resnet50_model()

    def get_model(self):
        return self.resnet_model

