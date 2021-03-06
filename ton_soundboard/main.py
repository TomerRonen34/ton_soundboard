from bokeh.plotting import curdoc

from config import APP_NAME, SUBTITLE
from config import BUTTON_FILES_MASTER_DIR
from config import NUM_BUTTONS_PER_ROW
from config import BUTTON_SIZE_PIXELS
from bokeh_layouts.soundboard import Soundboard


def main():
    soundboard = Soundboard.build_soundboard_from_master_dir(
        title=APP_NAME, subtitle=SUBTITLE, master_dir=BUTTON_FILES_MASTER_DIR,
        num_buttons_per_row=NUM_BUTTONS_PER_ROW, button_size_pixels=BUTTON_SIZE_PIXELS)
    curdoc().add_root(soundboard.layout)
    curdoc().title = APP_NAME


main()
