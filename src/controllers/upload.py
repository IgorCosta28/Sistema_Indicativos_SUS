import json
import os
import shutil
from uuid import uuid4

from rich import print
from sqlalchemy import select
from sqlalchemy.orm import load_only, selectinload

from src.db.config.connection import SessionLocal
from src.db.models.files import Files
from src.db.models.group import Groups
from src.util.extrated_name_file import extrated_name_file


async def upload(input, files):

    data = json.loads(input)

    folder_uuid = str(uuid4())

    save_files = os.path.join("src", "upload", folder_uuid)

    os.makedirs(save_files, exist_ok=True)

    async with SessionLocal() as session:

        groups = Groups(
            year=data["year"],
            periodic=data["period"],
            team=data["team"],
            uuid=folder_uuid,
        )

        session.add(groups)

        # salva no banco
        await session.flush()

        for file in files:

            name_file_indicative = extrated_name_file(file)

            path_file = os.path.join(save_files, name_file_indicative)

            with open(path_file, "wb") as buffer:
                shutil.copyfileobj(file.file, buffer)

            file_db = Files(
                indicative=name_file_indicative.replace(".pdf", ""),
                name=name_file_indicative,
                path=path_file,
                group_id=groups.id,
                status="ativo",
            )

            session.add(file_db)

            await session.commit()

            await session.refresh(groups)

    return {"save": "true"}


async def get_upload_all():
    async with SessionLocal() as session:
        stmt = (
            select(Groups)
            .options(load_only(Groups.id), selectinload(Groups.files))
            .order_by(Groups.id)
        )

        result = await session.execute(stmt)

        return result.mappings().all()
