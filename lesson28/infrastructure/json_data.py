class JsonInformation:
    def __init__(self):
        self.data_for_post = {
                "name": "Pug",
                "data": {
                    "year": 2023,
                    "price": 8000,
                    "color": "fawn",
                    "description": "All functionality old man: grunts, farts, drools"
                }
        }
        self.data_for_put = {
            "name": "Super-Pyper-Pug",
            "data": {
                "year": 2024,
                "price": "over-price"
            }
        }