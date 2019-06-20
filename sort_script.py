
import json


def install_sort(package):
	return package['analytics']['30d']

with open('package_info.json', 'r') as f:
	data = json.load(f)

# this below list comprehension can be adjusted according to user needs.
data = [item for item in data if 'video' in item['desc']]

data.sort(key=install_sort, reverse=True)
data_str = json.dumps(data, indent=2)

print(data_str)

 