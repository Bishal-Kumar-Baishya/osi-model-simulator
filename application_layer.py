from datetime import datetime

class ApplicationLayer:
    def __init__(self, user_A, user_B, app_type):
        self.user_A = user_A
        self.user_B = user_B
        self.app_type = app_type

    def process(self, data, direction):
        if direction == "encapsulation":
            results = {"data": data,
                "sender": self.user_A,
                "recipient": self.user_B,
                "app_type": self.app_type,
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            return results
        elif direction == "decapsulation":
            return data["data"]