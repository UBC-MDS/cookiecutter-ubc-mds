import os
os.chdir("..")
os.rmdir("bar")

print(
    "This cookiecutter has moved. Please use:\n\n"
    "\tcookiecutter https://github.com/py-pkgs/py-pkgs-cookiecutter.git"
)