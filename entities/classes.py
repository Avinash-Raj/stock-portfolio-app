from dataclasses import dataclass
from typing import Union
from decimal import Decimal
from forex_python.converter import CurrencyRates


@dataclass
class StockItem:
    """DB stock item"""

    symbol: str
    price_paid: float
    shares: int
    name: str
    price: float
    currency: str
    cost_basis: float
    market_value: float
    gain: float


@dataclass(frozen=True)
class Currency:
    """Currency class"""

    code: str
    symbol: str

    def __str__(self):
        return f"{self.code} ({self.symbol})"

    def __repr__(self):
        return f"Currency('{self.code}', '{self.symbol}')"


CURRENCIES = {"USD": Currency("USD", "$"), "INR": Currency("INR", "₹")}


@dataclass
class Amount:
    """Amount class"""

    price: Union[int, float, Decimal]
    currency: Currency = CURRENCIES["USD"]

    def convert_to(self, to_currency: Union[Currency, str]) -> "Amount":
        currency_rate = CurrencyRates(force_decimal=True)
        currency = to_currency if isinstance(to_currency, Currency) else CURRENCIES[to_currency]
        final_amount = currency_rate.convert(self.currency.code, currency.code, self.price)
        return Amount(price=final_amount, currency=currency)
