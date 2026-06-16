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
- **Nested encapsulation** — each layer wraps previous layer's entire data
- **Step-by-step visualization** — see data transformation at each layer
- **Bidirectional flow** — encapsulation and decapsulation in single request
- **JSON** — based data flow visualization

## Project Structure
- `app.py` — Flask app with routes
- `coordinator.py` — Orchestrates data flow through layers
- `*_layer.py` — Individual layer classes
- `templates/index.html` — Frontend UI
- `static/script.js` — JavaScript for form handling

## How it works
User A sends a message through encapsulation:
1. Application Layer creates initial message structure
2. Session Layer wraps it with session management
3. Transport Layer adds port information
4. Network Layer adds IP addressing
5. Physical Layer converts to binary frame (simulated)
The fully wrapped packet is then decapsulated at User B's side, unwrapping each layer in reverse order until the original message is revealed.

## Built with
- Python 3
- flask module
- datetime module
- random module
- Javascript
- HTML

## Version History
- **V1:** Flat dictionary encapsulation, basic UI
- **V2:** Nested encapsulation, bidirectional flow, realistic protocol stacking

## Future Improvements
- CSS styling and responsive design
- Firewall rule simulation
- Intrusion detection system (IDS)
- Packet inspection tool
- Multiple protocol support (HTTP, DNS, SSH)
- Message history and persistence
- User authentication and multiple users