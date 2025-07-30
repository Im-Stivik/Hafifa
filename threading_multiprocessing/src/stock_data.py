from typing import Dict, Any, Self

from pydantic import BaseModel

class Relevant(BaseModel):
    timestamp: str
    stock: float
    percentage_change: float

class StockData(BaseModel):
    Open: float
    High: float
    Low: float
    Close: float
    Volume: int
    Dividends: float
    timestamp: str

    def get_relevant_data(self) -> Relevant:
        percentage_change= ((self.Close - self.Open) / self.Open) * 100

        return Relevant(timestamp=self.timestamp, stock=self.Open, percentage_change=percentage_change)
