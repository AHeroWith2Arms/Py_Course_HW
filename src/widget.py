from src.masks import get_mask_card_number, get_mask_account

def mask_account_and_card(card_data: str) -> str:
    if 'Счет' in card_data:
        return 'Счет ' + get_mask_account(card_data[5:])
    if 'Mastercard' in card_data or 'Visa' in card_data or 'Maestro' in card_data:

        return card_data[:-16] +  get_mask_card_number(card_data[-16:])
def get_date(card_data: str) -> str:
    input_date = card_data[:10]
    year, month, day = input_date.split('-')
    return f'{day}.{month}.{year}'
