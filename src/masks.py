def get_mask_card_number(card_number):
    """Возвращает замаскированный номер карты и проверяет соотвествие требованиям"""
    if len(card_number) != 16 or not card_number.isdigit():
        return None

    masked = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    return masked


def get_mask_account(account_number):
    """Возвращает замаскированный номер счёта и проверяет соотвествие требованиям"""
    if len(account_number) < 4 or not account_number.isdigit():
        return None

    masked = f"**{account_number[-4:]}"
    return masked
