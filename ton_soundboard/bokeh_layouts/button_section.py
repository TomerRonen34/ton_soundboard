from typing import Sequence
from typing import Union
from typing import List
from pathlib import Path
import re

from bokeh.models.widgets import Button
from bokeh.layouts import column
from bokeh.layouts import gridplot

from bokeh_layouts.button_props import gather_button_props
from config import SECTION_HEADER_CSS_CLASS
from config import SECTION_MARGIN_TOP_RIGHT_BOTTOM_LEFT
from config import SECTION_TITLE_PREFIX_REGEX


class ButtonSection:
    def __init__(self,
                 buttons: Sequence[Button],
                 num_buttons_per_row: int,
                 title: str):
        self._buttons = buttons
        self._num_buttons_per_row = num_buttons_per_row
        self._title = title
        self._button_grid = gridplot(buttons, ncols=num_buttons_per_row)
        self._header_button_expanded = self._build_header_button(is_collapsed=False)
        self._header_button_collapsed = self._build_header_button(is_collapsed=True)
        self.layout = column(margin=SECTION_MARGIN_TOP_RIGHT_BOTTOM_LEFT)
        self._expand_button_grid()

    @classmethod
    def build_section_from_dir(cls,
                               files_dir: Union[str, Path],
                               num_buttons_per_row: int,
                               button_size_pixels: int):
        buttons = cls._build_audio_buttons_from_dir(files_dir, button_size_pixels)
        section_title_with_prefix = Path(files_dir).stem
        section_title = re.sub(SECTION_TITLE_PREFIX_REGEX, '', section_title_with_prefix)
        section = cls(buttons, num_buttons_per_row, section_title)
        return section

    @classmethod
    def _build_audio_buttons_from_dir(cls,
                                      files_dir: Union[str, Path],
                                      button_size_pixels: int) -> List[Button]:
        all_button_props = gather_button_props(files_dir)
        buttons = [
            button_props.build_button(button_size_pixels)
            for button_props in all_button_props
        ]
        return buttons

    def _build_header_button(self, is_collapsed: bool):
        single_button_width = self._buttons[0].width
        header_button_width = single_button_width * self._num_buttons_per_row
        is_collapsed_arrow = "► " if is_collapsed else "▼ "
        header_button = Button(label=is_collapsed_arrow + self._title,
                               width=header_button_width,
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
        self.layout.children = [self._header_button_expanded, self._button_grid]
        self._is_collapsed = False

    def _collapse_button_grid(self):
        self.layout.children = [self._header_button_collapsed]
        self._is_collapsed = True
