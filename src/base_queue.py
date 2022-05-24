import abc
from typing import List

from constants import MAX_SIZE, MIN_SIZE


class BaseQueue(metaclass=abc.ABCMeta):
    code: int = 0
    queue: List[str] = []
    customers_served: List[str] = []
    current_number: str = ""

    def reset_queue(self) -> None:
        if self.code >= MAX_SIZE:
            self.code = MIN_SIZE
        else:
            self.code += 1

    def insert_customer(self) -> None:
        self.queue.append(self.current_number)

    @abc.abstractmethod
    def generate_current_number(self) -> None:
        ...

    def update_queue(self) -> None:
        self.reset_queue()
        self.generate_current_number()
        self.insert_customer()

    @abc.abstractmethod
    def call_customer(self, till: int) -> str:
        ...
