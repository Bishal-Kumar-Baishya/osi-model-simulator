class NetworkLayer:
    def __init__(self):
        self.src_ip = "192.168.1.5"
        self.dst_ip = "192.168.1.10"
    
    def process(self, data):
        data = data.copy()
        
        # Encapsulation
        if "src_ip" not in data:
            data["src_ip"] = self.src_ip
            data["dst_ip"] = self.dst_ip

        # Decapsulation
        else:
            data.pop("src_ip")
            data.pop("dst_ip")
        return data