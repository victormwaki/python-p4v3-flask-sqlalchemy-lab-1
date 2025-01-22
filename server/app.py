#!/usr/bin/env python3

from flask import Flask, make_response, jsonify
from flask_migrate import Migrate

from models import db, Earthquake

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)

@app.route('/')
def index():
    body = {'message': 'Flask SQLAlchemy Lab 1'}
    return make_response(body, 200)

# Add views here
@app.route('/earthquakes/magnitude/<float:magnitude>', methods=['GET'])
def get_earthquakes_by_magnitude(magnitude):
    # Query the database for earthquakes with magnitude >= parameter
    earthquakes = Earthquake.query.filter(Earthquake.magnitude >= magnitude).all()
    
    # Prepare response data
    earthquake_list = [earthquake.to_dict() for earthquake in earthquakes]
    response_data = {
        "count": len(earthquake_list),
        "quakes": earthquake_list  # Update key to "quakes" as expected by the test
    }
    
    # Return JSON response
    return jsonify(response_data), 200


if __name__ == '__main__':
    app.run(port=5555, debug=True)
