import random

def player(prev_play, opponent_history=[]):
    # Initialize opponent_history if it's the first move
    if not opponent_history:
        opponent_history.extend(["", "", ""])

    # Update opponent_history with the previous play
    if prev_play != "":
        opponent_history.append(prev_play)

    # Define the possible moves
    moves = ["R", "P", "S"]

    # Define the counters for each move
    counters = {"R": "P", "P": "S", "S": "R"}

    # Predict the next move based on the most frequent pattern
    guess = "R"  # Default guess
    if len(opponent_history) > 3:
        # Look at the last three moves and predict the next move
        last_three = "".join(opponent_history[-3:])
        potential_plays = [
            last_three + "R",
            last_three + "P",
            last_three + "S"
        ]

        # Count the occurrences of each potential play in the history
        counts = {play: "".join(opponent_history).count(play) for play in potential_plays}

        # Predict the most frequent play
        guess = max(potential_plays, key=counts.get)[-1]

    # Return the counter to the predicted move
    return counters[guess]