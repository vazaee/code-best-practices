from typing import List, Dict, Union


class SummaryStatistics:
    def __init__(self, day: str, agency: int) -> None:
        self.day = day
        self.agency = agency

    def run_statistics(self, customers_served: List[str]) -> dict:
        statistics: Dict[str, Union[List[str], str, int]] = {}

        statistics[f'{self.agency}-{self.day}'] = len(customers_served)

        return statistics
