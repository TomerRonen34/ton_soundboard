from bokeh.plotting import curdoc

from config import APP_NAME
from config import AUDIO_FILES_DIR
from config import NUM_BUTTONS_PER_ROW
from bokeh_utils import build_all_audio_buttons
from bokeh_utils import build_layout


def main():
    audio_buttons = build_all_audio_buttons(AUDIO_FILES_DIR)
    layout = build_layout(audio_buttons, NUM_BUTTONS_PER_ROW, APP_NAME)
    curdoc().add_root(layout)
    curdoc().title = APP_NAME


main()