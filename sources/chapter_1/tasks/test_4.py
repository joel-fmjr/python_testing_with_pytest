"""Test the Task data type."""

import time
import pytest
from collections import namedtuple

Task = namedtuple('Task', ['summary', 'owner', 'done', 'id'])
Task.__new__.__defaults__ = (None, None, False, None)


def test_asdict():
    """_asdict should return a dictionary."""
    t_task = Task('do something', 'Joel', True, 21)
    t_dict = t_task._asdict()
    expected = {'summary': 'do something',
                'owner': 'Joel', 'done': True, 'id': 21}
    assert t_dict == expected


@pytest.mark.run_these_please
def test_replace():
    """replace() should change in passed in fields."""
    time.sleep(0.1)
    t_before = Task('finish book', 'Brian', False)
    t_after = t_before._replace(id=10, done=True)
    t_expected = Task('finish book', 'Brian', True, 10)
    assert t_after == t_expected
