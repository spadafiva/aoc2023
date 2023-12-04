from utils.input_helpers import get_input_for as read_day
import importlib

# get day input and sample
print("Day number:", end="")
day = int(input())

print("Use sample (y/n): ", end="")
sample = bool(input() == "y")

# get lines for the input
lines = read_day(day, sample)

# find the code for the day
day_module = importlib.import_module(f"day{day:02}.part1")
solve = getattr(day_module, 'solve')

# run the solution
solve(lines)