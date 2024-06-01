from project import *

def main():
    test_task_init()
    test_saved()
    test_find()

def test_task_init():
    work = Task("work", 15)

    assert work.duration == 15
    assert work.msg == f"Now is {work.name} time, you will have to do it for {work.duration} minutes"
    assert work.name == "work"
    assert len(work.tasks) == 1

def test_saved():
    assert saved("b")

def test_find():
    assert find("saved.json")
    
if __name__ == "__main__":
    main()