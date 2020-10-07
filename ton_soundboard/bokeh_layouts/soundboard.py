from pathlib import Path
from typing import Iterable, Union

from bokeh.layouts import column
from bokeh.models import Column, Div

from bokeh_layouts.button_section import ButtonSection
from config import SOUNDBOARD_TITLE_CSS_CLASS, SECTION_MARGIN_TOP_RIGHT_BOTTOM_LEFT, CREDITS, CREDITS_CSS_CLASS


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
        for subdir in sorted(Path(master_dir).iterdir()):
            if subdir.is_dir():
                section = ButtonSection.build_section_from_dir(
                    subdir, num_buttons_per_row, button_size_pixels)
                button_sections.append(section)
        layout = cls(button_sections, title)
        return layout

    def _build_layout(self) -> Column:
        align_options = dict(align="center")
        title_div = Div(text=self._title, css_classes=[SOUNDBOARD_TITLE_CSS_CLASS],
                        margin=SECTION_MARGIN_TOP_RIGHT_BOTTOM_LEFT, **align_options)
        section_layouts = [section.layout for section in self._button_sections]
        credits_div = Div(text=CREDITS, css_classes=[CREDITS_CSS_CLASS], **align_options)
        layout = column(title_div,
                        *section_layouts,
                        credits_div,
                        **align_options)
        return layout
