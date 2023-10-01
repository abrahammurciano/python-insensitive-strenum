# insensitive-strenum
A case insensitive StrEnum

## Installation

You can install this package with pip or conda.
```sh
$ pip install insensitive-strenum
```
```sh
$ conda install -c abrahammurciano insensitive-strenum
```

## Links

[![Documentation](https://img.shields.io/badge/Documentation-C61C3E?style=for-the-badge&logo=Read+the+Docs&logoColor=%23FFFFFF)](https://abrahammurciano.github.io/python-insensitive-strenum)

[![Source Code - GitHub](https://img.shields.io/badge/Source_Code-GitHub-181717?style=for-the-badge&logo=GitHub&logoColor=%23FFFFFF)](https://github.com/abrahammurciano/python-insensitive-strenum.git)

[![PyPI - insensitive-strenum](https://img.shields.io/badge/PyPI-insensitive_strenum-006DAD?style=for-the-badge&logo=PyPI&logoColor=%23FFD242)](https://pypi.org/project/insensitive-strenum/)

[![Anaconda - insensitive-strenum](https://img.shields.io/badge/Anaconda-insensitive_strenum-44A833?style=for-the-badge&logo=Anaconda&logoColor=%23FFFFFF)](https://anaconda.org/abrahammurciano/insensitive-strenum)

## Usage

```python
from insensitive_strenum import InsensitiveStrEnum

class Color(InsensitiveStrEnum):
	RED = 'red'
	GREEN = 'green'
	BLUE = 'blue'
```

```python
>>> Color('RED')
<Color.RED: 'red'>
>>> Color('red')
<Color.RED: 'red'>
>>> Color('Red')
<Color.RED: 'red'>
```