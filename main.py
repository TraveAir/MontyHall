from dataclasses import dataclass
import random


# PLAYER_SWITCHES = True

NUM_GAMES = 1_000_000


@dataclass
class Door:
    prize: str = "goat"
    is_open: bool = False


def setup_new_game():
    doors = [Door(), Door(), Door()]
    doors[random.randint(0, 2)].prize = "car"
    return doors


def open_empty_door(doors, choice):
    # make a list of 0, 1, and 2 in a random order
    possible_doors = [0, 1, 2]
    random.shuffle(possible_doors)

    for door in possible_doors:
        if doors[door].prize == "goat" and door != choice:
            return door


def switch_doors_or_not(doors, choice):
    if random.randint(0, 1) == 1:
        for door in [0, 1, 2]:
            if door != choice and doors[door].is_open is False:
                return door
    else:
        return choice


def determine_if_win(doors, choice):
    if doors[choice].prize == "car":
        return True
    else:
        return False


def write_to_file(game_num, doors, choice, changed_doors, won):
    with open("results.csv", "a") as f:
        f.write(
            f"{game_num},{doors[0].prize},{doors[1].prize},{doors[2].prize},{choice},{changed_doors},{won}\n"
        )


def create_file():
    with open("results.csv", "w") as f:
        f.write("game_number,door1,door2,door3,choice,changed_doors,won\n")


def game_loop(game_num):
    doors = setup_new_game()
    choice = random.randint(0, 2)
    doors[open_empty_door(doors, choice)].is_open = True
    old_choice = choice
    choice = switch_doors_or_not(doors, choice)
    if choice != old_choice:
        changed_doors = True
    else:
        changed_doors = False
    won = determine_if_win(doors, choice)
    write_to_file(game_num, doors, choice, changed_doors, won)


def main():
    create_file()
    for game_num in range(NUM_GAMES):
        game_loop(game_num + 1)


if __name__ == "__main__":
    main()
