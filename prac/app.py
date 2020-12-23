from flask import Flask, render_template, jsonify, request

app = Flask(__name__)


# HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/mypage')
def mypage():
    return 'This is mypage!'


# API 역할 하는
@app.route('/test', methods=['GET'])
def test_get():
    title_receive = request.args.get('title_give')
    print(title_receive)
    return jsonify({'msg': '이 요청은 GET 메소드 입니다', 'result': 'success'})


@app.route('/test', methods=['POST'])
def test_post():

    title_receive = request.form.get('title_give')
    print('test_post: ' + title_receive)
    return jsonify({'msg': '이 요청은 POST 메소드 입니다', 'result': 'success', 'data': title_receive})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)