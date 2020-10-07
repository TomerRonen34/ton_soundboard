from pathlib import Path

SOURCES_ROOT = Path(__file__).absolute().parent
PROJECT_ROOT = SOURCES_ROOT.parent
BUTTON_FILES_MASTER_DIR = SOURCES_ROOT / "static" / "button_files_adjusted_volume"
# BUTTON_FILES_MASTER_DIR = SOURCES_ROOT / "static" / "button_files_original_volume"
LAME_EXE_PATH = PROJECT_ROOT / "lame_audio_converter" / "lame3.100.1-x64" / "lame.exe"

APP_NAME = "Tales Of Nowhere Soundboard"

NUM_BUTTONS_PER_ROW = 3
BUTTON_SIZE_PIXELS = 300
SECTION_MARGIN_TOP_RIGHT_BOTTOM_LEFT = (0, 0, int(BUTTON_SIZE_PIXELS / 4), 0)

SECTION_TITLE_PREFIX_REGEX = r"^x\d+_"

SECTION_HEADER_CSS_CLASS = "section_header_button"
SOUNDBOARD_TITLE_CSS_CLASS = "soundboard_title"
CREDITS_CSS_CLASS = "credits"

CREDITS = """
Made with love by Tomer Ronen using Python's Bokeh Server.
<br>
<a href="https://github.com/TomerRonen34/ton_soundboard" target="_blank">Code and audio files</a>  
<br>
<br>
Special thanks to Rita Volosin and John Good for cutting many of the snippets.
<br>
<br>
<u>Art credits:</u>
<br>
memoangeles (goblin), artofmervin (scifi woman), Beth Davies (horse cowboy), 
Arkham Horror card game (Henry Armitage), official Tales of Nowhere site (character icons), 
The Muppets (swedish chef), Vicki Jauron (cowwoman)
"""
