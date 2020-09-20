SET PORT=%1
IF "%PORT%"=="" (
    SET PORT=2000
)

cd ton_soundboard
python create_css_styles.py

cd ..
bokeh serve --show ton_soundboard --port=%PORT%

