from model.process import Process

process_storage = {}

def save(process: Process):
    process_storage[process.id] = process

def get_by_id(process: str):
    return process_storage[process.id]
