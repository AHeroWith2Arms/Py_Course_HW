from datetime import datetime

"""Функции сортировки транзакций"""


def filter_by_state(transactions: dict, state: str="EXECUTED") -> list[dict]:
    return [transaction for transaction in transactions if transaction.get("state") == state]


def sort_by_date(transactions: dict) -> list[dict]:
    return sorted(transactions, key=lambda x: datetime.strptime(x["date"], "%Y-%m-%dT%H:%M:%S.%f"))
