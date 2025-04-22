from src.masks import get_mask_card_number, get_mask_account

"""Возвращает замаскированные данные карты"""


def mask_account_and_card(card_data: str) -> str or None:
    if "Счет" in card_data:
        return str("Счет " + get_mask_account(card_data[5:]))
    elif "Mastercard" in card_data or "Visa" in card_data or "Maestro" in card_data:
        return str(card_data[:-16] + get_mask_card_number(card_data[-16:]))
    return None




def get_date(card_data: str) -> str:
    input_date = card_data[:10]
    year, month, day = input_date.split("-")
    return f"{day}.{month}.{year}"
