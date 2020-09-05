from bokeh.plotting import curdoc

from config import AUDIO_FILES_DIR
from bokeh_utils import build_all_audio_buttons
from bokeh_utils import build_layout


def main():
    audio_buttons = build_all_audio_buttons(AUDIO_FILES_DIR)
    layout = build_layout(audio_buttons)
    curdoc().add_root(layout)
