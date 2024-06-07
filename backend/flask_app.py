from flask import Flask, request, Response, jsonify
from graphviz import Source
from red_black import RBTree
from flask_cors import CORS


app = Flask(__name__)


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
rb_tree = RBTree()

# Helper function to set CORS headers
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'  # Allow requests from any origin
    response.headers['Access-Control-Allow-Methods'] = 'POST, GET'  # Allow POST and GET methods
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'  # Allow Content-Type header
    return response

@app.route('/generate', methods=['POST'])
def generate():
    global rb_tree
    rb_tree = RBTree()
    return 'RB Tree initialized.'

@app.route('/insert', methods=['POST'])
def insert():
    data = request.json
    value = data.get('value')
    if value is None:
        return jsonify({'error': 'Please provide a value to insert.'}), 400
    try:
        rb_tree.add(int(value))
        return 'Value inserted successfully.'
    except ValueError:
        return jsonify({'error': 'Value must be an integer.'}), 400

@app.route('/delete', methods=['POST'])
def delete():
    data = request.json
    value = data.get('value')
    if value is None:
        return jsonify({'error': 'Please provide a value to delete.'}), 400
    try:
        rb_tree.delete_node(int(value))
        return 'Value deleted successfully.'
    except ValueError:
        return jsonify({'error': 'Value must be an integer.'}), 400

@app.route('/svg', methods=['GET'])
def get_svg():
    global rb_tree
    rb_tree.visualize()
    with open('RBTREE.svg', 'r') as f:
        svg_data = f.read()
    response = Response(svg_data, mimetype='image/svg+xml')
    return add_cors_headers(response)  # Add CORS headers to the response

if __name__ == '__main__':
    app.run(debug=True)
