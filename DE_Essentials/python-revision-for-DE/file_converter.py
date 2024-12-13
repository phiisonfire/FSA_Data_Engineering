import json
import os
import glob
import sys

import pandas as pd


def get_column_names(
        schemas: dict, 
        table_name: str, 
        sorting_key: str='column_position'
) -> list[str]:
    columns_detail = schemas.get(table_name)
    columns_detail_sorted = sorted(
        columns_detail, 
        key=lambda column_detail: column_detail.get(sorting_key)
    )
    return list(map(lambda column_detail: column_detail.get('column_name'), columns_detail_sorted))


def get_table_name_from_path(path: str):
    return path.split("/")[2]


def create_dataframe(file_name, column_names):
    return pd.read_csv(
        filepath_or_buffer=file_name,
        names=column_names
    )

def convert(db_name: str) -> None:

    src_file_names = glob.glob(f"data/{db_name}/*/part-*")

    schemas = json.load(open(f'data/{db_name}/schemas.json'))

    for file_name in src_file_names:
        table_name = get_table_name_from_path(file_name)

        write_dir = f"data/retail_db_json/{table_name}"
        write_file_name = write_dir + f"/{table_name}.json"
        os.makedirs(write_dir)

        column_names = get_column_names(schemas, table_name)

        table_df = create_dataframe(file_name, column_names)

        table_df.to_json(
            write_file_name,
            orient='records',
            lines=True)

if __name__ == '__main__':
    db_name = os.environ.get('DB_NAME')
    convert(db_name)
