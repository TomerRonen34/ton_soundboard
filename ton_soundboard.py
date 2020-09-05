from bokeh.plotting import curdoc
from bokeh.layouts import row
from bokeh.models.widgets import Button
from bokeh.events import ButtonClick
from bokeh.models.callbacks import CustomJS
import logging

from utils import encode_file_as_base64

bokehlog = logging.getLogger("deepsong")
bokehlog.setLevel(logging.INFO)

audio_file_path = "./audio_sample.mp3"
audio_base64 = encode_file_as_base64(audio_file_path)
code = f"""
var snd = new Audio("data:audio/mp3;base64,{audio_base64}");
snd.play();
"""
callback = CustomJS(code=code)

play_audio = Button(label='play audio')
play_audio.js_on_event(ButtonClick, callback)

curdoc().add_root(row(play_audio))
