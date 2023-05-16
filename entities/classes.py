from dataclasses import dataclass
from decimal import Decimal
from typing import Union

from currency_converter import CurrencyConverter


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

    def __init__(
        self, symbol, price_paid, shares, name, price, currency, cost_basis, market_value, gain, *args, **kwargs
    ):
        self.symbol = symbol
        self.price_paid = price_paid
        self.shares = shares
        self.name = name
        self.price = price
        self.currency = currency
        self.cost_basis = cost_basis
        self.market_value = market_value
        self.gain = gain


@dataclass(frozen=True)
class Currency:
    """Currency class"""

    code: str
    symbol: str

    def __str__(self):
        return f"{self.code} ({self.symbol})"

    def __repr__(self):
        return f"Currency('{self.code}', '{self.symbol}')"


CURRENCIES = {"USD": Currency("USD", "$"), "INR": Currency("INR", "₹"), "EUR": Currency("EUR", "€")}


@dataclass
class Amount:
    """Amount class"""

    price: Union[int, float, Decimal]
    currency: Currency = CURRENCIES["USD"]

    def __str__(self):
        return f"{self.currency.symbol} {self.price}"


@dataclass
class ConversionRate:
    from_currency: str
    to_currency: str

    def __post_init__(self):
        self.value = self._get_value()

    def _get_value(self):
        """
        Conversion rate for 1 dollar if the from_currency = USD.
        """
        c = CurrencyConverter()
        conversion_rate = c.convert(1, self.from_currency, self.to_currency)
        return conversion_rate

    def convert(self, amount) -> float:
        return self.value * amount
