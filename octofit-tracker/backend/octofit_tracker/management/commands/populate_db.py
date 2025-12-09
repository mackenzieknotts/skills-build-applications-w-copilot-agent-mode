from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.db import connection

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

        # Create users (super heroes)
        users = [
            User(email='tony@marvel.com', name='Tony Stark', team='Marvel'),
            User(email='steve@marvel.com', name='Steve Rogers', team='Marvel'),
            User(email='bruce@dc.com', name='Bruce Wayne', team='DC'),
            User(email='clark@dc.com', name='Clark Kent', team='DC'),
        ]
        User.objects.bulk_create(users)

        # Create activities
        activities = [
            Activity(user='Tony Stark', type='Running', duration=30),
            Activity(user='Steve Rogers', type='Cycling', duration=45),
            Activity(user='Bruce Wayne', type='Swimming', duration=60),
            Activity(user='Clark Kent', type='Flying', duration=120),
        ]
        Activity.objects.bulk_create(activities)

        # Create leaderboard
        Leaderboard.objects.create(team='Marvel', points=75)
        Leaderboard.objects.create(team='DC', points=180)

        # Create workouts
        workouts = [
            Workout(name='Pushups', difficulty='Easy'),
            Workout(name='Pullups', difficulty='Medium'),
            Workout(name='Squats', difficulty='Hard'),
        ]
        Workout.objects.bulk_create(workouts)


        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data'))
