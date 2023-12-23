from dataclasses import dataclass, field

@dataclass
class Card:
    number: int
    winning_nums: list[int] = field(default_factory=list)
    my_nums: list[int] = field(default_factory=list)

    def match_count(self) -> int:
        winning_set = set(self.winning_nums)
        my_set = set(self.my_nums)
        match_count = len(winning_set.intersection(my_set))
        return match_count
    
    def raw_score(self) -> int:
        count = self.match_count()
        if count > 0:
            return (2 ** (count - 1))
        else:
            return 0

def count_score(cards: list[Card]) -> int:
    total = 0

    for card in cards:
        total += card.raw_score()
    return total

def parse_cards(lines: list[str]) -> list[Card]:
    cards = []
    for line in lines:
        card_num_str_and_rest = line.split(":")
        card_num_str = card_num_str_and_rest[0]
        print(card_num_str)
        card_num = card_num_str.split(" ")[1]


        all_nums_list = card_num_str_and_rest[1].split(" | ")

        winning_nums = [int(num) for num in all_nums_list[0].split(" ") if num]
        my_nums = [int(num) for num in all_nums_list[1].split(" ") if num]
        cards.append(Card(number=card_num, winning_nums=winning_nums, my_nums=my_nums))
    return cards

memo = {}

def count_card_in_cards(idx: int, cards: list[Card]) -> int:
    card = cards[idx]
    
    if card.number in memo.keys():
        return memo[card.number]
    elif card.match_count() == 0:
        return 1
    else:
        end_index = (idx + card.match_count())
        total = 1
        current_idx = idx + 1
        while current_idx <= end_index:
            total += count_card_in_cards(current_idx, cards)
            current_idx +=1
        return total

def solve(lines: list[str]):
    cards = parse_cards(lines)
    total = 0
    current_idx = len(cards) - 1
    while current_idx >= 0:
        total += count_card_in_cards(current_idx, cards)
        current_idx -= 1

    print(total)