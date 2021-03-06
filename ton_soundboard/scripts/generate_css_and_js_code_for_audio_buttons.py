import sys
from pathlib import Path

_SOURCES_ROOT = Path(__file__).absolute().parent.parent
sys.path.append(str(_SOURCES_ROOT))

from bokeh_layouts.button_props import generate_css_styles_file
from bokeh_layouts.button_props import generate_js_file_for_audio_preloading
from config import SOURCES_ROOT, BUTTON_FILES_MASTER_DIR


def main():
    button_files_dir = BUTTON_FILES_MASTER_DIR
    css_styles_path = SOURCES_ROOT / "templates" / "audio_button_styles.css"
    audio_preloading_javascript_path = SOURCES_ROOT / "templates" / "audio_preloading.js"

    generate_css_styles_file(button_files_dir, css_styles_path)
    generate_js_file_for_audio_preloading(button_files_dir, audio_preloading_javascript_path)


if __name__ == '__main__':
    main()
