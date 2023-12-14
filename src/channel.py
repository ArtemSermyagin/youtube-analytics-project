import json
import os

import dotenv
from googleapiclient.discovery import build  # type: ignore

dotenv.load_dotenv()


class Channel:
    """Класс для ютуб-канала"""

    api_key: str | None = os.environ.get("YT_API_KEY")

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        channel = (
            self.get_service()
            .channels()
            .list(id=self.__channel_id, part="snippet,statistics")
            .execute()
        )
        # print(channel)
        self.title = channel["items"][0]["snippet"]["title"]
        self.description = channel["items"][0]["snippet"]["description"]
        # print(self.description)
        self.url = "https://www.youtube.com/channel/" + self.__channel_id
        self.subscriberCount = channel["items"][0]["statistics"]["subscriberCount"]
        self.video_count = channel["items"][0]["statistics"]["videoCount"]
        self.viewCount = channel["items"][0]["statistics"]["viewCount"]

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(
            f"""{self.__channel_id} - id канала,
{self.title} - название канала,
{self.description} - описание канала,
{self.url} - ссылка на канал,
{self.subscriberCount} - количество подписчиков,
{self.video_count} - количество видео,
{self.viewCount} - общее количество просмотров"""
        )

    @classmethod
    def get_service(cls):
        return build("youtube", "v3", developerKey=cls.api_key)

    def to_json(self, file_name):
        with open(file_name, "w") as f:
            json.dump(self.__dict__, f, indent=4, ensure_ascii=False)

    def __str__(self) -> str:
        """Возвращает строковое представление канала."""
        return f"{self.title} ({self.url})"

    def __add__(self, other) -> int:
        """Возвращает сумму подписчиков двух каналов."""
        return int(self.subscriberCount) + int(other.subscriberCount)

    def __sub__(self, other) -> int:
        """Возвращает разность подписчиков двух каналов."""
        return int(self.subscriberCount) - int(other.subscriberCount)

    def __lt__(self, other) -> bool:
        """Возвращает True, если количество подписчиков
        текущего канала меньше, чем у другого."""
        return self.subscriberCount < other.subscriberCount

    def __le__(self, other) -> bool:
        """Возвращает True, если количество подписчиков
        текущего канала меньше или равно, чем у другого."""
        return self.subscriberCount <= other.subscriberCount

    def __eq__(self, other) -> bool:
        """Возвращает True, если количество подписчиков
        у двух каналов одинаково."""
        return self.subscriberCount == other.subscriberCount


# video_id = "AWX4JnAnjBE"
# api_key = "AIzaSyAKvaVPp95lAYmDjFfAJWsE0N5SBdrljMk"
#
# youtube = build("youtube", "v3", developerKey=api_key)
#
# video_response = (
#     youtube.videos()
#     .list(part="snippet,statistics,contentDetails,topicDetails", id=video_id)
#     .execute()
# )
# print(video_response)
