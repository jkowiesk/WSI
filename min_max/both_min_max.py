from twoPlayerGames.two_player_games.games.dots_and_boxes\
                    import DotsAndBoxes
from utils.min_max import min_max


def main():
    game = DotsAndBoxes(3)
    for _ in game.state.get_moves():
        if game.get_current_player().char == "2":
            rating, best_move = min_max(float('-inf'), float('inf'), game, 4)
        else:
            rating, best_move = min_max(float('-inf'), float('inf'), game, 4)
        print(str(game))
        print(rating)
        game.make_move(best_move)
    print(str(game))

    if game.get_winner():
        print(game.get_winner().char)


if __name__ == "__main__":
    main()
