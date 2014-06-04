def checkio(game_result):

    if "OOO" in game_result:
        return "O"

    elif "XXX" in game_result:
        return "X"

    elif game_result[0][0] == game_result[1][1] == game_result[2][2] and game_result[1][1] != ".":
        return game_result[1][1]

    elif game_result[0][2] == game_result[1][1] == game_result[2][0] and game_result[1][1] != ".":
        return game_result[1][1]

    else:
        for i in range(len(game_result)):
            if game_result[0][i] == game_result[1][i] == game_result[2][i] and game_result[1][i] != ".":
                return game_result[0][i]

    return "D"



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "OOO",
        "XX.",
        ".XX"]) == "O"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X"
