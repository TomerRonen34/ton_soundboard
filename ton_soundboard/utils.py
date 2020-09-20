from typing import Union
from typing import Dict
from typing import List
from typing import Sequence
from pathlib import Path
from base64 import b64encode


def encode_file_as_base64(path: Union[str, Path]) -> str:
    with open(path, 'rb') as f:
        content = f.read()
    b64_content = b64encode(content).decode()
    return b64_content


def split_sequence(lst: Sequence, chunk_size: int) -> List[List]:
    result = []
    for i in range(0, len(lst), chunk_size):
        result.append(lst[i:i + chunk_size])
    return result
