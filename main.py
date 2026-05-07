import sys
import subprocess
from pathlib import Path


def play(wav_path: Path) -> None:
    path = str(wav_path)
    if sys.platform == "win32":
        import winsound
        winsound.PlaySound(path, winsound.SND_FILENAME)
    elif sys.platform == "darwin":
        subprocess.run(["afplay", path], check=True)
    else:
        subprocess.run(["aplay", path], check=True)


def main():
    wav_path = Path(__file__).parent / "ulala.wav"
    play(wav_path)


if __name__ == "__main__":
    main()
