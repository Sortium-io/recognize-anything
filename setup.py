from setuptools import setup, find_packages

REQ_LOCATION = "requirements.txt"

def get_requirements():
    with open(REQ_LOCATION, encoding="utf-8") as f:
        requirements = f.read().splitlines()
        return [r for r in requirements if not r.startswith("--") and not r.startswith("#")]


setup(
    name="ram",
    version="0.0.1",
    description="Recognize Anything Plus Model, Recognize Anything Model and Tag2Text Model",
    install_requires=get_requirements(),
    packages=["ram", "ram.configs", "ram.data", "ram.utils", "ram.models"],
    package_data = {
        '': ['*.yaml', '*.json', '*.txt', 'swin/*.yaml', 'swin/*.json'],
    },
    package_dir={
        "": ".",
        "configs": "ram/configs",
        "data": "ram/data",
        "models": "ram/models",
        "utils": "ram/utils",
    },
)
