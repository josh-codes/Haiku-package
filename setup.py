import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="haiku-Josh-codes", # Replace with your own username
    version="0.4",
    author="Josh",
    author_email="joshua.brest99@gmail.com",
    description="Control your Haiku(TM) devices!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/josh-codes/Haiku-package",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
