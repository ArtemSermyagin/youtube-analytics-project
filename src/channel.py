import os

import dotenv

from googleapiclient.discovery import build


dotenv.load_dotenv()

api_key = os.environ.get('YT_API_KEY')


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала.
        Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        # print(self.channel_id)
        youtube = build("youtube", "v3", developerKey=api_key)
        channel = (
            youtube.channels()
            .list(id=self.channel_id, part="snippet,statistics")
            .execute()
        )
        print(channel)
