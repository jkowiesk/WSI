from twoPlayerGames.two_player_games.games.dots_and_boxes import DotsAndBoxes
from random import randint, shuffle
import copy as cp
MAX_RATING = 1000
static_depth = -1


def min_max(alpha: int, beta: int, curr_game: DotsAndBoxes, depth: int, best_move=(-1, -1)):
    global static_depth
    static_depth = depth
    moves_num = len(curr_game.state.get_moves())
    if depth == 0:
        return 0, curr_game.state.get_moves()[randint(0, moves_num - 1)]

    rating, best_move = min_max_recursive(alpha, beta, curr_game, depth)

    return rating, best_move


def min_max_recursive(alpha: int, beta: int, curr_game: DotsAndBoxes, depth: int, best_move=(-1, -1)):
    player1 = curr_game.first_player
    player2 = curr_game.second_player
    curr_player = curr_game.get_current_player()
    winner = curr_game.get_winner()
    game_moves = cp.copy(curr_game.get_moves())

    if winner:
        return (MAX_RATING, best_move) if winner.char == "1"\
          else (-1*MAX_RATING, best_move)

    if depth == 0 or curr_game.is_finished():
        score_player1 = curr_game.state.get_scores()[player1]
        score_player2 = curr_game.state.get_scores()[player2]
        return score_player1 - score_player2, best_move

    if static_depth == depth:
        shuffle(game_moves)     # change order of moves for root

    if curr_player.char == "1":
        maxRating = float('-inf')
        for move in game_moves:
            newGame = cp.copy(curr_game)
            newGame.make_move(move)
            rating, best_move = min_max_recursive(alpha, beta, newGame, depth - 1, best_move)
            if rating > maxRating:
                maxRating = rating
                alpha = max(maxRating, alpha)
                best_move = move if static_depth == depth else best_move
            if alpha >= beta:
                break
        return maxRating, best_move

    else:
        minRating = float('inf')
        for move in game_moves:
            newGame = cp.copy(curr_game)
            newGame.make_move(move)
            rating, best_move = min_max_recursive(alpha, beta, newGame, depth - 1, best_move)
            if rating < minRating:
                minRating = rating
                beta = min(minRating, beta)
                best_move = move if static_depth == depth else best_move
            if alpha >= beta:
                break
        return minRating, best_move
