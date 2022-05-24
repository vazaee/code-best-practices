import abc


class BaseQueue(metaclass=abc.ABCMeta):
    code: int = 0
    queue = []
    customers_served = []
    current_number: str = ""

    def reset_queue(self) -> None:
        if self.code >= 200:
            self.code = 0
        else:
            self.code += 1

    def insert_customer(self):
        self.queue.append(self.current_number)

    @abc.abstractmethod
    def generate_current_number(self):
        ...

    def update_queue(self):
        self.reset_queue()
        self.generate_current_number()
        self.insert_customer()

    @abc.abstractmethod
    def call_customer(self, till: int):
        ...
