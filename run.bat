SET PORT=%1
IF "%PORT%"=="" (
    SET PORT=2000
)

cd ton_soundboard
python scripts/generate_css_and_js_code_for_audio_buttons.py

cd ..
bokeh serve --show ton_soundboard --port=%PORT%

