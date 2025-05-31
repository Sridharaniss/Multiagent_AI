from multiprocessing import Manager
from datetime import datetime
import uuid

# Start shared memory store using Manager
_manager = Manager()
_shared_memory = _manager.list()

def log_result(source, intent_type, extracted_data, thread_id=None):
    """Log result into shared memory."""
    memory_entry = {
        "id": str(uuid.uuid4()),
        "source": source,              # e.g., "email", "json"
        "type": intent_type,          # e.g., "RFQ", "Invoice"
        "timestamp": datetime.utcnow().isoformat(),
        "extracted_data": extracted_data,
        "thread_id": thread_id or str(uuid.uuid4())
    }
    _shared_memory.append(memory_entry)

def get_all_logs():
    return list(_shared_memory)

def get_logs_by_type(intent_type):
    return [entry for entry in _shared_memory if entry['type'] == intent_type]

def clear_logs():
    _shared_memory[:] = []
