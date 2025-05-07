from flask import Blueprint, render_template, request, jsonify
from .crypto import caesar, rc4, aes, des

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/api/process', methods=['POST'])
def process():
    data = request.json
    alg = data.get('algorithm')
    mode = data.get('mode')
    text = data.get('text', '')
    key  = data.get('key', '')

    if alg == 'caesar':
        shift = int(key) if key.isdigit() else 0
        result = caesar(text, shift, encrypt=(mode == 'encrypt'))
    elif alg == 'rc4':
        result = rc4(text, key, encrypt=(mode == 'encrypt'))
    elif alg == 'aes':
        result = aes(text, key, encrypt=(mode == 'encrypt'))
    elif alg == 'des':
        result = des(text, key, encrypt=(mode == 'encrypt'))
    else:
        result = ''

    return jsonify({'result': result})