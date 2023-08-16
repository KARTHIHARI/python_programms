import os

# os.environ["test"]="ok"

# print(os.environ)

[print(i) for i in os.environ["Path"].split(";")]