from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelTestCase(TestCase):
    def setUp(self):
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')
        user1 = User.objects.create_user(username='ironman', email='ironman@marvel.com', team=marvel)
        user2 = User.objects.create_user(username='batman', email='batman@dc.com', team=dc)
        Activity.objects.create(user=user1, type='run', duration=30, distance=5)
        Workout.objects.create(name='Morning Cardio', description='Cardio for all heroes')
        Leaderboard.objects.create(team=marvel, points=100)

    def test_team_count(self):
        self.assertEqual(Team.objects.count(), 2)
    def test_user_count(self):
        self.assertEqual(User.objects.count(), 2)
    def test_activity_count(self):
        self.assertEqual(Activity.objects.count(), 1)
    def test_workout_count(self):
        self.assertEqual(Workout.objects.count(), 1)
    def test_leaderboard_count(self):
        self.assertEqual(Leaderboard.objects.count(), 1)
