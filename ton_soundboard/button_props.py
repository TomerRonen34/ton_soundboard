from pathlib import Path
from typing import Union
from typing import List


class ButtonProps:
    def __init__(self,
                 audio_path: Union[str, Path],
                 image_extension: str = ".png",
                 parent_dir_for_css: str = "ton_soundboard"):
        self.audio_path = Path(audio_path)
        self.image_path = self.audio_path.with_suffix(image_extension)
        self.css_class_name = self.audio_path.stem + "_button"
        self.parent_dir_for_css = parent_dir_for_css
        self._assert_files_exist()

    def _assert_files_exist(self):
        assert self.audio_path.exists(), f"Audio path doesn't exists: {self.audio_path}"
        assert self.image_path.exists(), f"Image path doesn't exists: {self.audio_path}"

    def generate_css_class_code(self):
        image_path_for_css = Path(self.parent_dir_for_css) / self.image_path
        css_code = f"""
.{self.css_class_name} button.bk.bk-btn.bk-btn-default {{
    background-image: url('{image_path_for_css.as_posix()}');
    background-repeat: no-repeat;
    background-size: contain;
    background-position: center;
    background-color: gray;
    border-radius: 15%;
}}
"""
        return css_code


def gather_button_props(button_files_dir: Union[str, Path]) -> List[ButtonProps]:
    audio_paths = sorted(Path(button_files_dir).rglob('*.mp3'))
    all_button_props = [ButtonProps(audio_path) for audio_path in audio_paths]
    return all_button_props


def create_css_styles_file(button_files_dir: Union[str, Path],
                           output_path: Union[str, Path],
                           default_css_styles_path: Union[str, Path] = None):
    all_button_props = gather_button_props(button_files_dir)
    all_css_classes = [b.generate_css_class_code() for b in all_button_props]
    css_styles_code = ''.join(all_css_classes)

    if default_css_styles_path is not None:
        with open(default_css_styles_path, 'r') as f:
            default_css_styles_code = f.read()
        css_styles_code = default_css_styles_code + css_styles_code

    with open(output_path, 'w') as f:
        f.write(css_styles_code)
