__version__ = "0.2.9"

# Re-export this
from ._safetensors_rust import SafetensorError, deserialize, safe_open, serialize, serialize_file  # noqa: F401
