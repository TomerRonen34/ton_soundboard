import sys
from pathlib import Path

_SOURCES_ROOT = Path(__file__).absolute().parent.parent
sys.path.append(str(_SOURCES_ROOT))

from shutil import copyfile

from audio_processing import adjust_mp3_amplitude
from bokeh_layouts.button_props import gather_button_props, ButtonProps
from config import SOURCES_ROOT


def main():
    buttons_dir_original_volume = SOURCES_ROOT / "static" / "button_files_original_volume"
    buttons_dir_adjusted_volume = SOURCES_ROOT / "static" / "button_files_adjusted_volume"

    all_button_props = gather_button_props(buttons_dir_original_volume)
    for button_props in all_button_props:
        _adjust_button_volume(button_props, buttons_dir_original_volume, buttons_dir_adjusted_volume)


def _adjust_button_volume(button_props: ButtonProps,
                          original_dir: Path,
                          new_dir: Path):
    new_audio_path = new_dir / button_props.audio_path.relative_to(original_dir)
    new_image_path = new_dir / button_props.image_path.relative_to(original_dir)

    button_subdir = new_audio_path.parent
    button_subdir.mkdir(parents=True, exist_ok=True)

    copyfile(button_props.image_path, new_image_path)
    adjust_mp3_amplitude(button_props.audio_path, new_audio_path)


if __name__ == '__main__':
    main()
