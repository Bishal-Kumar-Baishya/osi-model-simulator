import random

class TransportLayer:
    def __init__(self):
        self.app_port_mapping = {
                "messaging": 9000,
                "http": 80,
                "https": 443,
                "dns": 53
            }

    def process(self, data, direction):
        payload = {}
        
        # Encapsulation
        if direction == "encapsulation":
            payload["payload"] = data
            src_port = random.randint(1024, 65535)
            dst_port = self.app_port_mapping[data["payload"]["app_type"]]
            payload["src_port"] = src_port
            payload["dst_port"] = dst_port
            return payload
        
        # Decapsulation
        elif direction == "decapsulation":
            return data["payload"]