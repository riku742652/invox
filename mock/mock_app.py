import random
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/estimate', methods=['POST'])
def estimate():
    if random.randint(0, 1):
        return jsonify({
                'success': True,
                'message': 'success',
                'estimated_data': {
                    'class': random.randint(1, 1000),
                    'confidence': round(random.random(), 4)
                }
            })
    else:
        return jsonify({
                'success': False,
                'message': f'Error:E{random.choice([400, 500])}{random.randint(0, 999)}',
                'estimated_data': {}
            })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)
