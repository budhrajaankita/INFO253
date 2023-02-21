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
        msg = req['data']['message']

        if not msg:
            return jsonify({'error': 'No JSON data provided'}), 400
        if str(msg).startswith("/"):
            cmd, _, new_msg = msg.partition(' ')
            if cmd == "/" or new_msg == "":
                return jsonify({'error': 'Incorrect format for command'}), 400
            else:
                resp = {'command': cmd, 'message': new_msg}
        else:
            resp = {'command': None, 'message': msg}
        
        return jsonify({"data": resp})
    except Exception as e:
        return jsonify({'error': str(e)}), 400


if __name__ == '__main__':
    app.run(debug=True)