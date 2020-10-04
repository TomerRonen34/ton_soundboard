from typing import Union
from typing import List
from pathlib import Path

from bokeh.models.widgets import Button
from bokeh.events import ButtonClick
from bokeh.models.callbacks import CustomJS


class ButtonProps:
    def __init__(self,
                 audio_path: Union[str, Path],
                 image_extension: str = ".jpg"):
        self.audio_path = Path(audio_path)
        self.image_path = self.audio_path.with_suffix(image_extension)
        self._assert_files_exist()

        self.button_id = self.audio_path.stem + "_button"
        self.parent_dir_for_css_and_js = Path(__file__).absolute().parent.stem

    def _assert_files_exist(self):
        assert self.audio_path.exists(), f"Audio path doesn't exists: {self.audio_path}"
        assert self.image_path.exists(), f"Image path doesn't exists: {self.image_path}"

    def build_button(self, button_size_pixels: int) -> Button:
        js_code_for_adio_playing = self._generate_js_code_for_audio_playing()
        callback = CustomJS(code=js_code_for_adio_playing)
        audio_button = Button(label='', css_classes=[self.button_id],
                              width=button_size_pixels, height=button_size_pixels)
        audio_button.js_on_event(ButtonClick, callback)
        return audio_button

    def _generate_js_code_for_audio_playing(self):
        js_code = f"""
        window.{self.button_id}.play();
        """
        return js_code

    def generate_css_class_code(self):
        image_path_for_css = Path(self.parent_dir_for_css_and_js) / self.image_path
        css_code = f"""
.{self.button_id} button.bk.bk-btn.bk-btn-default {{
    background-image: url('{image_path_for_css.as_posix()}');
    background-repeat: no-repeat;
    background-size: contain;
    background-position: center;
    background-color: white;
    border-radius: 15%;
}}
"""
        return css_code

    def generate_js_code_for_audio_preloading(self) -> str:
        audio_path_for_js = Path(self.parent_dir_for_css_and_js) / self.audio_path
        js_code = f"""
window.{self.button_id} = new Audio('{audio_path_for_js.as_posix()}');
window.{self.button_id}.preload = "auto";
window.{self.button_id}.load();
"""
        return js_code


def gather_button_props(button_files_dir: Union[str, Path]) -> List[ButtonProps]:
    audio_paths = sorted(Path(button_files_dir).rglob('*.mp3'))
    all_button_props = [ButtonProps(audio_path) for audio_path in audio_paths]
    return all_button_props


def generate_css_styles_file(button_files_dir: Union[str, Path],
                             output_path: Union[str, Path]) -> None:
    all_button_props = gather_button_props(button_files_dir)
    all_css_classes = [b.generate_css_class_code() for b in all_button_props]
    css_styles_code = ''.join(all_css_classes)

    with open(output_path, 'w') as f:
        f.write(css_styles_code)


def generate_js_file_for_audio_preloading(button_files_dir: Union[str, Path],
                                          output_path: Union[str, Path]) -> None:
    all_button_props = gather_button_props(button_files_dir)
    all_js_preloading_code = [b.generate_js_code_for_audio_preloading() for b in all_button_props]
    js_preloading_code = ''.join(all_js_preloading_code)

    with open(output_path, 'w') as f:
        f.write(js_preloading_code)
