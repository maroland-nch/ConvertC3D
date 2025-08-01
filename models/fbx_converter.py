from models.converter import ConversionOperation, Converter

class FbxConverterOperation(ConversionOperation):
    def 

class FbxConverter(Converter):
    def create_operation(self):
        """ Create the specific implementation of a ConversionOperation """
        pass

    def start(self):
        """ Start the converter operation """
        pass

    def force_stop(self):
        """ Stop the conversion operation in progress """
        pass

    def on_finished(self, interrupted):
        """ Clean up conversion operation, whether interrupted or finished gracefully """
        pass