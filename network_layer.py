class NetworkLayer:
    def __init__(self):
        self.src_ip = "192.168.1.5"
        self.dst_ip = "192.168.1.10"
    
    def process(self, data, direction):
        payload = {}
        
        # Encapsulation
        if direction == "encapsulation":
            payload["payload"] = data
            payload["src_ip"] = self.src_ip
            payload["dst_ip"] = self.dst_ip
            return payload

        # Decapsulation
        elif direction == "decapsulation":
            return data["payload"]