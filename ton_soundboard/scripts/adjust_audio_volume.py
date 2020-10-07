from pathlib import Path
from audio_processing import adjust_mp3_amplitude


def main():
    original_mp3_path = Path("../static/button_files/x1_Useful & Misc/x2_oh_my_e57_002032.mp3").absolute()
    adjusted_mp3_path = Path(original_mp3_path.stem + "___adjusted.mp3")
    adjust_mp3_amplitude(original_mp3_path, adjusted_mp3_path)


if __name__ == '__main__':
    main()
