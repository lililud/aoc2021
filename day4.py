
from functools import reduce
from helper import get_input, p
import re


url = 'https://adventofcode.com/2021/day/4/input'
target_string = get_input(url)
# result = re.search(r"([\d,.*]+)\n+((([\d{|' ']+\n){5})\n+)+", target_string)
result = re.search(r"([\d,.*]+)\n+((([\d{|' ']+\n){5})\n+)+", target_string)
print(f'result: {result}')
print(f'result group: {result.group(1)}')

print(f'result group2: {result.group(2)}')
print(f'result group3 {result.group(3)}')

print(target_string.split('\n'))
nums = result.group(1)
def part_one():
	p(1)


def part_two():
	p(2)
	
part_one()
print()
part_two()


