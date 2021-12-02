

from get_input import get_input

url = 'https://adventofcode.com/2021/day/1/input'
lines = get_input(url).split('\n')
# sample problem
# lines = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

def print_logs(log_str):
	if False:
		print(log_str)

def part_one():
	print('===========PART 1===========')
	last_seen = int(lines[0])
	increased = 0
	for curr_line in lines:
		try:
			# am i pythonic yet
			curr_line = int(curr_line)
		except:
			continue
		
		if curr_line > last_seen:
			print_logs(f'{curr_line} (increased)')
			increased+=1
		elif curr_line < last_seen:
			print_logs(f'current: {curr_line}, last:{last_seen} (decreased)')
		else:
			print_logs(f'{curr_line} (equal)')
		last_seen = curr_line

	print(f'increased: {increased}')


def part_two():
	print('===========PART 2===========')

	increased = 0
	last_seen_sum_of_three = int(lines[0]) + int(lines[1]) + int(lines[2])
	for i in range(0,len(lines)-2):
		try:
			sum_next_three = int(lines[i]) + int(lines[i+1]) + int(lines[i+2])
		except:
			continue
		if sum_next_three > last_seen_sum_of_three:
			increased+=1
			print_logs(f'{sum_next_three} (increased)')
		elif sum_next_three < last_seen_sum_of_three:
			print_logs(f'{sum_next_three} (decreased)')

		else:
			print_logs(f'{sum_next_three} (equal)')
		
		last_seen_sum_of_three = sum_next_three
	print(f'increased: {increased}')


part_one()
part_two()
