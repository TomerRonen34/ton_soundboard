SET PORT=%1
IF "%PORT%"=="" (
    SET PORT=2000
)

bokeh serve --show . --port=%PORT%

