class NormalQueue:
    code: int = 0
    queue = []
    customers_served = []
    current_number: str = ""

    def generate_current_number(self) -> None:
        self.current_number = f'NM{self.code}'

    def reset_queue(self):
        if self.code >= 100:
            self.code = 0
        else:
            self.code += 1

    def update_queue(self):
        self.reset_queue()
        self.generate_current_number()
        self.queue.append(self.current_number)

    def call_customer(self, till: int) -> str:
        current_customer = self.queue.pop(0)
        self.customers_served.append(current_customer)
        return f'Current customer: {current_customer}, go to the till: {till}'
