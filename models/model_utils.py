from typing import Any, Dict

from PySide6.QtSql import QSqlField, QSqlRecord


def QSqlRecordToDict(record: QSqlRecord) -> Dict[str, Any]:
    data_dict = {}

    for i in range(record.count()):
        field = record.field(i)
        column_name = field.name()
        value = record.value(i)
        data_dict[column_name] = value

    return data_dict


def dictToQSqlRecord(data_dict: Dict[str, Any]) -> QSqlRecord:
    record = QSqlRecord()

    for column_name, value in data_dict.items():
        field = QSqlField(column_name)
        field.setValue(value)
        record.append(field)

    return record
