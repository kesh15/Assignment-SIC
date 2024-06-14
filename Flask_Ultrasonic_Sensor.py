from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/sensor', methods=['POST'])
def receive_sensor_data():
    data = request.get_json()

    if not data or 'distance' not in data:
        return jsonify({"message": "Invalid data"}), 400

    distance = data['distance']
    print(f"Received distance: {distance} cm")

    response = {
        "message": "Data received successfully",
        "received_distance": distance
    }

    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
