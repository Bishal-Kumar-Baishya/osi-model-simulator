class SessionLayer:
    def __init__(self):
        self.session_id = "session_001"

    def process(self, data):
        data = data.copy()
        
        # Encapsulation
        if "session_id" not in data:
            data["session_id"] = self.session_id

        # Decapsulation
        else:
            data.pop("session_id")
        return data