from pydantic import BaseModel


class StockSettings(BaseModel):
    name: str
    stock_name: str
    output_file: str
    dates_file: str