from typing import Sequence
from typing import Union
from typing import List
from pathlib import Path

from bokeh.models.widgets import Button
from bokeh.events import ButtonClick
from bokeh.models.callbacks import CustomJS
from bokeh.models import Div
from bokeh.layouts import row
from bokeh.layouts import column
from bokeh.layouts import Column

from utils import gather_mp3_files
from utils import split_sequence


def build_layout(buttons: Sequence[Button],
                 num_per_row: int,
                 title: str) -> Column:
    # layout_options = dict(align="center", sizing_mode="scale_width")
    layout_options = dict(align="center")
    buttons_per_row = split_sequence(buttons, num_per_row)
    button_rows = [row(curr_buttons, **layout_options) for curr_buttons in buttons_per_row]
    title = Div(text=f"<h1>{title}</h1>", **layout_options)
    layout = column(title,
                    *button_rows,
                    **layout_options)
    return layout


def build_all_audio_buttons(files_dir: Union[str, Path]) -> List[Button]:
    buttons = []
    mp3_files_name2encoded = gather_mp3_files(files_dir)
    for file_name, audio_base64 in mp3_files_name2encoded.items():
        button = build_audio_button(file_name, audio_base64)
        col = column([Div(text="<h1>looooooooooooooooooool</h1>", width=300),
                      button])
        buttons.append(col)
    return buttons


def build_audio_button(label: str, audio_base64: str) -> Button:
    js_code = f"""
    var snd = new Audio("data:audio/mp3;base64,{audio_base64}");
    snd.play();
    """
    layout_options = dict(align="center", sizing_mode="scale_width",
                          aspect_ratio=1)
    callback = CustomJS(code=js_code)
    # audio_button = Button(label=label, css_classes=["custom_button_bokeh"],
    #                       **layout_options)
    # label = "abcdefghij\nklmnopqrst\nuvwxyz"
    label = "ab<br>cd11111<br>1111111111111111111111111111111111111111111111111111111111111111111111111"
    audio_button = Button(label=label, css_classes=["custom_button_bokeh"],
                          width=300, height=300)
    audio_button.js_on_event(ButtonClick, callback)
    return audio_button
