

class Processor:
    def __init__(self):
        self._coef = 0.0
    def add_process(self, process):
        self._coef += process
    def get_coef(self):
        return self._coef