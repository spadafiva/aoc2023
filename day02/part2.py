from dataclasses import dataclass, field

@dataclass
class ParsedGameSet:
    red: int = 0
    green: int = 0
    blue: int = 0

    def power(self) -> int:
        return self.red * self.green * self.blue

@dataclass
class ParsedGame:
    is_valid = True
    number: int
    game_sets: list[ParsedGameSet] = field(default_factory=list)

    def min_required_set(self) -> ParsedGameSet:
        min_red = 0
        min_blue = 0
        min_green = 0

        for set in self.game_sets:
            min_red = max(set.red, min_red)
            min_blue = max(set.blue, min_blue)
            min_green = max(set.green, min_green)
        
        return ParsedGameSet(red=min_red, blue=min_blue, green=min_green)

    def power(self) -> int:
        return self.min_required_set().power()


def solve(lines: list[str]):
    max_red = 12
    max_green = 13
    max_blue = 14

    sum = 0
    parsed_games = []

    for line in lines:
        game_and_contents = line.split(":")

        # get the game number
        game_number = int(str(game_and_contents[0])[4:])
        game_sets_data = [set.strip() for set in game_and_contents[1].split(";")]
        
        new_game = ParsedGame(game_number)
        parsed_sets = []

        # check all the draws in each set of the game
        for token_draws in game_sets_data:
            new_set = ParsedGameSet()
            for draw in [new_draw.strip() for new_draw in token_draws.split(",")]:
                if draw.endswith("green"):
                    new_set.green += int(draw.split(" ")[0])
                elif draw.endswith("blue"):
                    new_set.blue += int(draw.split(" ")[0])
                elif draw.endswith("red"):
                    new_set.red += int(draw.split(" ")[0])
                else:
                    print("unknown color")
            parsed_sets.append(new_set)

            ## check that set is valid
            if new_set.green > max_green:
                new_game.is_valid = False
            elif new_set.blue > max_blue:
                new_game.is_valid = False
            elif new_set.red > max_red:
                new_game.is_valid = False

        new_game.game_sets = parsed_sets
        parsed_games.append(new_game)
        sum += new_game.power()
        # if new_game.is_valid:
        #     sum += new_game.number

    print(sum)
    # print(parsed_games)
    