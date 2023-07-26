from setuptools import setup, find_packages
from AIMD_extractor.version import __version__ as VERSION

readme = "README.md"
long_description = open(readme).read()

setup(
    name="AIMD_extractor",
    version=VERSION,
    description="Python utilities for VASP AIMD analysis",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Frazer N. Forrester",
    author_email="f.forrester2@ncl.ac.uk",
    url="https://github.com/fforrester/AIMD_extractor",
    download_url="https://github.com/fforrester/AIMD_extractor/archive/{}.tar.gz".format(VERSION),
    license="MIT",
    packages=find_packages(),
    package_data={
        'AIMD_extractor': ['temperature_variations.json', 'run_variations.json']
    },
    install_requires=["pymatgen", "pymatgen-analysis-diffusion", "numpy"],
    python_requires=">=3.7",
    entry_points={
        'console_scripts': [
            'AIMD_extractor = AIMD_extractor.AIMD_extractor:main',
        ],
    },
)

