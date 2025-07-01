import itertools
from typing import Iterable

import pytest

from insensitive_strenum import InsensitiveStrEnum


class EnumValues(InsensitiveStrEnum):
    LOWER = "lower"
    UPPER = "UPPER"
    MIXED = "MiXeD"


@pytest.fixture(params=[EnumValues.LOWER, EnumValues.UPPER, EnumValues.MIXED])
def member(request: pytest.FixtureRequest) -> EnumValues:
    return request.param


@pytest.fixture
def values(member: EnumValues) -> Iterable[str]:
    return (
        "".join(
            char.upper() if upper else char.lower()
            for char, upper in zip(member, cases)
        )
        for cases in itertools.product((False, True), repeat=len(member))
    )


def test_insensitive_strenum(member: EnumValues, values: Iterable[str]) -> None:
    for value in values:
        assert EnumValues(value) is member


def test_insensitive_strenum_missing() -> None:
    with pytest.raises(ValueError):
        EnumValues("not-a-member")
