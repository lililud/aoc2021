

from get_input import get_input

url = 'https://adventofcode.com/2021/day/2/input'
lines = get_input(url).split('\n')

def part_one():	
	print("==========PART ONE=========")
	horizontal_val = 0
	depth = 0

	# sample problem:
	# lines = ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"]

	for line in lines:
		direction = line.split(' ')[0]
		try: 
			value = int(line.split(' ')[1])
		except:
			break
		match(direction):
			case "forward":
				horizontal_val += value
				continue
			case "up":
				depth -= value
				continue
			case "down":
				depth += value
				continue

	print(f'horizontal: {horizontal_val}')
	print(f'depth: {depth}')
	print(f'horizontal X depth: {horizontal_val*depth}')

def part_two():	
	print("==========PART TWO=========")
	horizontal_val = 0
	depth = 0
	aim = 0

	# sample problem:
	# lines = ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"]



	for line in lines:
		direction = line.split(' ')[0]
		try: 
			value = int(line.split(' ')[1])
		except:
			break
		match(direction):
			case "forward":
				horizontal_val += value
				depth += (aim*value)
				continue
			case "up":
				# depth -= value
				aim -= value
				continue
			case "down":
				# depth += value
				aim+=value
				continue

	print(f'horizontal: {horizontal_val}')
	print(f'depth: {depth}')
	print(f'horizontal X depth: {horizontal_val*depth}')

part_one()
part_two()


