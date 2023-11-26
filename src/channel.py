import json
import os
from googleapiclient.discovery import build
import dotenv

dotenv.load_dotenv()


class Channel:
    """Класс для ютуб-канала"""

    api_key: str = os.environ.get("YT_API_KEY")

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
