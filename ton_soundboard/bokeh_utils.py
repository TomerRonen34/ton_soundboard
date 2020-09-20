from typing import Sequence
from typing import Union
from typing import List
from pathlib import Path

from bokeh.models.widgets import Button
from bokeh.events import ButtonClick
from bokeh.models.callbacks import CustomJS
from bokeh.models import Div
from bokeh.layouts import column
from bokeh.layouts import Column
from bokeh.layouts import gridplot

from button_props import gather_button_props
from config import button_size_pixels


def build_layout(buttons: Sequence[Button],
                 num_buttons_per_row: int,
                 title: str) -> Column:
    layout_options = dict(align="center")
    title = Div(text=f"<h1>{title}</h1>", **layout_options)
    layout = column(title,
                    gridplot(buttons, ncols=num_buttons_per_row),
                    **layout_options)
    return layout


def build_all_audio_buttons(files_dir: Union[str, Path]) -> List[Button]:
    all_button_props = gather_button_props(files_dir)
    buttons = [
        build_audio_button(button_props.audio_path,
                           button_props.css_class_name)
        for button_props in all_button_props
    ]
    return buttons


def build_audio_button(audio_path: Path, css_class: str) -> Button:
    js_code = f"""
    var snd = new Audio("{audio_path.as_posix()}");
    snd.play();
    """
    callback = CustomJS(code=js_code)
    audio_button = Button(label='', css_classes=[css_class],
                          width=button_size_pixels, height=button_size_pixels)
    audio_button.js_on_event(ButtonClick, callback)
    return audio_button
