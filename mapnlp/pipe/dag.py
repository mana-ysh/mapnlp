
from typing import Tuple

from mapnlp.data.base import InputText
from mapnlp.pipe.base import InitialPipe, NLPPipe


class NLPTaskDAG():
    INITIAL = InitialPipe()

    def __init__(self, name: str):
        self.dag_name = name
        # dag as connection list
        self._dag = []
        self._initial_tasks = []
        self._task_id2task = {}

    def add_task_dep(self, from_to_task: Tuple['NLPPipe', 'NLPPipe']):
        from_task, to_task = from_to_task
        if from_task.id == self.INITIAL.ID:
            self._initial_tasks.append(to_task)

        if from_task.id not in self._task_id2task:
            self._task_id2task[from_task.id] = from_task

        if to_task.id not in self._task_id2task:
            self._task_id2task[to_task.id] = to_task

        self._dag.append((from_task.id, to_task.id))

    def process(self, input_txt: InputText, **kwargs) -> InputText:
        if type(input_txt) == str:
            input_txt = InputText(input_txt)

        if len(self._initial_tasks) == 0:
            raise RuntimeError("No initial task. Please set initial task")

        task_ids = self._get_task_order()
        for _id in task_ids:
            _task = self._task_id2task[_id]
            _task.process(input_txt, **kwargs)
        return input_txt

    def _get_task_order(self):
        """
        determine task order (breadth-first)
        """
        max_depth = len(self._task_id2task)

        # initialized depth
        _task_id2depth = {}
        for _id in self._task_id2task.keys():
            if _id == self.INITIAL.ID:
                _task_id2depth[_id] = 0
            else:
                _task_id2depth[_id] = -1

        # iteratively update depth
        for _ in range(max_depth):
            for (from_tn, to_tn) in self._dag:
                from_depth = _task_id2depth[from_tn]
                # update
                if from_depth > -1:
                    _task_id2depth[to_tn] = from_depth + 1

        assert all([depth > -1 for depth in _task_id2depth.values()]), \
            "Contain the task within invalid depth. maybe have non-connected task"

        task_ids = sorted(list(_task_id2depth.keys()), key=lambda x: _task_id2depth[x])
        assert task_ids[0] == self.INITIAL.ID

        return task_ids[1:]

    def get_dag(self):
        return self._dag
