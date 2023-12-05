import json

import pytest

from src.channel import Channel


class TestChannel:
    @pytest.fixture
    def channel(self):
        return Channel("UC-OVMPlMA3-YCIeg4z5z23A")

    def test_channel_info(self, channel):
        assert channel.title == "MoscowPython"
        assert channel.description == """Видеозаписи со встреч питонистов и джангистов в Москве и не только. :)
Присоединяйтесь: https://www.facebook.com/groups/MoscowDjango! :)"""
        assert channel.url == "https://www.youtube.com/channel/UC-OVMPlMA3-YCIeg4z5z23A"
        assert channel.subscriberCount == "26800"
        assert channel.video_count == "726"
        assert channel.viewCount == "2472920"


def load_json_file(file_path):
    with open(file_path) as f:
        data = json.load(f)
    return data


@pytest.fixture
def json_data():
    file_path = "../homework-2/moscowpython.json"
    return load_json_file(file_path)


def test_json_data(json_data):
    assert "_Channel__channel_id" in json_data
    assert "title" in json_data
    assert json_data["_Channel__channel_id"] == "UC-OVMPlMA3-YCIeg4z5z23A"
    assert json_data["title"] == "MoscowPython"
