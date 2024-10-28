class ElementFoundException(Exception):
    def __init__(self, element, message='Element is found, but shouldnt'):
        self.element = element
        self.message = f'{message} {element}'
        super().__init__(self.message)