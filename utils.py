from typing import Union
from pathlib import Path
from base64 import b64encode


def encode_file_as_base64(path: Union[str, Path]) -> str:
    with open(path, 'rb') as f:
        content = f.read()
    b64_content = b64encode(content).decode()
    return b64_content
