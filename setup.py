from setuptools import setup, find_packages

setup(
    name = "gamui",
    version = "0.1",
    packages = find_packages(),
    include_package_data = True,
    description = "The gamui module it was developed for create easy and intuitive UI for the pygame module.",
    long_description = open('README.md').read(),
    long_description_content_type = 'text/markdown',
    author = "Alba Luca Francesco",
    author_email = "lucaalbafrancesco@gmail.com",
    url = "https://github.com/lucx-albx/gamui", 
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires = '>=3.12.4'
)