from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelSmokeTest(TestCase):
    def test_team_create(self):
        team = Team.objects.create(name='Test Team', universe='Test')
        self.assertEqual(str(team), 'Test Team')
    def test_user_create(self):
        team = Team.objects.create(name='Test Team2', universe='Test')
        user = User.objects.create(email='test@example.com', name='Test User', team=team)
        self.assertEqual(str(user), 'Test User')
    def test_activity_create(self):
        team = Team.objects.create(name='Test Team3', universe='Test')
        user = User.objects.create(email='test2@example.com', name='Test User2', team=team)
        activity = Activity.objects.create(user=user, activity_type='Test', duration_minutes=10, date='2024-01-01')
        self.assertEqual(str(activity), 'Test User2 - Test')
    def test_workout_create(self):
        workout = Workout.objects.create(name='Test Workout', description='desc', suggested_for='strength')
        self.assertEqual(str(workout), 'Test Workout')
    def test_leaderboard_create(self):
        team = Team.objects.create(name='Test Team4', universe='Test')
        user = User.objects.create(email='test3@example.com', name='Test User3', team=team)
        lb = Leaderboard.objects.create(user=user, score=10, rank=1)
        self.assertEqual(str(lb), 'Test User3 - Rank 1')
