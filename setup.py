from setuptools import setup, find_packages

setup(
    name='PyTPG',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'autorom',
        'autorom-accept-rom-license',
        'click',
        'cloudpickle',
        'contourpy',
        'cycler',
        'fonttools',
        'gym[all]',
        'gym-notices',
        'importlib-resources',
        'ipdb',
        'kiwisolver',
        'llvmlite',
        'matplotlib',
        'numba',
        'numpy',
        'pandas',
        'pillow',
        'pyparsing',
        'seaborn',
        'tqdm',
        'tzdata',
        'unittest-xml-reporting',
        'networkx',
        'sphinx',
        'sphinx_book_theme',
        'myst_parser'
    ],
)
