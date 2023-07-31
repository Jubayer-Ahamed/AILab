import os

file_name = "Jubayer.txt"
content_to_write = "Hello, I am your friend."

if os.path.exists(file_name):
    f = open("Jubayer.txt", "a")
    f.write(content_to_write)
    f.close()

    f = open("Jubayer.txt", "r")
    print(f.read())
    f.close()


    os.remove(file_name)
    print(f"{file_name} deleted successfully.")
else:
    print(f"There is no file named '{file_name}'.")
