from utils.input_helpers import get_input_for as read_day
import importlib



def run_day(day: int, sample: bool, part1: bool):
    # # get day input and sample
    # print("Day number:", end="")
    # day = int(input())

    # print("Use sample (y/n): ", end="")
    # sample = bool(input() == "y")
    # print('HI')

    # get lines for the input
    part_number = 1 if part1 else 2
    lines = read_day(day, sample, part_number)

    # find the code for the day
    part_number = '1' if part1 else '2'
    day_module = importlib.import_module(f"day{day:02}.part{part_number}")
    solve = getattr(day_module, 'solve')

    # run the solution
    solve(lines)

if __name__ == "__main__":
    print("To run, use the command  `python3 -c \"import aoc; aoc.run_day(day=<day_number>, sample=<sample>, part1=<part>)\"`")
