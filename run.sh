python ton_soundboard/scripts/generate_css_and_js_code_for_audio_buttons.py

bokeh serve \
    --allow-websocket-origin=ton-soundboard.herokuapp.com --address=0.0.0.0 --use-xheaders \
    --port=$PORT \
    ton_soundboard