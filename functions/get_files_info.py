import os

def get_files_info(working_directory, directory=None):
  full_path = os.path.abspath(os.path.join(working_directory, directory))
  if not full_path.startswith(os.path.abspath(working_directory)):
    return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
  if not os.path.isdir(full_path):
    return f'Error: "{directory}" is not a directory'
  try:
    contents_list = os.listdir(full_path)
    return "\n".join(list(map(lambda file: file_metadata(file, full_path), contents_list)))
  except Exception as e:
    return f"Error listing files: {e}"

def file_metadata(file, path):
  file_path = os.path.join(path, file)
  return f"- {file}: file_size={os.path.getsize(file_path)} bytes, is_dir={os.path.isdir(file_path)}"
