from typing import List

from service.gpt_service import GptService
from service.recruitment_process_reader import RecruitmentProcessReader
from service.recruitment_process_updater import RecruitmentProcessUpdater


class SelectRecruitmentPositions:
    recruitment_process_updater = RecruitmentProcessUpdater()
    recruitment_process_reader = RecruitmentProcessReader()
    gpt_service = GptService()

    @classmethod
    def select_recruitment_process_positions(cls, process_id: str, selected_positions: List[str]):
        positions = cls.recruitment_process_updater.update_recruitment_process_positions(process_id, selected_positions)
        process = cls.recruitment_process_reader.get_recruitment_process()
        process.selected_positions = positions
        return cls.gpt_service.generate_cover_letter(process)

