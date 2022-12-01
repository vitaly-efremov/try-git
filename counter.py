from collections import defaultdict

def counter(elements: list[str]) -> dict[str, int]:
	counter = defaultdict(int)
	for element in elements:
		counter[element] += 1
	return dict(counter)


if __name__ == '__main__':
	assert counter([1, 2, 1]) == {1: 2, 2: 1}
	assert counter([]) == {}
	assert counter([1, 2, 3]) == {1: 1, 2: 1, 3: 1}
	
