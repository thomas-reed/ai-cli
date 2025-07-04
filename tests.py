import unittest
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file

def test():
    print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
    print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
    print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))


# def test():
#   print(get_file_content("calculator", "main.py"))
#   print(get_file_content("calculator", "pkg/calculator.py"))
#   print(get_file_content("calculator", "/bin/cat"))

# def test():
#     result = get_files_info("calculator", ".")
#     print("Result for current directory:")
#     print(result)
#     print("")

#     result = get_files_info("calculator", "pkg")
#     print("Result for 'pkg' directory:")
#     print(result)

#     result = get_files_info("calculator", "/bin")
#     print("Result for '/bin' directory:")
#     print(result)

#     result = get_files_info("calculator", "../")
#     print("Result for '../' directory:")
#     print(result)


if __name__ == "__main__":
    test()

# class TestFunctions(unittest.TestCase):
#   def test_list_dir_calculator(self):
#     result = get_files_info("calculator", ".")
#     self.assertEqual(
#       result,
#       """
#       - main.py: file_size=575 bytes, is_dir=False
#       - tests.py: file_size=1343 bytes, is_dir=False
#       - pkg: file_size=92 bytes, is_dir=True
#       """,
#     )

#   def test_list_dir_pkg(self):
#     result = get_files_info("calculator", "pkg")
#     self.assertEqual(
#       result,
#       """
#       - calculator.py: file_size=1737 bytes, is_dir=False
#       - render.py: file_size=768 bytes, is_dir=False
#       - __pycache__: file_size=96 bytes, is_dir=True
#       """,
#     )

#   def test_list_dir_bin(self):
#     result = get_files_info("calculator", "/bin")
#     self.assertEqual(
#       result,
#       'Error: Cannot list "/bin" as it is outside the permitted working directory'
#     )

#   def test_list_dir_parent(self):
#     result = get_files_info("calculator", "../")
#     self.assertEqual(
#       result,
#       'Error: Cannot list "../" as it is outside the permitted working directory'
#     )

# if __name__ == "__main__":
#     unittest.main()
