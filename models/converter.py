from abc import ABC, abstractmethod

class ConversionOperation(ABC):
    def initialize(self, owner, path):
        self.set_owner(owner)
        self.set_source_path(path)
        self._running = False
        self._finished = False
        self._successful = False
        self._result = None

    def set_owner(self, owner):
        if owner:
            self._owner = owner

    def set_source_path(self, path):
        if path:
            self._source_path = path
    
    def get_is_running(self):
        return self._running
    
    def get_is_finished(self):
        return self._finished
    
    def get_is_successful(self):
        return self._successful
    
    def get_result(self):
        return self._result
    
    @abstractmethod
    def start(self):
        """ Start the converter operation """
        pass

    @abstractmethod
    def force_stop(self):
        """ Stop the converter operation in progress """
        pass

    @abstractmethod
    def on_finished(self, interrupted):
        """ Clean up converter operation, whether interrupted or finished gracefully """
        pass

class Converter(ABC):
    def initialize(self, path):
        self.set_source_path(path)
        self._operation: ConversionOperation = None

    def set_source_path(self, path):
        if path:
            self._source_path = path

    def is_running(self):
        if self._operation is None:
            return False
        return self._operation.get_is_running()

    def is_finished(self):
        if self._operation is None:
            return False
        return self._operation.get_is_finished()

    def is_successful(self):
        if self._operation is None:
            return False
        return self._operation.get_is_successful()
    
    def is_result_available(self):
        return self.is_finished() and self.is_successful()
    
    def get_result(self):
        if self._operation is None:
            return None
        if self.is_result_available() is False:
            return None
        
        return self._operation.get_result()
    
    def start(self):
        """ Start the converter operation """
        if self._operation is None:
            self._operation = self.create_operation()
        
        if self._operation.get_is_running():
            return

        if self._operation.get_is_finished():
            return
        
        self._operation.start()

    def force_stop(self):
        if self._operation is None:
            return
        
        if self._operation.get_is_finished():
            return
        
        if self._operation.get_is_running() is False:
            return
        
        self._operation.force_stop()
        self.on_finished()

    @abstractmethod
    def create_operation(self):
        """ Create the specific implementation of a ConversionOperation """
        pass

    @abstractmethod
    def on_finished(self, interrupted):
        """ Clean up conversion operation, whether interrupted or finished gracefully """
        pass