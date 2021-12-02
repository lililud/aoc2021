import requests
import json
from requests.structures import CaseInsensitiveDict
from dotenv import load_dotenv
import os
load_dotenv()


def get_input(url):
	headers = CaseInsensitiveDict()
	headers["Cookie"] = os.environ.get('ADVENT_OF_CODE_COOKIE')

	request = requests.get(url, headers=headers)
	return request.text
