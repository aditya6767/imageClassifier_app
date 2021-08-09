from app import create_app
import os

os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

app = create_app()
