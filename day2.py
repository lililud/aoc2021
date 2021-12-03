

from helper import get_input, p

url = 'https://adventofcode.com/2021/day/2/input'
lines = get_input(url).split('\n')

# sample problem:
# lines = ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"]

def print_answer(horizontal, depth):
	print(f'horizontal ({horizontal}) x depth ({depth}): [{horizontal*depth}]\n')

def match_line(horizontal, depth, aim, value, direction):
	match(direction):
		case "forward":
			horizontal += value
			depth += (aim*value)
			
		case "up":
			aim -= value
			
		case "down":
			aim+=value
			
	return horizontal, depth, aim

def parse_ans():
	horizontal, aim, depth = 0, 0, 0

	for line in lines:
		direction = line.split(' ')[0]
		try: 
			# how pythonic am i
			value = int(line.split(' ')[1])
		except:
			break
		horizontal, depth, aim = match_line(
			horizontal=horizontal, 
			depth=depth, 
			aim=aim, 
			value=value, 
			direction=direction
		)
	return horizontal, depth, aim

def part_one():	
	p(1)	
	horizontal, aim, depth = parse_ans()
	print_answer(horizontal=horizontal, depth=depth) 


def part_two():	
	p(2)
	horizontal, aim, depth = parse_ans()
	print_answer(horizontal=horizontal, depth=aim)

part_one()
part_two()


