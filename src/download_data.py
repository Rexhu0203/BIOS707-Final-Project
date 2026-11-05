"""Download Challenge 2012 Set A using the exploration notebook's logic."""

from pathlib import Path
import shutil
from urllib.request import urlopen
import zipfile

BASE_URL = "https://physionet.org/files/challenge-2012/1.0.0/"
RAW_DIR = Path(__file__).resolve().parents[1] / "data" / "raw"


def main():
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    for filename in ("set-a.zip", "Outcomes-a.txt"):
        destination = RAW_DIR / filename
        if not destination.exists():
            temporary = destination.with_suffix(destination.suffix + ".part")
            try:
                with urlopen(BASE_URL + filename, timeout=120) as response, temporary.open("wb") as output:
                    shutil.copyfileobj(response, output)
                temporary.replace(destination)
            finally:
                temporary.unlink(missing_ok=True)
        print(filename, destination.stat().st_size, "bytes")

    with zipfile.ZipFile(RAW_DIR / "set-a.zip") as archive:
        for member in archive.infolist():
            target = (RAW_DIR / member.filename).resolve()
            if not target.is_relative_to(RAW_DIR.resolve()):
                raise ValueError("Unsafe ZIP member path")
        archive.extractall(RAW_DIR)
    patient_files = list((RAW_DIR / "set-a").glob("*.txt"))
    if not patient_files:
        raise FileNotFoundError("No patient files found in data/raw/set-a/.")
    print("Extracted patient files:", len(patient_files))


if __name__ == "__main__":
    main()
