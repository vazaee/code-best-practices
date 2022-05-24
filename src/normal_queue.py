from base_queue import BaseQueue


class NormalQueue(BaseQueue):

    def generate_current_number(self) -> None:
        self.current_number = f'NM{self.code}'

    def update_queue(self):
        self.reset_queue()
        self.generate_current_number()
        self.queue.append(self.current_number)

    def call_customer(self, till: int) -> str:
        current_customer = self.queue.pop(0)
        self.customers_served.append(current_customer)
        return f'Current customer: {current_customer}, go to the till: {till}'
