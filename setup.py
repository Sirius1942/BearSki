from setuptools import setup
import src.BearSki
find_packages
setup (
    name =BearSki.__title__,
    version = BearSki.__version__,
    packages = find_packages('src'),  # 包含所有src中的包
    package_dir = {'':'src'},   # 告诉distutils包都在src下
    package_data = {
        # 任何包中含有.txt文件，都包含它
        '': ['*.txt'],
        # 包含demo包data文件夹中的 *.dat文件
        'BearSki': ['data/*.dat'],
    },
    description = BearSki.__description__,
    author = BearSki.__author__,
    url = BearSki.__url__,
    license =BearSki.__license__,
    py_modules=['hello'],
    install_requires = ["requests","har2case"],
    entry_points = {
        'console_scripts': [
            'BearSki = src.BearSki.BearCLI:main'
        ]
    }
)