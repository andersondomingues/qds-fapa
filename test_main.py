from main import soma, subtracao


def test_soma():
    assert soma(1, 2) == 3

def test_subtracao():
    assert subtracao(1, 2) == -1