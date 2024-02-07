from setuptools import setup, find_packages

setup(
    name='your_package_name',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'ale-py',
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
        'pdoc',
        'pillow',
        'pyparsing',
        'seaborn',
        'tqdm',
        'tzdata',
        'unittest-xml-reporting'
    ],
)
