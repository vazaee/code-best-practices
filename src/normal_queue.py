from base_queue import BaseQueue
from constants import NORMAL_CODE


class NormalQueue(BaseQueue):

    def generate_current_number(self) -> None:
        self.current_number = f'{NORMAL_CODE}{self.code}'

    def call_customer(self, till: int) -> str:
        current_customer = self.queue.pop(0)
        self.customers_served.append(current_customer)
        return f'Current customer: {current_customer}, go to the till: {till}'
