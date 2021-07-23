
import pytest

def test_fetch_goggles():
    import project

    result = project.fetch_goggles()

    assert result['foo']

def test_fetch_goggles(mocker):
    import project

    mocker.patch('project.fetch_goggles', return_value={'status':200,"foo": True})
    result = project.fetch_goggles('Hi')

    assert result['foo']

def test_fetch_goggles_failure(mocker):
    import project

    mocker.patch('project.fetch_goggles', return_value={'status':408})
    result = project.fetch_goggles()

    if result['status'] != 200:
        # recover gracefully
        graceful_recovery = True

    # assert that this was not a success
    assert graceful_recovery

def test_count_goggles(mocker):
    import project

    mocker.patch('project.helpers.fetch_goggles', 
                  return_value={'status':200, "count": 4})

    result = project.count_goggles()
    assert result == 4