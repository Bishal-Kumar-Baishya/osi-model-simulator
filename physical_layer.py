class PhysicalLayer:
    def process(self, data, direction):
        payload = {}
        
        # Encapsulation
        if direction == "encapsulation":
            payload["payload"] = data
            result = data["payload"]["payload"]["payload"]["data"].encode().hex()
            payload["frame"] = result
            return payload
        
        # Decapsulation
        elif direction == "decapsulation":
            return data["payload"]