import re

def is_adjacent(number, symbol) -> bool:
    min_row = max(number['row'] - 1, 0)
    min_col = max(number['start'] - 1, 0)
    max_row = number['row'] + 1
    max_col = number['end'] + 1
    symbol_row = symbol['row']
    symbol_col = symbol['col']
    return symbol_row >= min_row and symbol_row <= max_row and symbol_col >= min_col and symbol_col <= max_col

def gear_ratio(symbol, numbers) -> int:
    adjacent_numbers = [number for number in numbers if is_adjacent(symbol=symbol, number=number)]
    is_gear = len(adjacent_numbers) == 2
    if is_gear:
        gear_ratio = adjacent_numbers[0]['value'] * adjacent_numbers[1]['value']
        return gear_ratio
    else:
        return 0


def solve(lines: list[str]):
    symbol_locations = []
    numbers = []

    # go through list and find all the symbol and number locations
    for line_idx, line in enumerate(lines):
        next_num_start = -1

        for char_idx, char in enumerate(line):
            try:
                int(char)
                if next_num_start == -1:
                    next_num_start = char_idx
                if char_idx == len(line) -1:
                    if next_num_start != -1:
                        numbers.append({ 'row': line_idx, 'start': next_num_start, 'end': char_idx, 'value': int(line[next_num_start : char_idx + 1])})
            except:
                next_num_end = char_idx
                if next_num_start != -1:
                    numbers.append({ 'row': line_idx, 'start': next_num_start, 'end': char_idx - 1, 'value': int(line[next_num_start : next_num_end])})
                if not char == '.':
                    symbol_locations.append({ 'col': char_idx, 'row': line_idx, 'symbol': char})
                next_num_start = -1
    
    gear_ratio_sum = sum([gear_ratio(symbol=symbol, numbers=numbers) for symbol in symbol_locations])
    print(gear_ratio_sum)