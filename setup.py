"""""
setup module
"""""
from pathlib import Path

import setuptools
import os

app = Path(__file__).resolve(strict=True).parent.parent
here = Path(__file__).resolve(strict=True).parent


__al__ = ["__version__"]

with open(os.path.join(here, 'VERSION')) as f:
    __version__ = f.read().strip()

with open("README.md", "r") as fh:
    long_description = fh.read()

with open(os.path.join(here, 'MANIFEST.in')) as f:
    MANIFEST = f.read().strip()

extra_files = [
    os.path.join(here, 'VERSION'),
    os.path.join(here, 'README.md'),
    os.path.join(here, 'MANIFEST.in')
]

setuptools.setup(
    name="djangular-serve",
    version=__version__,

    include_package_data=True,
    package_data={"": extra_files},
    project_urls={
        "Bug Tracker": "https://github.com/forafekt/djangular-serve/issues",
        "Documentation": "https://github.com/forafekt/djangular-serve/tree/master/djangular_serve/docs",
        "Source Code": "https://github.com/forafekt/djangular-serve",
    },

    packages=setuptools.find_packages(),

    entry_points={
        'console_scripts': [
            'build=djangular_serve:main',
        ],
    },

    author="Jonny Doyle",
    author_email="jonathan.d@programmer.net",
    license="MIT",
    description="Django + Angular client for complete project management & development.",
    keywords="django angular client template boilerplate git automate",
    platform="Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/forafekt/djangular-serve",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
    ],
    install_requires=[
        "Django"
    ],
    python_requires='>=3.6',
)
