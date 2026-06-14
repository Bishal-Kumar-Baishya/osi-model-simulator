# OSI 5-Layer Model Simulator
A Flask-based simulator that demonstrates data encapsulation and decapsulation through a 5-layer OSI model. Watch how a message is transformed as it passes through Application, Session, Transport, Network, and Physical layers.

## Skills/Concepts Demonstrated
- **Python:** Classes, OOP, dictionaries, object composition
- **Networking:** Encapsulation, decapsulation, layered architecture, protocol stacks
- **Web Development:** Flask routes, client-server communication, Fetch API, DOM manipulation

## Setup and Run instructions
- Clone the repo by `git clone <repo link>`
- Install Flask:- `pip install flask`
- Navigate to project directory
- Run flask:- `python app.py`
- Open browser: `http://127.0.0.1:5000`
- Type a message and click Send

## Features
- Real-time layer-by-layer progression display
- Hardcoded users (User A, User B) for testing
- JSON-based data flow visualization
- Bidirectional message flow (send/receive)

## Project Structure
- `app.py` — Flask app with routes
- `coordinator.py` — Orchestrates data flow through layers
- `*_layer.py` — Individual layer classes
- `templates/index.html` — Frontend UI
- `static/script.js` — JavaScript for form handling

## How it works
User A sends a message. The Coordinator passes it through 5 layers (Application → Session → Transport → Network → Physical), with each layer adding its own metadata. The progression is displayed in real-time. Then the data is decapsulated for User B.

## Built with
- Python 3
- flask module
- datetime module
- random module
- Javascript
- HTML

## Future Improvements (Version 2)
- Nested encapsulation (realistic protocol stacking)
- CSS styling (3-column layout with better UI)
- User authentication and dynamic users
- Decapsulation animation
- Message history and logging