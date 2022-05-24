from typing import List, Dict, Union


class DetailedStatistics:
    def __init__(self, day: str, agency: int) -> None:
        self.day = day
        self.agency = agency

    def run_statistics(self, customers_served: List[str]) -> dict:
        statistics: Dict[str, Union[List[str], str, int]] = {}

        statistics['day'] = self.day
        statistics['agency'] = self.agency
        statistics['customers_served'] = customers_served
        statistics['number_customers_served'] = (
            len(customers_served)
        )

        return statistics
