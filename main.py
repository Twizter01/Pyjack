import os
import time

from animations.card_animations import animate_asset
from assets.ascii_art import *
from cli.game_promtps import intro
from generators import number_generator, symbol_generator, intro_bet
from assets.cards_creator import face_down_card_maker, face_up_card_maker
from constants import card_template
from cli.player_prompts import player_intro_bet
from assets.blackjack_moves import moves
from core.player import Player

# === GAME OBJECTS ===
player = Player()
player.is_playing = True


def main() -> None:

    intro() # This prints the devil girl and loading thingy, its shit tbh
    intro_bet() # This prints the bets panels
    player_intro_bet(player)
    
    print(face_down_card_maker())

    player.initial_move()
    player.display_cards()

    moves() # Prints the available moves
    action = player.move()
    player.check_action(action)
    player.display_cards()

if __name__ == "__main__":
    main()


