from typing import Iterable
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
from config import SOUNDBOARD_TITLE_CSS_CLASS
from config import SECTION_HEADER_CSS_CLASS
from config import SECTION_MARGIN_TOP_RIGHT_BOTTOM_LEFT


class ButtonSection:
    def __init__(self,
                 buttons: Sequence[Button],
                 num_buttons_per_row: int,
                 title: str):
        self._buttons = buttons
        self._num_buttons_per_row = num_buttons_per_row
        self._title = title
        self._button_grid = gridplot(buttons, ncols=num_buttons_per_row)
        self._header_button = self._build_header_button()
        self.layout = column(margin=SECTION_MARGIN_TOP_RIGHT_BOTTOM_LEFT)
        self._expand_button_grid()

    @classmethod
    def build_section_from_dir(cls,
                               files_dir: Union[str, Path],
                               num_buttons_per_row: int,
                               button_size_pixels: int):
        buttons = _build_audio_buttons_from_dir(files_dir, button_size_pixels)
        section_title = Path(files_dir).stem
        section = cls(buttons, num_buttons_per_row, section_title)
        return section

    def _build_header_button(self):
        single_button_width = self._buttons[0].width
        header_button_width = single_button_width * self._num_buttons_per_row
        header_button = Button(label=self._title, width=header_button_width,
                               css_classes=[SECTION_HEADER_CSS_CLASS],
                               align="center")
        header_button.on_click(self._toggle_button_grid)
        return header_button

    def _toggle_button_grid(self):
        if self._is_collapsed:
            self._expand_button_grid()
        else:
            self._collapse_button_grid()

    def _expand_button_grid(self):
        self.layout.children = [self._header_button, self._button_grid]
        self._is_collapsed = False

    def _collapse_button_grid(self):
        self.layout.children = [self._header_button]
        self._is_collapsed = True


class Soundboard:
    def __init__(self,
                 button_sections: Iterable[ButtonSection],
                 title: str):
        self._button_sections = button_sections
        self._title = title
        self.layout = self._build_layout()

    @classmethod
    def build_soundboard_from_master_dir(cls,
                                         title: str,
                                         master_dir: Union[str, Path],
                                         num_buttons_per_row: int,
                                         button_size_pixels: int):
        button_sections = []
        for subdir in Path(master_dir).iterdir():
            if subdir.is_dir():
                section = ButtonSection.build_section_from_dir(
                    subdir, num_buttons_per_row, button_size_pixels)
                button_sections.append(section)
        layout = cls(button_sections, title)
        return layout

    def _build_layout(self) -> Column:
        align_options = dict(align="center")
        title_div = Div(text=self._title, css_classes=[SOUNDBOARD_TITLE_CSS_CLASS], **align_options)
        section_layouts = [section.layout for section in self._button_sections]
        layout = column(title_div,
                        *section_layouts,
                        **align_options)
        return layout


def _build_audio_buttons_from_dir(files_dir: Union[str, Path],
                                  button_size_pixels: int) -> List[Button]:
    all_button_props = gather_button_props(files_dir)
    buttons = [
        _build_audio_button(button_props.audio_path,
                            button_props.css_class_name,
                            button_size_pixels)
        for button_props in all_button_props
    ]
    return buttons


def _build_audio_button(audio_path: Path, css_class: str, button_size_pixels: int) -> Button:
    js_code = f"""
    var snd = new Audio("{audio_path.as_posix()}");
    snd.play();
    """
    callback = CustomJS(code=js_code)
    audio_button = Button(label='', css_classes=[css_class],
                          width=button_size_pixels, height=button_size_pixels)
    audio_button.js_on_event(ButtonClick, callback)
    return audio_button
