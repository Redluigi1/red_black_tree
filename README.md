# Red-Black Tree

This project aims to impelent Red-Black Trees in Python, and includes a web interface for visualizing them. It consists of a backend implemented using Flask and hosted on PythonAnywhere, and a frontend built with React and hosted on Netlify. The visualization is created using Graphviz, which dynamically updates as the user interacts with the tree by inserting and deleting nodes.

## Project Overview

### Tech Stack

- **Frontend**: React
- **Backend**: Flask
- **Visualization**: Graphviz
- **Hosting**:
  - **Frontend**: Netlify
  - **Backend**: PythonAnywhere

### Key Features

- **Dynamic Tree Visualization**: The Red-Black Tree is visualized in real-time as nodes are inserted or deleted.
- **Interactive Interface**: Users can add or remove nodes through a simple web interface.
- **Robust Backend**: The Flask backend handles all the tree operations and ensures the Red-Black Tree properties are maintained.

## Red-Black Tree Operations

### Insertion

1. **Insert Node**: A new node is added to the tree following the binary search tree insertion rules.
2. **Fix Violations**: After insertion, the tree might violate Red-Black Tree properties. These violations are fixed using rotations and recoloring:
   - If the parent of the newly inserted node is red, and the uncle is also red, both the parent and the uncle are recolored black, and the grandparent is recolored red.
   - If the parent is red but the uncle is black, rotations (left or right) are performed to balance the tree and maintain the properties.

### Deletion

1. **Find Node**: The node to be deleted is located using a standard binary search.
2. **Remove Node**: The node is removed, and the tree is restructured to maintain the binary search tree properties.
3. **Fix Violations**: Post-deletion, the tree might violate Red-Black Tree properties. These are fixed by:
   - Recoloring and rotating nodes to ensure that the tree remains balanced and the properties are maintained.

### Tree Properties

A Red-Black Tree is a balanced binary search tree with the following properties:
- **Node Color**: Each node is either red or black.
- **Root Property**: The root of the tree is always black.
- **Leaf Property**: Every leaf (NIL node) is black.
- **Red Property**: If a red node has children, then the children are always black (no two red nodes can be adjacent).
- **Depth Property**: Every path from a node to its descendant leaves has the same number of black nodes.

## API Endpoints

The backend exposes several endpoints for interacting with the Red-Black Tree:

- **POST /generate**: Initializes a new Red-Black Tree.
- **POST /insert**: Inserts a new value into the Red-Black Tree. Requires a JSON payload with a `value` field.
- **POST /delete**: Deletes a value from the Red-Black Tree. Requires a JSON payload with a `value` field.
- **GET /svg**: Retrieves the SVG visualization of the Red-Black Tree.

## How to Use

1. **Initialize Tree**: Start by initializing a new Red-Black Tree using the `/generate` endpoint.
2. **Insert Nodes**: Add nodes by sending a `POST` request to the `/insert` endpoint with the value to be inserted.
3. **Delete Nodes**: Remove nodes by sending a `POST` request to the `/delete` endpoint with the value to be deleted.
4. **View Visualization**: Retrieve the current state of the tree by accessing the `/svg` endpoint, which returns an SVG image of the tree.


