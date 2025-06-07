def evaluate_hand(hole_cards, board_cards):
    if "??" in hole_cards:
        return "Card detection failed — try a clearer screenshot."

    if "AS" in hole_cards and "KS" in hole_cards:
        return "Premium hand! Go All In!"
    if board_cards.count("5C") >= 2:
        return "Dangerous board — Check or Fold"
    return "Standard situation — Play cautiously"
