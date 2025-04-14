from setuptools import setup, find_packages

setup(
    name="ads-utp",
    version="0.0.1",
    author="Aleksandar Karastoyanov",
    author_email="karastoqnov.alexandar@gmail.com",
    description="Algorithms and Data Structures in Python",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="",
    packages=find_packages(),
    install_requires=[
        # List dependencies
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)