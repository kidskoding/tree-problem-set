import pytest
from helpers import build, load

merge_bsts = load("39_merge_two_bsts").merge_bsts


@pytest.mark.parametrize(
    "a, b, expected",
    [
        ([5, 3, 6, 2, 4], [2, 1, 3, None, None, None, 7], [1, 2, 2, 3, 3, 4, 5, 6, 7]),
        ([1], [], [1]),
        ([], [2, 1, 3], [1, 2, 3]),
        ([], [], []),
    ],
)
def test_merge_bsts(a, b, expected):
    assert merge_bsts(build(a), build(b)) == expected
