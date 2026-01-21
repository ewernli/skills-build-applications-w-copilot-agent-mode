from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models
from octofit_tracker import models as app_models

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete existing data
        User = get_user_model()
        User.objects.all().delete()
        app_models.Team.objects.all().delete()
        app_models.Activity.objects.all().delete()
        app_models.Leaderboard.objects.all().delete()
        app_models.Workout.objects.all().delete()

        # Create Teams
        marvel = app_models.Team.objects.create(name='Marvel')
        dc = app_models.Team.objects.create(name='DC')

        # Create Users (super heroes)
        ironman = User.objects.create_user(username='ironman', email='ironman@marvel.com', password='password', team=marvel)
        spiderman = User.objects.create_user(username='spiderman', email='spiderman@marvel.com', password='password', team=marvel)
        batman = User.objects.create_user(username='batman', email='batman@dc.com', password='password', team=dc)
        superman = User.objects.create_user(username='superman', email='superman@dc.com', password='password', team=dc)

        # Create Activities
        app_models.Activity.objects.create(user=ironman, type='run', duration=30, distance=5)
        app_models.Activity.objects.create(user=spiderman, type='cycle', duration=45, distance=20)
        app_models.Activity.objects.create(user=batman, type='swim', duration=60, distance=2)
        app_models.Activity.objects.create(user=superman, type='run', duration=50, distance=10)

        # Create Workouts
        app_models.Workout.objects.create(user=ironman, name='Chest Day', description='Bench press and push-ups')
        app_models.Workout.objects.create(user=batman, name='Leg Day', description='Squats and lunges')

        # Create Leaderboard
        app_models.Leaderboard.objects.create(user=ironman, points=100)
        app_models.Leaderboard.objects.create(user=spiderman, points=80)
        app_models.Leaderboard.objects.create(user=batman, points=90)
        app_models.Leaderboard.objects.create(user=superman, points=95)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
