from twoPlayerGames.two_player_games.games.dots_and_boxes\
                    import DotsAndBoxes, DotsAndBoxesMove
from utils.min_max import min_max


def main():
    game = DotsAndBoxes(2)
    game.make_move(DotsAndBoxesMove("v", (0, 0)))
    game.make_move(DotsAndBoxesMove("v", (0, 1)))
    game.make_move(DotsAndBoxesMove("v", (0, 2)))
    game.make_move(DotsAndBoxesMove("h", (0, 0)))
    game.make_move(DotsAndBoxesMove("h", (1, 0)))
    print(str(game))

    rating, best_move = min_max(float('-inf'), float('inf'), game, 2)
    print(str(game))
    game.make_move(best_move)

    print(str(game))

    if game.get_winner():
        print(game.get_winner().char)



if __name__ == "__main__":
    main()
