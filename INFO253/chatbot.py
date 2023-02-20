# -*- coding: utf-8 -*-

from flask import Flask, jsonify, request

app = Flask(__name__)


@app.errorhandler(404)
def page_not_found(e):
    return "This route doesn't exist! {}".format(e)

#Post Endpoint to take data json as input and return data json output
@app.route('/message', methods=['POST'])
def handle_message():
    try:
        req = request.get_json()
        if not req:
            return jsonify({'error': 'No JSON data provided'}), 400
        msg = req['data']['message']
        if str(msg).startswith("/"):
            cmd, _, new_msg = msg.partition(' ')
            resp = {'command': cmd, 'message': new_msg}
        else:
            resp = {'command': None, 'message': msg}
        
        return jsonify({"data": resp})
    except ValueError as e:
        return jsonify({'error': str(e)}), 400


if __name__ == '__main__':
    app.run(debug=True)