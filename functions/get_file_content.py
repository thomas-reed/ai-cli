import os
from config import MAX_CHARS

def get_file_content(working_directory, file_path):
  full_path = os.path.abspath(os.path.join(working_directory, file_path))
  if not full_path.startswith(os.path.abspath(working_directory)):
    return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
  if not os.path.isfile(full_path):
    return f'Error: File not found or is not a regular file: "{file_path}"'

  try:
    with open(full_path, "r") as f:
      file_content_string = f.read(MAX_CHARS)
    if len(file_content_string) >= MAX_CHARS:
      return f'{file_content_string}[...File "{file_path}" truncated at {MAX_CHARS} characters]'
    return file_content_string
  except Exception as e:
    return f"Error getting file content: {e}"