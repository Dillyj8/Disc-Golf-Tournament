from io import TextIOWrapper


print("How many players are playing in the Disc Golf tournament? ")

def validate_scores(scores):
    if not scores or any(score < 1 or score > 10 for score in scores):
        print("Invalid score. Scores must be between 1 and 10.")
        return False
    return True

def get_scores(player):
    while True:
        try:
            scores = list(map(int, input(f"Enter scores for {player}: ").split()))
        except ValueError:
            print("Invalid input. Enter whole-number scores between 1 and 10.")
            continue
        if validate_scores(scores):
            return scores

while True:
    try:
        num_players = int(input("Enter the number of players (1-4): "))
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 4.")
        continue

    if num_players < 1 or num_players > 4:
        print("Invalid number of players. Please enter a number between 1 and 4.")
    else:
        break
players = []
for player_num in range(1, num_players + 1):
    players.append(input(f"Enter the name of Player {player_num}: "))

print("What was the score the player got for each hole? (Enter scores separated by spaces)")
player_scores = [get_scores(player) for player in players]

report_lines = ["Scores for each player:"]
for i, (player, scores) in enumerate(zip(players, player_scores)):
    report_lines.append(f"{player}: {scores}")
    average_score = sum(scores) / len(scores)
    report_lines.append(f"Average score for {player}: {average_score:.2f}")

report_lines.append(f"The winner is: {players[player_scores.index(max(player_scores))]}")
report_lines.append(
    f"The overrall average score for the tournament is: "
    f"{sum(sum(scores) for scores in player_scores) / sum(len(scores) for scores in player_scores):.2f}"
)
report_lines.append(
    f"The hardest hole was: "
    f"{max(range(len(player_scores[0])), key=lambda i: sum(scores[i] for scores in player_scores)) + 1}"
)

report = "\n\n".join(report_lines)
print(f"\n{report}")
with open("tournament_results.txt", "w", encoding="utf-8") as results_file:
    results_file.write(report + "\n")
print("\nAnalysis saved to tournament_results.text.")
