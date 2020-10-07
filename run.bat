SET PORT=%1
IF "%PORT%"=="" (
    SET PORT=2000
)

python ton_soundboard/scripts/generate_css_and_js_code_for_audio_buttons.py

bokeh serve --show ton_soundboard --port=%PORT%
