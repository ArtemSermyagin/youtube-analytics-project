import os
from typing import Any

import dotenv
from googleapiclient.discovery import build

dotenv.load_dotenv()


class Video:
    api_key: str | None = os.environ.get("YT_API_KEY")

    def __init__(self, video_id: str):
        self.video_id = video_id  # - id видео
        self.video_title = self.data_videos()["items"][0]["snippet"][
            "title"
        ]  # - название видео
        self.video_url = "https://youtu.be/" + self.video_id  # - ссылка на видео
        self.view_count = self.data_videos()["items"][0]["statistics"][
            "viewCount"
        ]  # - количество просмотров
        self.like_count = self.data_videos()["items"][0]["statistics"][
            "likeCount"
        ]  # - количество лайков

    @classmethod
    def get_service(cls) -> Any:
        return build("youtube", "v3", developerKey=cls.api_key)

    def data_videos(self) -> dict:
        video_response = (
            self.get_service()
            .videos()
            .list(
                part="snippet,statistics,contentDetails,topicDetails", id=self.video_id
            )
            .execute()
        )
        return video_response

    def __str__(self) -> str:
        return self.video_title


class PLVideo(Video):
    """Класс PLVideo из ютуб-канала"""

    def __init__(self, video_id: str, playlist_id: str):
        super().__init__(video_id)
        self.playlist_id = playlist_id

