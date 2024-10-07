class CellPhone:
    def __init__(self, manufact, model, retail_price):
        self._manufact = manufact
        self._model = model
        self._retail_price = retail_price

    def set_manufact(self, manufact):
        self._manufact = manufact

    def set_model(self, model):
        self._model = model

    def set_retail_price(self, retail_price):
        self._retail_price = retail_price
    
    def get_manufact(self):
        return self._manufact
    
    def get_model(self):
        return self._model
    
    def get_retail_price(self):
        return self._retail_price