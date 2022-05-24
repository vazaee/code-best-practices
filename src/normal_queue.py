from typing import Union

from base_queue import BaseQueue
from constants import NORMAL_CODE
from summary_statistics import SummaryStatistics
from detailed_statistics import DetailedStatistics

Classes = Union[SummaryStatistics, DetailedStatistics]


class NormalQueue(BaseQueue):

    def generate_current_number(self) -> None:
        self.current_number = f'{NORMAL_CODE}{self.code}'

    def call_customer(self, till: int) -> str:
        current_customer = self.queue.pop(0)
        self.customers_served.append(current_customer)
        return f'Current customer: {current_customer}, go to the till: {till}'

    def statistics(self, return_statistics: Classes) -> dict:
        return return_statistics.run_statistics(self.customers_served)
