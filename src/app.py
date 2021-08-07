from flask import Flask, request, jsonify, Response, make_response
import json
from src.service import predict_image, initialize

app = Flask(__name__)


@app.errorhandler(Exception)
def handle_exception(e):
    results = dict({
                    "ERROR_MSG": str(e)
                    })
    return make_response(jsonify(results), 500)


@app.route('/my_api/classify', methods=['POST'])
def main_predict():
    request_data = json.loads(request.get_data().decode('utf-8'))
    results = predict_image(request_data)
    return jsonify(results)


def create_app():
    initialize()
    return app


if __name__ == '__main__':
    initialize()
    app.run(host='0.0.0.0', port=8181, threaded=True)


