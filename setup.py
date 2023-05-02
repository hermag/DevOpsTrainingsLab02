import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="devopstraininglab02", # Replace with your username
    version="1.0.0",
    author="Erekle Magradze",
    author_email="erekle.magradze@iliauni.edu.ge",
    description="Test python whl package for training purposes Lab Course 02.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hermag/DevOpsTrainingsLab02",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    options = {"bdist_wheel": {"universal":True}},
    python_requires='>=3.7',
)

