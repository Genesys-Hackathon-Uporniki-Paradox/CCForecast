from flask import Flask, jsonify, request
from flask_cors import CORS
from .metric_prediction import predict

app = Flask(__name__)


@app.route('/')
def hello_world():
    return jsonify({'success': 'Hello World!'})


@app.route('/predictPlease', methods=['POST'])
def predict_metric():
    if request.json is not None:
        data = request.json['data']
        predict_days = request.json['predictDays']

        stats = list(list(data.values())[0].keys())
        predictions = {}

        for s in stats:
            predict_stats = {}

            for item in list(data.items()):
                predict_stats[item[0]] = item[1][s]

            predictions[s] = predict(predict_stats, predict_days)

        return jsonify(predictions)
    else:
        return jsonify({'error': 'No date provided'})


CORS(app)

if __name__ == '__main__':
    app.run(debug=False)
