from collections import defaultdict
from typing import Any


def count_elements(elements: list[Any]) -> dict[Any, int]:
	counter = defaultdict(int)
	for element in elements:
		counter[element] += 1
	return dict(counter)


if __name__ == '__main__':
	assert count_elements([1, 2, 1]) == {1: 2, 2: 1}
	assert count_elements([]) == {}
	assert count_elements([1, 2, 3]) == {1: 1, 2: 1, 3: 1}
