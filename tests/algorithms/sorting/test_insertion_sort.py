import pytest

from src.algorithms import insertion_sort


@pytest.fixture(params=[insertion_sort])
def sort_method(request):
    return request.param


class TestSorting:
    @pytest.mark.parametrize(
        "data, expected",
        [
            ([-1, 2, 1, 4, 2], [-1, 1, 2, 2, 4]),
            ([-1.0, 2.2, 2], [-1.0, 2, 2.2]),
            ([-0, 4, -6.2, -2, -0], [-6.2, -2, 0, 0, 4]),
            ([], []),
            (None, None),
        ],
    )
    def test_sort(self, sort_method, data, expected):
        sort_method(data)
        assert data == expected