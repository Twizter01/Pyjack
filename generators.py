from random import choice

from constants import card_numbers, symbols
from assets.bet_panels import bet_panel


def number_generator() -> str:
    random_card = choice(list(card_numbers.keys()))
    return str(random_card)

def symbol_generator() -> str:
    random_symbol = choice(list(symbols))
    return str(random_symbol)

def intro_bet() -> None:
    print(f"{bet_panel('10')}", end='')
    print(f"{bet_panel('50')}", end='')
    print(f"{bet_panel('100')}", end='')
    print(f"{bet_panel('200')}", end='')   
    print(f"{bet_panel('500')}", end='')
    print(f"{bet_panel('1000')}", end='')


def panel_maker(panel_str: str) -> str | None:
    if not panel_str:
        raise ValueError("Panel string is empty")
    
    lines = [line.split('\n') for line in panel_str]
    max_lines = max(len(p) for p in lines)

