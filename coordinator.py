class Coordinator:
    def __init__(self):
        self.layers = []

    def add_layer(self, layer):
        self.layers.append(layer)

    def send(self, data):
        results = {}
        for layer in self.layers:
            result = layer.process(data)
            layer_name = layer.__class__.__name__   # getting the layer's class name
            results[layer_name] = result            # storing in dictionary
            data = result                           # updating data for next layer
        return results
    
    def receive(self, wrapped_data):
        res_receive = {}
        data = wrapped_data
        for layer in reversed(self.layers):
            result = layer.process(data)
            layer_name = layer.__class__.__name__
            res_receive[layer_name] = result
            data = result
        return res_receive