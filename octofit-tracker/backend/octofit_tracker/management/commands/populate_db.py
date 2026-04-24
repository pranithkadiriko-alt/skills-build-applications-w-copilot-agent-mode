from django.core.management.base import BaseCommand
from octofit_tracker.models import Team, User, Activity, Workout, Leaderboard
from django.utils import timezone
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Connect to MongoDB directly for index creation
        client = MongoClient('mongodb://localhost:27017')
        db = client['octofit_db']
        db.users.create_index('email', unique=True)

        # Clear existing data
        Leaderboard.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='Team Marvel', universe='Marvel')
        dc = Team.objects.create(name='Team DC', universe='DC')

        # Users (superheroes)
        users = [
            User.objects.create(email='tony@marvel.com', name='Iron Man', team=marvel),
            User.objects.create(email='steve@marvel.com', name='Captain America', team=marvel),
            User.objects.create(email='bruce@marvel.com', name='Hulk', team=marvel),
            User.objects.create(email='clark@dc.com', name='Superman', team=dc),
            User.objects.create(email='bruce@dc.com', name='Batman', team=dc),
            User.objects.create(email='diana@dc.com', name='Wonder Woman', team=dc),
        ]

        # Workouts
        workouts = [
            Workout.objects.create(name='Strength Training', description='Build muscle and power.', suggested_for='strength'),
            Workout.objects.create(name='Endurance Run', description='Improve stamina and endurance.', suggested_for='endurance'),
        ]

        # Activities
        Activity.objects.create(user=users[0], activity_type='Flight', duration_minutes=30, date=timezone.now().date())
        Activity.objects.create(user=users[1], activity_type='Shield Practice', duration_minutes=45, date=timezone.now().date())
        Activity.objects.create(user=users[3], activity_type='Laser Vision', duration_minutes=20, date=timezone.now().date())

        # Leaderboard
        Leaderboard.objects.create(user=users[0], score=100, rank=1)
        Leaderboard.objects.create(user=users[3], score=90, rank=2)
        Leaderboard.objects.create(user=users[4], score=80, rank=3)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
