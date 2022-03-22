from twoPlayerGames.two_player_games.games.dots_and_boxes\
                    import DotsAndBoxes, DotsAndBoxesMove
from utils.min_max import min_max


def main():
    game = DotsAndBoxes(3)
    for _ in game.state.get_moves():
        is_wrong_move = False
        if game.get_current_player().char == "2":
            rating, move = min_max(float('-inf'), float('inf'), game, 3)
            game.make_move(move)
        else:
            print(str(game))
            while not is_wrong_move:
                is_wrong_move = True
                items = input("con and loc: ").split(" ")
                con = items[0]
                loc = tuple([int(x) for x in items[1:]])
                try:
                    game.make_move(DotsAndBoxesMove(con, loc))
                except Exception:
                    is_wrong_move = False
                    print("Wrong Move, example: (v 0 0)")

    print(str(game))

    if game.get_winner():
        print(game.get_winner().char)


if __name__ == "__main__":
    main()
