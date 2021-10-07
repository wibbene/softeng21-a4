import  Pytest


from pmgr.project import Project

@pytest.fixture(scope="function")
def proj1():
    proj1 = Project("test1")
    yield proj1
    proj1.delete()



def test_add_single_task(proj1):
    proj1.add_task("test_task")
    test_task_list = proj1.get_tasks()
    assert "test_task" is in test_task_list

def test_add_mult_task(proj1):
    proj1.add_task("test_task1")
    proj1.add_task("test_task2")
    test_task_list = proj1.get_tasks()
    assert "test_task1" is in test_task_list and "test_task2" is in test_task_list


def test_fail_add_dup(proj1):
    proj1.add_task("test_task")
    with pytest.raise(TaskException):
        proj1.add_task("test_task")


def test_fail_remove_nonexistent(proj1):
    with pytest.raise(TaskException):
        proj1.remove_task("test_task")

def test_remove_single_task(proj1):
    proj1.add_task("test_task")
    test_task_list = proj1.get_tasks()
    proj1.remove_task("test_task")
    assert "test_task" is not in test_tasK_list

def test_remove_multi_st_task(proj1):
    proj1.add_task("test_task1")
    proj1.add_task("test_task2")
    proj1.remove_task("test_task1")
    proj1.remove_task("test_task2")
    test_task_list = proj1.get_tasks()
    assert len(test_task_list) == 0


def test_remove_multi_st_task(proj1):
    proj1.add_task("test_task1")
    proj1.add_task("test_task2")
    proj1.remove_task("test_task1")
    test_task_list = proj1.get_tasks()
    assert "test_task1" is not in test_task_list and "test_task2" is in test_task_list

def test_show_empty_task(proj1):
    test_task_list = proj1.get_tasks()
    assert len(test_task_list) == 0

def test_show_single_task(proj1):
    proj1.add_task("test_task")
    test_task_list = proj1.get_tasks()
    assert len(test_task_list) == 1

def test_show_multi_task(proj1):
    proj1.add_task("test_task1")
    proj1.add_task("test_task2")
    test_task_list = proj1.get_tasks()
    assert len(test_task_list) == 2



