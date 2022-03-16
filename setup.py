import json
from setuptools import setup

meta = json.load(open("package.json"))

setup(
    name=meta["name"],
    author=meta["author"],
    author_email=meta["email"],
    packages=["multitool"],
    license=open("LICENSE").read(),
    long_description=open("README").read(),
    keywords=meta["keywords"],
    url=meta["url"],
    entry_points={'console_scripts': ['multitool = multitool.__main__:main']}
)
