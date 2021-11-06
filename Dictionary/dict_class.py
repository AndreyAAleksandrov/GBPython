class Auto:
    # Параметр, который используется по всему классу
    auto_count = 0
    def __init__(self, auto_brand, auto_model):
        '''
        Используется в качестве документации

        :param auto_brand: string
        :param auto_model: string
        '''
        self.auto_brand = auto_brand
        self.auto_model = auto_model


