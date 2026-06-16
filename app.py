from flask import Flask, render_template, request, jsonify
from application_layer import ApplicationLayer
from coordinator import Coordinator
from network_layer import NetworkLayer
from physical_layer import PhysicalLayer
from session_layer import SessionLayer
from transport_layer import TransportLayer

app = Flask(__name__)

coordinator = Coordinator()
coordinator.add_layer(ApplicationLayer("User_A", "User_B", "messaging"))
coordinator.add_layer(SessionLayer())
coordinator.add_layer(TransportLayer())
coordinator.add_layer(NetworkLayer())
coordinator.add_layer(PhysicalLayer())


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/send", methods=["POST"])
def send():
    message = request.form.get("message")

    # Encapsulation
    send_result = coordinator.send(message)

    wrapped_packet = send_result["PhysicalLayer"]

    # Decapsulation
    receive_result = coordinator.receive(wrapped_packet)

    return jsonify({
        "encapsulation": send_result,
        "decapsulation": receive_result
    })

if __name__ == "__main__":
    app.run(debug=True)