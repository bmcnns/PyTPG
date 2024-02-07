from setuptools import setup, find_packages

setup(
    name='your_package_name',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'ale-py==0.8.1',
        'autorom==0.4.2',
        'autorom-accept-rom-license==0.6.1',
        'click==8.1.7',
        'cloudpickle==2.2.1',
        'contourpy==1.1.1',
        'cycler==0.12.0',
        'fonttools==4.43.0',
        'gym[all]==0.26.2',
        'gym-notices==0.0.8',
        'importlib-resources==6.1.0',
        'ipdb==0.13.13',
        'kiwisolver==1.4.5',
        'llvmlite==0.41.0',
        'matplotlib==3.8.0',
        'numba==0.58.0',
        'numpy==1.25.2',
        'pandas==2.1.3',
        'pdoc',  # Include pdoc as a dependency
        'pillow==10.0.1',
        'pyparsing==3.1.1',
        'seaborn==0.13.0',
        'tqdm==4.66.1',
        'tzdata==2023.3',
        'unittest-xml-reporting==3.2.0'
    ],
)
