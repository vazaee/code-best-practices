class PriorityQueue:
    code: int = 0
    queue = []
    customers_served = []
    current_number: str = ""

    def generate_current_number(self) -> None:
        self.current_number = f'PR{self.code}'

    def reset_queue(self) -> None:
        if self.code >= 100:
            self.code = 0
        else:
            self.code += 1

    def update_queue(self) -> None:
        self.reset_queue()
        self.generate_current_number()
        self.queue.append(self.current_number)

    def call_customer(self, till: int) -> str:
        current_customer = self.queue.pop(0)
        self.customers_served.append(current_customer)
        return f'Current customer: {current_customer}, go to the till: {till}'

    def statistics(self, day: str, agency: int, flag: str) -> dict:
        if flag != 'detail':
            statistics = {f'{agency}-{day}': len(self.customers_served)}
        else:
            statistics = {}
            statistics['day'] = day
            statistics['agency'] = agency
            statistics['customers_served'] = self.customers_served
            statistics['n_customers_served'] = len(self.customers_served)

        return statistics
