import os
import subprocess

def run_python_file(working_directory, file_path):
  full_path = os.path.abspath(os.path.join(working_directory, file_path))
  if not full_path.startswith(os.path.abspath(working_directory)):
    return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
  if not os.path.exists(full_path):
    return f'Error: File "{file_path}" not found.'
  if not full_path.endswith(".py"):
    return f'Error: "{file_path}" is not a Python file.'

  try:
    output = []
    result = subprocess.run(["python3", full_path], capture_output=True, timeout=30)
    if not result.returncode == 0:
      output.append(f"Process exited with code {result.returncode}")
    if not result.stdout == b'':
      output.append(f"STDOUT:{result.stdout.decode("utf-8")}")
    if not result.stderr == b'':
      output.append(f"STDERR: {result.stderr.decode("utf-8")}")
    if len(output) == 0:
      return "No output produced."
    return "\n".join(output)
  except Exception as e:
    return f"Error: executing Python file: {e}"
    