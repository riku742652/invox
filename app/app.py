from datetime import datetime
import requests
import traceback

from flask import Flask, jsonify, request

from config import get_config
from lib import validate
from models.ai_analysis_log import AiAnalysisLog


app = Flask(__name__)
config = get_config()


@app.route("/register", methods=["POST"])
def register_image_class():
    '''
        [POST]クラス登録API
            mock-up APIをコールし結果をai_analysis_logテーブルに登録する
        request:
            {
                'image_path': <str> 画像のPath
            }
        response:
            {
                'status': <int> ステータスコード,
                'message': <str> 結果
            }
    '''
    app.logger.info('[POST]/register start')
    request_time = datetime.now()
    request_data = request.json
    app.logger.debug(f'data:{request_data}')

    # リクエストパラメータのチェック
    if not request_data.get('image_path'):
        return jsonify({
            'status': 400,
            'massage': 'image_path is required'
        })
    if not validate.image_path(request_data['image_path']):
        return jsonify({
            'status': 400,
            'massage': 'invalid image_path'
        })

    # mock-up APIをコール
    try:
        response = requests.post(
            config.MOCK_API + config.ESTIMATE_ENDPOINT,
            data=request_data)
    except Exception:
        traceback.format_exc()
        return jsonify({
            'status': 500,
            'massage': 'mock-up api call failed'
        })

    response_time = datetime.now()
    result_dict = response.json()
    app.logger.debug(f'response: {result_dict}')

    assigned_class = None
    confidence = None
    # リクエスト成功の場合は class と confidence を登録
    if result_dict['success']:
        assigned_class = result_dict['estimated_data']['class']
        confidence = result_dict['estimated_data']['confidence']

    # データ登録
    result = AiAnalysisLog.register_data(
        result_dict['success'],
        request_data['image_path'],
        result_dict['message'],
        assigned_class,
        confidence,
        request_time,
        response_time
    )
    if result is False:
        app.logger.info('register data failed')
        return jsonify({
            'status': 500,
            'message': 'register data failed'
        })
    app.logger.info('register data succeed')
    app.logger.info('[POST]/register finish')

    return jsonify({
        'status': 200,
        'message': 'ok'
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
