from pathlib import Path
from button_props import generate_css_styles_file
from button_props import generate_js_file_for_audio_preloading


def main():
    curr_dir = Path(__file__).parent
    button_files_dir = curr_dir / "static" / "button_files"
    css_styles_path = curr_dir / "templates" / "audio_button_styles.css"
    audio_preloading_javascript_path = curr_dir / "templates" / "audio_preloading.js"

    generate_css_styles_file(button_files_dir, css_styles_path)
    generate_js_file_for_audio_preloading(button_files_dir, audio_preloading_javascript_path)


if __name__ == '__main__':
    main()
