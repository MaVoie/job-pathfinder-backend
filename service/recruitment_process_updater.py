from typing import List


class RecruitmentProcessUpdater:
    recruitment_process = {}

    @classmethod
    def update_recruitment_process_positions(cls, process_id: str, selected_positions: List[str]):
        cls.recruitment_process[process_id] = selected_positions
        return cls.recruitment_process[process_id]
