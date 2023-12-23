from dataclasses import dataclass, field

@dataclass
class Card:
    number: int
    winning_nums: list[int] = field(default_factory=list)
    my_nums: list[int] = field(default_factory=list)


def solve(lines: list[str]):
    cards = []
    total = 0
    for line in lines:
        card_num_str_and_rest = line.split(":")
        card_num_str = card_num_str_and_rest[0]
        card_num = card_num_str.split(" ")[1]


        all_nums_list = card_num_str_and_rest[1].split(" | ")
        # print(all_nums_list)

        winning_nums = [int(num) for num in all_nums_list[0].split(" ") if num]
        my_nums = [int(num) for num in all_nums_list[1].split(" ") if num]
        # my_nums = [int(num) for num in all_nums_list[1]]
        cards.append(Card(number=card_num, winning_nums=winning_nums, my_nums=my_nums))
        # print(cards[-1])
    
    for card in cards:
        winning_set = set(card.winning_nums)
        my_set = set(card.my_nums)
        match_count = len(winning_set.intersection(my_set))
        if match_count > 0:
            total += (2 ** (match_count - 1))
        print(card, match_count)

    print(total)