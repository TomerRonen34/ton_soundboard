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


def gather_mp3_files(files_dir: Union[str, Path]) -> Dict[str, str]:
    mp3_files_name2encoded = {}
    for audio_file_path in Path(files_dir).iterdir():
        file_name = audio_file_path.stem
        audio_base64 = encode_file_as_base64(audio_file_path)
        mp3_files_name2encoded[file_name] = audio_base64
    return mp3_files_name2encoded


def split_sequence(lst: Sequence, chunk_size: int) -> List[List]:
    result = []
    for i in range(0, len(lst), chunk_size):
        result.append(lst[i:i + chunk_size])
    return result
