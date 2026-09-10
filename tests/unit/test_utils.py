import pytest

from app.utils import predict


# Utilisation de parametrize pour tester plusieurs cas nominaux proprement
@pytest.mark.parametrize(
    "features, expected",
    [
        ([1, 2, 3], [2, 4, 6]),
        ([5], [10]),
        ([1.5, 2.5], [3, 5]),
    ],
)
def test_predict_logic(features, expected):
    assert predict(features) == expected


def test_predict_limit():
    entry_data = [[0], [], [-2], [-1000], [2000000]]
    expected_data = [[0], [], [-4], [-2000], [4000000]]
    for i in range(len(entry_data)):
        assert predict(entry_data[i]) == expected_data[i]


def test_invalid_cases():
    invalid_features = [None, "abc", {}, [1, "abc", 3], [1, None, 3]]

    for feature in invalid_features:
        # pytest.raises vérifie que la fonction lève une exception (ex: TypeError ou ValueError)
        with pytest.raises((TypeError, ValueError)):
            predict(feature)