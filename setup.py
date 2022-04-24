import json
from setuptools import setup

meta = json.load(open("package.json", encoding="utf-8"))

setup(
    name=meta["name"],
    author=meta["author"],
    author_email=meta["email"],
    description=meta["description"],
    version=meta["version"],
    packages=["multitool"],
    license=open("LICENSE", encoding="utf-8").read(),
    long_description=open("README", encoding="utf-8").read(),
    keywords=meta["keywords"],
    url=meta["url"],
    entry_points={'console_scripts': [
        'multitool = multitool.__main__:main',
        'mtool = multitool.__main__:main'
    ]},
    data_files=[("assets", ['AllWords.txt', 'en_thesaurus.jsonl.txt', 'Synonyms.json', 'Words_Frequency.json', 'Words_Length.json'])]
)
