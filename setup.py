import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="utility-scripts-struckchure",
    version="0.0.1",
    author="Mohammed Al Ameen",
    author_email="ameenmohammed2311@gmail.com",
    description="Composition of utilities for commonly executed tasks",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/struckchure/utility-scripts",
    project_urls={
        "Bug Tracker": "https://github.com/struckchure/utility-scripts/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "."},
    packages=setuptools.find_packages(where="."),
    python_requires=">=3.6",
)