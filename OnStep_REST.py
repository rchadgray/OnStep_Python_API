from flask import Flask, jsonify, request
from time import sleep
from serial import Serial

import sys

port = Serial('/dev/ttyS0', 9600, timeout=1)
port.flushInput()
port.flushOutput()

# Rest API
app = Flask(__name__)

@app.route('/onstep', methods=['GET'])
def get_data():
    try:
        byte_obj = request.args.get('cmd')
        port.write(bytes(byte_obj,'utf-8'))
        print(byte_obj)
        return jsonify(foo=1,
                       moo=2)

    except (IndexError, IOError) as e:
        port.flushInput()
        port.flushOutput()
        return jsonify({'error': e.message}), 503

try:
    app.run()

except KeyboardInterrupt:
    print ("\nCtrl-C pressed.  Closing serial port and exiting...")
finally:
    port.close()
