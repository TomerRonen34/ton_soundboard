from pathlib import Path
from button_props import create_css_styles_file


def main():
    curr_dir = Path(__file__).parent
    css_styles_path = curr_dir / "templates" / "styles.css"
    button_files_dir = curr_dir / "static" / "button_files"
    create_css_styles_file(button_files_dir, css_styles_path)


if __name__ == '__main__':
    main()
