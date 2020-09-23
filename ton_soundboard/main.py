from bokeh.plotting import curdoc

from config import APP_NAME
from config import BUTTON_FILES_MASTER_DIR
from config import NUM_BUTTONS_PER_ROW
from config import BUTTON_SIZE_PIXELS
from bokeh_utils import Soundboard


def main():
    soundboard = Soundboard.build_soundboard_from_master_dir(
        title=APP_NAME, master_dir=BUTTON_FILES_MASTER_DIR,
        num_buttons_per_row=NUM_BUTTONS_PER_ROW, button_size_pixels=BUTTON_SIZE_PIXELS)
    curdoc().add_root(soundboard.layout)
    curdoc().title = APP_NAME


main()
