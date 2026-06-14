import random

class TransportLayer:
    def __init__(self):
        self.app_port_mapping = {
                "messaging": 9000,
                "http": 80,
                "https": 443,
                "dns": 53
            }

    def process(self, data):
        data = data.copy()
        
        # Encapsulation
        if "src_port" not in data:
            src_port = random.randint(1024, 65535)
            dst_port = self.app_port_mapping[data["app_type"]]
            data["src_port"] = src_port
            data["dst_port"] = dst_port
        
        # Decapsulation
        else:
            data.pop("src_port")
            data.pop("dst_port")
        return data