
def test_fetch_goggles():
    import project

    result = project.fetch_goggles()

    assert result['foo']