from copy import deepcopy
scoring= {'p': 1,
          'n': 3,
          'b': 3,
          'r': 5,
          'q': 9,
          'k': 100,
          'P': -1,
          'N': -3,
          'B': -3,
          'R': -5,
          'Q': -9,
          'K': -100,
          }
def fen_to_board(fen):
    board = {}
    ranks = fen.split(' ')[0].split('/')

    for i, rank in enumerate(ranks):
        file_num = 1
        for char in rank:
            if char.isnumeric():
                file_num += int(char)
            else:
                piece = char
                board.setdefault(piece, []).append(f"{chr(ord('a') + file_num - 1)}{8 - i}")
                file_num += 1

    return board

def eval_board(BOARD):
    score = 0
    pieces = BOARD.piece_map()

    for key in pieces:
        score += scoring[str(pieces[key])]

    return score

def most_value_agent(BOARD, forcolor):

    moves = list(BOARD.legal_moves)
    scores = []
    best_move = None
    for move in moves:
        #creates a copy of BOARD so we dont
        #change the original class
        temp = deepcopy(BOARD)
        temp.push(move)

        scores.append(eval_board(temp))

        if forcolor == "white":
            best_move = moves[scores.index(min(scores))]
        else:
            best_move = moves[scores.index(max(scores))]
    return best_move



def MinMax_Check(BOARD):
    moves = list(BOARD.legal_moves)
    scores = []

    for move in moves:
        temp = deepcopy(BOARD)
        temp.push(move)
        #black move ended

        forwhitemove = most_value_agent(temp, "white")
        # white move ended
        if forwhitemove is None:
            continue
        temp.push(forwhitemove)

        fornextbackmove = most_value_agent(temp, "black")
        # next black move ended
        if fornextbackmove is None:
            continue
        temp.push(fornextbackmove)

        forwhitemove = most_value_agent(temp, "white")
        # white move ended
        if forwhitemove is None:
            continue
        temp.push(forwhitemove)

        fornextbackmove = most_value_agent(temp, "black")
        # next black move ended
        if fornextbackmove is None:
            continue
        temp.push(fornextbackmove)

        forwhitemove = most_value_agent(temp, "white")
        # white move ended
        if forwhitemove is None:
            continue
        temp.push(forwhitemove)

        fornextbackmove = most_value_agent(temp, "black")
        # next black move ended
        if fornextbackmove is None:
            continue
        temp.push(fornextbackmove)

        forwhitemove = most_value_agent(temp, "white")
        # white move ended
        if forwhitemove is None:
            continue
        temp.push(forwhitemove)

        fornextbackmove = most_value_agent(temp, "black")
        # next black move ended
        if fornextbackmove is None:
            continue
        temp.push(fornextbackmove)

        forwhitemove = most_value_agent(temp, "white")
        # white move ended
        if forwhitemove is None:
            continue
        temp.push(forwhitemove)

        fornextbackmove = most_value_agent(temp, "black")
        # next black move ended
        if fornextbackmove is None:
            continue
        temp.push(fornextbackmove)

        scores.append(eval_board(temp))
    if len(scores) == 0 and len(moves) == 1:
        bestmove = moves[0]
    else:
        bestmove = moves[scores.index(max(scores))]

    return bestmove