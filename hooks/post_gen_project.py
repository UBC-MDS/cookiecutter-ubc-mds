import os
import shutil
os.chdir("..")
shutil.rmtree("bar")

print(
    "\nThis cookiecutter has moved. Please use:\n\n"
    "\tcookiecutter https://github.com/py-pkgs/py-pkgs-cookiecutter.git"
)