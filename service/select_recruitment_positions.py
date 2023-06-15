from typing import List
from uuid import UUID

from service.gpt_service import GptService
from repository.process_repository import get_by_id, save as save_process
from repository.user_repository import get_by_id as get_user_by_id
from service.recruitment_process_updater import RecruitmentProcessUpdater


class SelectRecruitmentPositions:
    recruitment_process_updater = RecruitmentProcessUpdater()
    gpt_service = GptService()

    @classmethod
    def select_recruitment_process_positions(cls, process_id: UUID, selected_position: str):
        cls.recruitment_process_updater.update_recruitment_process_position(process_id, selected_position)
        process = get_by_id(process_id)
        user = get_user_by_id(process.userId)
        cover_letters = cls.gpt_service.generate_cover_letter(process, user)
        process.covered_letters = cover_letters
        save_process(process)
        return cover_letters

