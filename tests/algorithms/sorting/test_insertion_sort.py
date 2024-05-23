import pytest

from src.algorithms import insertion_sort, merge, selection_sort


@pytest.fixture(params=[insertion_sort, selection_sort])
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
    def test_sort_asc(self, sort_method, data, expected):
        sort_method(data)
        assert data == expected

    @pytest.mark.parametrize(
        "data, expected",
        [
            ([-1, 2, 1, 4, 2], [4, 2, 2, 1, -1]),
            ([-1.0, 2.2, 2], [2.2, 2, -1.0]),
            ([-0, 4, -6.2, -2, -0], [4, 0, 0, -2, -6.2]),
            ([], []),
            (None, None),
        ],
    )
    def test_sort_desc(self, sort_method, data, expected):
        sort_method(data, desc=True)
        assert data == expected

    @pytest.mark.parametrize(
        "data, left, mid, right, expected",
        [
            ([4, 7, 9, 9, -1, 6, 8, 9], 0, 3, 7, [-1, 4, 6, 7, 8, 9, 9, 9]),
            ([4, 7, 9, 9, -1, 6, 8, 9], 1, 3, 5, [4, -1, 6, 7, 9, 9, 8, 9]),
        ],
    )
    def test_merge(self, data, left, mid, right, expected):
        merge(data, left, mid, right)
        assert data == expected
