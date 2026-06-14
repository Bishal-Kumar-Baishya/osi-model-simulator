class PhysicalLayer:
    def process(self, data):
        data = data.copy()
        
        # Encapsulation
        if "frame" not in data:
            result = data["data"].encode().hex()
            data["frame"] = result
        
        # Decapsulation
        else:
            data.pop("frame")
        return data