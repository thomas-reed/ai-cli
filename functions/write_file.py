import os

def write_file(working_directory, file_path, content):
  full_path = os.path.abspath(os.path.join(working_directory, file_path))
  if not full_path.startswith(os.path.abspath(working_directory)):
    return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

  parent_dirs = os.path.dirname(full_path)
  if not os.path.exists(parent_dirs):
    try:
      os.makedirs(parent_dirs)
    except Exception as e:
      return f"Error creating parent directories: {e}"
  try:
    with open(full_path, "w") as f:
      f.write(content)
    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
  except Exception as e:
    return f"Error writing file: {e}"
