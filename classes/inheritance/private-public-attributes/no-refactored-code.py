from abc import ABC
from abc import abstractmethod
import datetime



class DiscountCalculator(ABC):
    @abstractmethod
    def get_price_apply_discount(self, price: float) -> float:
        pass


class BigDiscountCalculator(DiscountCalculator):
    def get_price_apply_discount(self, price: float) -> float:
        result = price/2
        return self._get_price_apply_special_discount(result)

    def _get_price_apply_special_discount(self, price: float) -> float:
        return price/2 if self._is_today_weekend else price

    @property
    def _is_today_weekend(self) -> bool:
        return datetime.datetime.today().weekday() >= 5


class SmallDiscountCalculator(DiscountCalculator):
    def get_price_apply_discount(self, price: float) -> float:
        result = price/4
        return self._get_price_apply_special_discount(result)

    def _get_price_apply_special_discount(self, price: float) -> float:
        return price/2 if self._is_today_weekend else price

    @property
    def _is_today_weekend(self) -> bool:
        return datetime.datetime.today().weekday() >= 5
