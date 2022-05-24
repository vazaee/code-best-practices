from base_queue import BaseQueue


class PriorityQueue(BaseQueue):

    def generate_current_number(self) -> None:
        self.current_number = f'PR{self.code}'

    def call_customer(self, till: int) -> str:
        current_customer: str = self.queue.pop(0)
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
            statistics['number_customers_served'] = (
                len(self.customers_served)
            )

        return statistics
