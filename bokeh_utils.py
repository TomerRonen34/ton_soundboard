from typing import Iterable
from typing import Union
from typing import List
from pathlib import Path

from bokeh.models.widgets import Button
from bokeh.events import ButtonClick
from bokeh.models.callbacks import CustomJS
from bokeh.layouts import row
from bokeh.layouts import Row

from utils import gather_mp3_files


def build_layout(buttons: Iterable[Button]) -> Row:
    return row(*buttons)


def build_all_audio_buttons(files_dir: Union[str, Path]) -> List[Button]:
    buttons = []
    mp3_files_name2encoded = gather_mp3_files(files_dir)
    for file_name, audio_base64 in mp3_files_name2encoded.items():
        button = build_audio_button(file_name, audio_base64)
        buttons.append(button)
    return buttons


def build_audio_button(label: str, audio_base64: str) -> Button:
    js_code = f"""
    var snd = new Audio("data:audio/mp3;base64,{audio_base64}");
    snd.play();
    """
    callback = CustomJS(code=js_code)
    audio_button = Button(label=label)
    audio_button.js_on_event(ButtonClick, callback)
    return audio_button
