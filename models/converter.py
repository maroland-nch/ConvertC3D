from abc import ABC, abstractmethod

class Converter(ABC):
    @abstractmethod
    def initialize(self, path):
        pass

    def set_source_path(self, path):
        pass

    @abstractmethod
    def is_running(self):
        pass

    @abstractmethod
    def is_finished(self):
        pass

    @abstractmethod
    def is_successful(self):
        pass

    def is_result_available(self):
        return self.is_finished() and self.is_successful()

    @abstractmethod
    def get_result(self):
        pass

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def force_stop(self):
        """ Stop the conversion operation in progress """
        pass

    @abstractmethod
    def on_finished(self, interrupted):
        """ Clean up conversion operation, whether interrupted or finished gracefully """
        pass