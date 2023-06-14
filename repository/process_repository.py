from model.process import Process
from uuid import UUID

process_storage = {}


def save(process: Process):
    process_storage[process.id] = process
    print(process_storage)


def get_by_id(process_id: UUID):
    process = process_storage[process_id]
    print(process)
    return process
