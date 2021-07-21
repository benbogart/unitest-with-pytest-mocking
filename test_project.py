
def test_fetch_goggles():
    import project

    result = project.fetch_goggles()

    assert result['foo']

def test_fetch_goggles(mocker):
    import project

    mocker.patch('project.fetch_goggles', return_value={'status':200,"foo": True})
    result = project.fetch_goggles('Hi')

    assert result['foo']


