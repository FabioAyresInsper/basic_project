# pylint: disable=missing-docstring
import requests
import io
import zipfile
from pathlib import Path


def main():
    url = 'https://archive.ics.uci.edu/static/public/186/wine+quality.zip'
    data_dir = Path(__file__).parents[1] / 'data' / 'orig'
    data_dir.mkdir(parents=True, exist_ok=True)

    with requests.get(url) as r:
        if r.status_code == 200:
            file = io.BytesIO(r.content)
            with zipfile.ZipFile(file, mode='r') as zip:
                zip.extractall(data_dir)


if __name__ == '__main__':
    main()
