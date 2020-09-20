from typing import List
from typing import Sequence


def split_sequence(lst: Sequence, chunk_size: int) -> List[List]:
    result = []
    for i in range(0, len(lst), chunk_size):
        result.append(lst[i:i + chunk_size])
    return result
