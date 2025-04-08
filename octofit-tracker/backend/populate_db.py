import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'octofit_tracker.settings')
django.setup()

from octofit_app.models import User, Team, Activity, Leaderboard, Workout

# Clear existing data
User.objects.all().delete()
Team.objects.all().delete()
Activity.objects.all().delete()
Leaderboard.objects.all().delete()
Workout.objects.all().delete()

# Add test data
# Create users
user1 = User.objects.create(username='john_doe', email='john@example.com')
user2 = User.objects.create(username='jane_doe', email='jane@example.com')

# Create teams
team1 = Team.objects.create(name='Team Alpha')
team2 = Team.objects.create(name='Team Beta')

# Assign users to teams
team1.members.add(user1)
team2.members.add(user2)

# Create activities
activity1 = Activity.objects.create(name='Running', description='Morning run in the park')
activity2 = Activity.objects.create(name='Cycling', description='Evening cycling session')

# Create workouts
workout1 = Workout.objects.create(user=user1, activity=activity1, duration=30, calories_burned=300)
workout2 = Workout.objects.create(user=user2, activity=activity2, duration=45, calories_burned=450)

# Create leaderboard entries
Leaderboard.objects.create(user=user1, points=100)
Leaderboard.objects.create(user=user2, points=150)

print("Test data added successfully!")

# Add test data to the database
def populate():
    User.objects.create(username="testuser1", email="test1@example.com", password="password123")
    User.objects.create(username="testuser2", email="test2@example.com", password="password123")
    print("Test data added successfully.")

if __name__ == "__main__":
    populate()
