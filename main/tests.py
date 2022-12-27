from datetime import timedelta

from django.test import TestCase
from django.utils import timezone

from .forms import TalkForm
from .models import Talk

class TestTalkModel(TestCase):  # TestCase を継承するのを忘れないように。
    @classmethod
    def setUpClass(cls):
        # Talk モデルのテストで使用する変数の初期化をしています。
        super().setUpClass()
        now = timezone.now()
        cls._talk_30minutes_ago = Talk(time=now - timedelta(minutes=30))
        cls._talk_3hours_ago = Talk(time=now - timedelta(hours=3))
        cls._talk_3days_ago = Talk(time=now - timedelta(days=3))
        cls._talk_9days_ago = Talk(time=now - timedelta(days=9))
        cls._talk_3weeks_ago = Talk(time=now - timedelta(weeks=3))
        cls._talk_future = Talk(time=now + timedelta(weeks=3))

    def test_valid_elapsed_time(self):
        self.assertEqual(self._talk_30minutes_ago.get_elapsed_time(), "30 分前")
        self.assertEqual(self._talk_3hours_ago.get_elapsed_time(), "3 時間前")
        self.assertEqual(self._talk_3days_ago.get_elapsed_time(), "3 日前")
        self.assertEqual(self._talk_9days_ago.get_elapsed_time(), "1 週間以上前")
        self.assertEqual(self._talk_3weeks_ago.get_elapsed_time(), "1 週間以上前")

    def test_invalid_elapsed_time(self):
        with self.assertRaises(ValueError):
            self._talk_future.get_elapsed_time()