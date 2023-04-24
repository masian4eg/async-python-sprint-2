from datetime import datetime
from typing import Callable, Optional, Dict, Any, Generator, List


class Job:
    def __init__(self,
                 task: Callable,
                 task_str: str,
                 start_at: datetime,
                 tries: int = 0,
                 dependencies: Optional[List['Job']] = None):

        self.start_at = start_at
        self.tries = tries
        self.dependencies = dependencies
        self.task = task
        self.task_str = task_str
        self.actual_tries: int = 0

    def run(self) -> Generator[None, None, None]:
        if self.check_run():
            self.task() # если я добавлю сюда в аргумент None, то получу TypeError: task_1() takes 0 positional arguments but 1 was given
            _ = (yield)
            yield True

    def dict(self) -> Dict[str, Any]:
        return {
            'task_str': self.task_str,
            'start_at': self.start_at.timestamp(),
            'tries': self.tries,
            'dependencies': self.dependencies
        }

    def check_run(self) -> bool:
        if datetime.now() < self.start_at:
            return False
        if self.dependencies:
            return False
        if self.actual_tries >= self.tries:
            return False
        return True
