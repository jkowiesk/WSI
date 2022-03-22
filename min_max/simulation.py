from twoPlayerGames.two_player_games.games.dots_and_boxes\
                    import DotsAndBoxes
from utils.min_max import min_max


def main():
    player1_depth = int(input("Player 1 Depth: "))
    player2_depth = int(input("Player 2 Depth: "))
    board_size = int(input("Board Size: "))
    player1 = 0
    player2 = 0
    for _ in range(10):
        game = DotsAndBoxes(board_size)
        for __ in game.state.get_moves():
            if game.get_current_player().char == "2":
                rating, best_move = min_max(float('-inf'), float('inf'), game, player2_depth)
            else:
                rating, best_move = min_max(float('-inf'), float('inf'), game, player1_depth)
            game.make_move(best_move)
            print(rating)
            print(str(game))

        if game.get_winner():
            if game.get_winner().char == "1":
                player1 += 1
            else:
                player2 += 1
        else:
            player1 += 0.5
            player2 += 0.5
    print("||      WINS        ||")
    print(f"Player 1: {player1}")
    print(f"Player 2: {player2}")


if __name__ == "__main__":
    main()
