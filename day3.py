# gamma rate == most common bit of each number

# epsilon rate = least common bit for each position
# power consumption = gamma rate * epsilon rate

from functools import reduce
from helper import get_input, p

def is_not_empty(l):
	return l != ''
url = 'https://adventofcode.com/2021/day/3/input'
lines = get_input(url).split('\n')
lines = list(filter(is_not_empty, lines))
# lines = ['00100', '11110', '10110', '10111', '10101', '01111', '00111', '10000', '11001', '00010', '01010']
length = len(lines[0])

def is_same_length(l):
	return len(l) == length


def is_1(s, i):
	
	return int(s[i]) == 1
def str_to_binary(s):
	num = int(s, 2) # binary string -> decimal equivalent of binary num
	return bin(num) # python binary

def invert_binary_str(binary):
	# take in an int
	int_binary = int(binary, 2)
	
	str_mask = reduce(lambda x, y: x+y, ['1' for i in range(0, length)]) # stripe the 0b
	
	int_mask = int(str_mask, 2)
	inverted_binary = int_binary^int_mask
	
	return bin(inverted_binary)

def binary_to_decimal(binary_str):
	decimal = 0
	for n in range(0, len(binary_str)):
		# going from right to left
		idx = len(binary_str) - n - 1
		decimal += (2**n*int(binary_str[idx]))
	return decimal



def part_one():
	p(1)
	must_be_greater_than = len(lines) / 2
	gamma_rate = []
	epsilon_rate = []
	epsilon_rate_2 = []

	for idx in range(0, length):
		nw_list = list(filter(lambda line: is_1(line, idx), lines))
		gamma_rate +='1' if len(nw_list) > must_be_greater_than else '0'

	gamma_rate = reduce(lambda x, y: x+y, gamma_rate)
	epsilon_rate = invert_binary_str(str_to_binary(gamma_rate))

	print(f'epsilon_rate: {epsilon_rate}')
	print(f'power consumption = {binary_to_decimal(gamma_rate) * int(epsilon_rate, 2)}')


def part_two():
	p(2)
	o2, c02 = lines, lines
	for idx in range(0, length):
		o2_must_be_greater_than = len(o2) / 2
		c02_must_be_less_than = len(c02) / 2
		
		list_w_1s_in_curr_idx = list(filter(lambda line: is_1(line, idx), o2))
		list_w_0s_in_curr_idx = list(filter(lambda x: x not in list_w_1s_in_curr_idx, o2))
		list_w_1s_in_curr_idx_c02 = list(filter(lambda line: is_1(line, idx), c02))
		list_w_0s_in_curr_idx_c02 = list(filter(lambda x: x not in list_w_1s_in_curr_idx_c02, c02))
		if len(list_w_1s_in_curr_idx) >= o2_must_be_greater_than:
			o2 = list_w_1s_in_curr_idx
			
		else:
			o2 = list_w_0s_in_curr_idx
		if len(list_w_0s_in_curr_idx_c02) <= c02_must_be_less_than:
			c02 = list_w_0s_in_curr_idx_c02
		else:
			c02 = list_w_1s_in_curr_idx_c02
		if(len(c02) == 1):
			final_cO2 = c02[0]
		if(len(o2) == 1):
			final_o2 = o2[0]
			
	print(f'O2: {final_o2}')
	print(f'c02: {final_cO2}')	
	print(f'life support rating: {int(final_o2, 2) * int(final_cO2, 2)}')
part_one()
print()
part_two()


