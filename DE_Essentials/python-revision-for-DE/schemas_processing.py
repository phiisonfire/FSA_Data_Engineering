import json
import logging
from typing import List, Dict, Any

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def load_schemas(file_path: str) -> Dict:
    try:
        with open(file_path, 'r') as fp:
            schemas = json.load(fp)
            logger.info(f"Successfully loaded schemas from {file_path}.")
            return schemas
    except FileNotFoundError:
        logger.error(f"File not found: {file_path}")
        raise
    except json.JSONDecodeError as e:
        logger.error(f"Failed to parse JSON from {file_path}: {e}")
        raise

def get_column_names(
    schemas: Dict,
    table_name: str,
    sorting_key: str = "column_position"
) -> List[str]:
    if table_name not in schemas:
        logger.error(f"Table {table_name} not found in schemas!")
        raise ValueError(f"Table {table_name} not found in schemas!")
    
    column_details = schemas.get(table_name)
    if not isinstance(column_details, list) or not all(isinstance(col, dict) for col in column_details):
        logger.error("Invalid schema format for table '%s'. Expected a list of dictionaries.", table_name)
        raise ValueError(f"Invalid schema format for table '{table_name}'.")
    
    try:
        sorted_columns = sorted(
            column_details,
            key=lambda col: col.get(sorting_key)
        )
        column_names = [col.get("column_name") for col in sorted_columns]
        logger.info(f"Retrieved column names for table {table_name}: {column_names}")
        return column_names
    except Exception as e:
        logger.exception(f"An error occurred while retrieving column names for table {table_name}")
        raise

if __name__ == "__main__":
    schemas_path = "data/retail_db/schemas.json"
    try:
        schemas = load_schemas(schemas_path)
        table_name = "orderss"
        column_names = get_column_names(schemas, table_name)
        print(f"Column names for table '{table_name}': {column_names}")
    except Exception as e:
        logger.error("Failed to retrieve column names: %s", e)