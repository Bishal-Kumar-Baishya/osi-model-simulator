class SessionLayer:
    def __init__(self):
        self.session_id = "session_001"

    def process(self, data, direction):        
        payload = {}

        # Encapsulation
        if direction == "encapsulation":
            payload["payload"] = data
            payload["session_id"] = self.session_id
            return payload

        # Decapsulation
        elif direction == "decapsulation":
            return data["payload"]