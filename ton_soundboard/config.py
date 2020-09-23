from pathlib import Path

curr_dir = Path(Path(__file__).absolute().parent.stem)
BUTTON_FILES_MASTER_DIR = curr_dir / "static" / "button_files"
NUM_BUTTONS_PER_ROW = 3
BUTTON_SIZE_PIXELS = 300
APP_NAME = "Tales Of Nowhere Soundboard"
SECTION_HEADER_CSS_CLASS = "section_header_button"
SOUNDBOARD_TITLE_CSS_CLASS = "soundboard_title"
SECTION_MARGIN_TOP_RIGHT_BOTTOM_LEFT = (0, 0, int(BUTTON_SIZE_PIXELS / 4), 0)
