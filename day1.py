

from helper import get_input, p

url = 'https://adventofcode.com/2021/day/1/input'
lines = get_input(url).split('\n')

# sample problem
# lines = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

def part_one():
	p(1)
	last_seen = int(lines[0])
	increased = 0
	for curr_line in lines:
		try:
			# am i pythonic yet
			curr_line = int(curr_line)
		except:
			continue
		
		if curr_line > last_seen:
			increased+=1
		last_seen = curr_line

	print(f'increased: {increased}\n')


def part_two():
	p(2)
	increased = 0
	last_seen_sum_of_three = int(lines[0]) + int(lines[1]) + int(lines[2])
	for i in range(0, len(lines)-2):
		try:
			sum_next_three = int(lines[i]) + int(lines[i+1]) + int(lines[i+2])
		except:
			continue
		if sum_next_three > last_seen_sum_of_three:
			increased+=1
		
		last_seen_sum_of_three = sum_next_three
	print(f'increased: {increased}')


part_one()
part_two()
