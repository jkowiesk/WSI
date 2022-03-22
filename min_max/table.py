from twoPlayerGames.two_player_games.games.dots_and_boxes\
                    import DotsAndBoxes
from utils.min_max import min_max
from utils.params import params
import numpy as np
from time import time
import csv

RANGE = 10


def main():
    fields = ["Player 1: Depth", "Wins", "Winrate", "Player 2: Depth",
              "Wins", "Winrate", "Board size", "Average Time"]
    with open("./csv/min_max_dots_game.csv", "w") as file:
        csvwriter = csv.writer(file)
        csvwriter.writerow(fields)
        j = 1

        for player1_depth, player2_depth, board_size in params:
            player1, player2 = 0, 0
            time_list = []
            for _ in range(RANGE):
                time_avg = 0
                prevTime = time()
                game = DotsAndBoxes(board_size)
                while not game.is_finished():
                    curr_player = game.get_current_player()
                    depth = player1_depth if curr_player.char == "1" else player2_depth

                    rating, best_move = min_max(float('-inf'), float('inf'), game, depth)
                    game.make_move(best_move)

                time_list.append(time() - prevTime)
                if game.get_winner():
                    if game.get_winner().char == "1":
                        player1 += 1
                    else:
                        player2 += 1
                else:
                    player1 += 0.5
                    player2 += 0.5
            print(j)
            for time_sample in time_list:
                time_avg += time_sample
            time_avg /= len(time_list)
            csvwriter.writerow([player1_depth, player1, np.around(player1/RANGE, 2) * 100,
                                player2_depth, player2, np.around(player2/RANGE, 2) * 100,
                                board_size, np.around(time_avg, 2)])
            j += 1


if __name__ == "__main__":
    main()
