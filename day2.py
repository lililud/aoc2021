

import requests
import json
from requests.structures import CaseInsensitiveDict


headers = CaseInsensitiveDict()
headers["Cookie"] = "_ga=GA1.2.1779206326.1633461475; _gid=GA1.2.1370206870.1638387628; session=53616c7465645f5fcdfea6be14360296077be5b47d195db9dafed49e68237b341389b34bfaa38f4831cf13b3daabb71c"

url = 'https://adventofcode.com/2021/day/2/input'
request = requests.get(url, headers=headers)
lines = request.text.split('\n')



horizontal_val = 0
depth = 0
# sample problem:
# lines = ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"]


aim = 0
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



