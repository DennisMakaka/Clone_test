from models.engine.file_storage import FileStorage

# Create a unique FileStorage instance for your application
storage = FileStorage()

# Load serialized data from the JSON file into memory
storage.reload()

