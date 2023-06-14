from typing import List
from uuid import UUID

from repository.process_repository import get_by_id
from repository.process_repository import save


class RecruitmentProcessUpdater:
    recruitment_process = {}

    @classmethod
    def update_recruitment_process_position(cls, process_id: UUID, selected_position: str):
        process = get_by_id(process_id)
        process.selected_position = selected_position
        save(process)