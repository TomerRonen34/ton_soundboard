from pathlib import Path
from tempfile import TemporaryDirectory
from subprocess import check_output

from scipy.io import wavfile
import matplotlib.pyplot as plt
import numpy as np

from ton_soundboard.config import LAME_EXE_PATH


def adjust_mp3_amplitude(original_mp3_path: Path, adjusted_mp3_path: Path, desired_max_amplitude: int = 30_000):
    with TemporaryDirectory() as tmp_dir:
        converted_wav_path = Path(tmp_dir) / "converted.wav"
        adjusted_wav_path = Path(tmp_dir) / "adjusted.wav"

        _convert_mp3_to_wav(original_mp3_path, converted_wav_path)
        _adjust_wav_amplitude(converted_wav_path, adjusted_wav_path, desired_max_amplitude)
        _convert_wav_to_mp3(adjusted_wav_path, adjusted_mp3_path)


def _convert_mp3_to_wav(mp3_path: Path, wav_path: Path) -> None:
    conversion_command = f'"{LAME_EXE_PATH}" --decode "{mp3_path}" "{wav_path}"'
    check_output(conversion_command, shell=True)


def _convert_wav_to_mp3(wav_path: Path, mp3_path: Path) -> None:
    conversion_command = f'"{LAME_EXE_PATH}" -V2 "{wav_path}" "{mp3_path}"'
    check_output(conversion_command, shell=True)


def _adjust_wav_amplitude(input_wav_path: Path, output_wav_path: Path,
                          desired_max_amplitude: int, clip_quantile: float = 0.995) -> None:
    sample_rate, audio_data = wavfile.read(input_wav_path)
    adjusted_audio_data = _linearly_adjust_amplitude(audio_data, desired_max_amplitude, clip_quantile)
    wavfile.write(output_wav_path, sample_rate, adjusted_audio_data)


def _linearly_adjust_amplitude(audio_data: np.ndarray,
                               desired_max_amplitude: int,
                               clip_quantile: float) -> np.ndarray:
    value_at_clip_quantile = np.quantile(audio_data.flat, clip_quantile)
    adjusted_audio_data = audio_data / value_at_clip_quantile * desired_max_amplitude
    adjusted_audio_data = np.clip(adjusted_audio_data, a_min=-desired_max_amplitude, a_max=desired_max_amplitude)
    adjusted_audio_data = adjusted_audio_data.astype(audio_data.dtype)
    return adjusted_audio_data


def plot_audio(audio_data, sample_rate):
    length = audio_data.shape[0] / sample_rate
    time = np.linspace(0., length, audio_data.shape[0])
    plt.plot(time, audio_data[:, 0], label="Left channel")
    plt.plot(time, audio_data[:, 1], label="Right channel")
    plt.legend()
    plt.xlabel("Time [s]")
    plt.ylabel("Amplitude")
    plt.show()
