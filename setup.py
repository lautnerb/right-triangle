from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="right-triangle",
    version="0.1",
    packages=[],
    py_modules="right_triangle",
    url="https://github.com/lautnerb/right-triangle",
    license="Unlicense",
    author="Balazs Lautner",
    author_email="lautner.balazs@gmail.com",
    description="Simple Python package that can be used to do calculations with right-angled triangles",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[],
    python_requires='~=3.7',
)
