from flask import Flask, request
import circlify
import json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    return 'Hello World!'

@app.route('/ping', methods=['GET'])
def ping():
    return 'Pong'
    
@app.route('/circles', methods=['POST'])
def get_circles():
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """
    request_json = request.get_json()
    if not request_json or 'height' not in request_json or 'width' not in request_json:
        return {"error": "Height or width is missing"}, 400

    if 'percentages' not in request_json:
        return {"error": "Percentages missing"}, 400
    
    height = request_json['height']
    width = request_json['width']
    percentages = request_json['percentages']

    # Calculate maximum circle radius
    max_radius = min(width, height) / 2

    # Circlify the data with maximum radius
    circles = circlify.circlify(percentages, show_enclosure=False, target_enclosure=circlify.Circle(x=0, y=0, r=max_radius))
    print(circles)

    circle_objects = []
    for circle in circles:
        circle_dict = {"x": circle.x, "y": circle.y, "radius": circle.r}
        circle_objects.append(circle_dict)

    json_data = json.dumps(circle_objects)
    return json_data

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)