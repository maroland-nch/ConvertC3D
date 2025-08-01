from models.converter import ConversionOperation, Converter

class SummaryConvertOperation(ConversionOperation):
    def start(self):
        """ Start the converter operation """
        self._running = True

    def force_stop(self):
        """ Stop the converter operation in progress """
        self._running = False
        self._successful = False
        self._finished = True
        self.on_finished(True)

    def on_finished(self, interrupted):
        """ Clean up converter operation, whether interrupted or finished gracefully """
        self._running = False

        if interrupted is False and self._owner is not None:
            self._owner.on_finished()

class SummaryConverter(Converter):
    def create_operation(self):
        """ Create the specific implementation of a ConversionOperation """
        operation = SummaryConvertOperation()
        operation.initialize(self, self._source_path)
        return operation

    def on_finished(self, interrupted):
        """ Clean up conversion operation, whether interrupted or finished gracefully """
        pass