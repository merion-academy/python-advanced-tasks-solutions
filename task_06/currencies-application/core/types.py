from dataclasses import dataclass
from datetime import date
from decimal import Decimal
from typing import TypedDict


class ResponseType(TypedDict):
    date: str
    values: dict[str, Decimal]


@dataclass(frozen=True)
class CurrencyValue:
    currency: str
    value: Decimal


@dataclass(frozen=True)
class CurrencyInfo:
    date: date
    currency: str
    values: list[CurrencyValue]

    @classmethod
    def from_currency_info_response(
        cls,
        info: ResponseType,
        source_currency: str,
        target_currencies: set[str],
    ) -> "CurrencyInfo":
        return cls(
            date=date.fromisoformat(info["date"]),
            currency=source_currency,
            values=[
                # prepare object
                CurrencyValue(currency=name, value=value)
                # read all items
                for name, value in info["values"].items()
                # filter out those which are not in our target
                if name in target_currencies
            ],
        )
