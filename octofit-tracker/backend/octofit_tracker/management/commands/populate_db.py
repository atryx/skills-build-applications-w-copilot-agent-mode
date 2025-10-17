from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from djongo import models

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users
        users = [
            User.objects.create(email='ironman@marvel.com', name='Iron Man', team='Marvel'),
            User.objects.create(email='captain@marvel.com', name='Captain America', team='Marvel'),
            User.objects.create(email='batman@dc.com', name='Batman', team='DC'),
            User.objects.create(email='wonderwoman@dc.com', name='Wonder Woman', team='DC'),
        ]

        # Create activities
        Activity.objects.create(user='Iron Man', type='Running', duration=30)
        Activity.objects.create(user='Captain America', type='Cycling', duration=45)
        Activity.objects.create(user='Batman', type='Swimming', duration=25)
        Activity.objects.create(user='Wonder Woman', type='Yoga', duration=40)

        # Create leaderboard
        Leaderboard.objects.create(team='Marvel', points=75)
        Leaderboard.objects.create(team='DC', points=65)

        # Create workouts
        Workout.objects.create(name='Super Strength', difficulty='Hard')
        Workout.objects.create(name='Agility Training', difficulty='Medium')
        Workout.objects.create(name='Mindfulness', difficulty='Easy')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
