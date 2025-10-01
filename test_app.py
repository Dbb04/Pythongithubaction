from app import add

def test_add_function():
    """This test checks the add function with various inputs."""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0