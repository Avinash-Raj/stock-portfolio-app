from decimal import Decimal
from typing import Optional

from requests.exceptions import RequestException

from stocks.entities import StockItem

from .get_price import get_stock_info


def create_stock_item(symbol: str, price_paid: float, quantity: int) -> Optional[StockItem]:
    """
    Helps to create instance of Stock Item class.

    Args:
        symbol (str): stock symbol
        price (float): purchase price
        quantity (int): number of shares
    """
    try:
        info = get_stock_info(stock_symbol=symbol)
    except RequestException:
        return None
    if "shortName" not in info:
        return None

    cost_basis = price_paid * quantity
    market_value = info["currentPrice"] * quantity
    gain = market_value - cost_basis
    return StockItem(
        **{
            "symbol": symbol,
            "price_paid": price_paid,
            "shares": quantity,
            "name": info["shortName"],
            "price": info["currentPrice"],
            "currency": info["currency"],
            "cost_basis": round(cost_basis, 2),
            "market_value": round(market_value),
            "gain": round(gain, 2),
        }
    )


def update_stock_info(stock: StockItem) -> StockItem:
    """
    Helps to update stock item with cost_basis, market_value, gain
    """
    purchase_price = stock.price_paid
    stock_info = get_stock_info(stock.symbol)
    quantity = stock.shares
    name = stock_info["shortName"]
    price = stock_info["currentPrice"]
    currency = stock_info["currency"]
    cost_basis = purchase_price * quantity
    market_value = price * quantity
    gain = market_value - cost_basis
    stock.name = name
    stock.price = price
    stock.cost_basis = round(cost_basis, 2)
    stock.market_value = round(market_value, 2)
    stock.currency = currency
    stock.gain = round(gain, 2)
    return stock
