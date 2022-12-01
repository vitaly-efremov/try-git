from collections import defaultdict


def count(elements: list[int]) -> dict[int, int]:
	counter = defaultdict(int)
	for element in elements:
		counter[element] += 1
	return dict(counter)


if __name__ == '__main__':
	assert count([1, 2, 1]) == {1: 2, 2: 1}
	assert count([]) == {}
	assert count([1, 2, 3]) == {1: 1, 2: 1, 3: 1}
