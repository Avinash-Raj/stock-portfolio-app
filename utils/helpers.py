from entities import StockItem
from .get_price import get_stock_info


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
    stock.cost_basis = cost_basis
    stock.market_value = market_value
    stock.currency = currency
    stock.gain = gain
    return stock
