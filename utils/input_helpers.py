import os

from config import ROOT_DIR

def get_input_for(day: int, sample: bool) -> list[str]:
    return [line for line in get_input_as_string_for(day, sample).splitlines()]

def get_input_as_string_for(day: int, sample: bool) -> str:
    input_file = _file_name(day, sample)

    with open(input_file) as file:
        content = file.read()
    
    content = content.rstrip("\n")
    return content

def _file_name(day: int, sample: bool) -> str:
    name = 'sample.txt'if sample  else 'input.txt'
    path = os.path.join(ROOT_DIR, f"day{day:02}", name)
    return path