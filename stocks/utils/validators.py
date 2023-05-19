from requests.exceptions import RequestException

from stocks.utils.get_price import get_stock_info


def is_valid_stock_symbol(stock_symbol) -> bool:
    """
    Checks for stock symbol valid or not.

    Args:
        stock_symbol (str): Stock Symbol, ex: AAPL
    """
    try:
        info = get_stock_info(stock_symbol=stock_symbol)
        if info.get("shortName"):
            return True
    except RequestException:
        return False
    return False
