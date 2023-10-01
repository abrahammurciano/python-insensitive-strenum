import pytest

from insensitive_strenum import InsensitiveStrEnum


class Foo(InsensitiveStrEnum):
    BAR = "bar"
    BAZ = "baz"


def test_insensitive_strenum():
    assert Foo("BAR") is Foo.BAR
    assert Foo("bar") is Foo.BAR
    assert Foo("Bar") is Foo.BAR
    assert Foo("bAr") is Foo.BAR
    assert Foo("BAZ") is Foo.BAZ
    assert Foo("baz") is Foo.BAZ
    assert Foo("Baz") is Foo.BAZ
    assert Foo("bAz") is Foo.BAZ


def test_insensitive_strenum_missing():
    with pytest.raises(ValueError):
        Foo("qux")
