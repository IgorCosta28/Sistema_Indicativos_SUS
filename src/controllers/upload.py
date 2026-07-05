import json
import os
import shutil
from pathlib import Path

from rich import print

async def upload(input, files):

    data = json.loads(input)

    save_files = os.path.join("upload", data["year"], data["period"], data["team"])

    os.makedirs(save_files, exist_ok=True)

    for file in files:
        with open(f"{save_files}/{file.filename}", "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

    res = {"path": save_files, "files": os.listdir(save_files)}

    return res


async def get_upload_all():
    return Path('upload').rglob('*')

