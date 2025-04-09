import pymongo
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Populate the MongoDB database with test data'

    def handle(self, *args, **kwargs):
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["octofit_db"]

        # Populate users collection
        users = db["users"]
        users.insert_many([
            {"email": "john.doe@example.com", "name": "John Doe", "age": 25},
            {"email": "jane.smith@example.com", "name": "Jane Smith", "age": 30}
        ])

        # Populate teams collection
        teams = db["teams"]
        teams.insert_one({"name": "Team Alpha", "members": ["john.doe@example.com", "jane.smith@example.com"]})

        # Populate activities collection
        activities = db["activities"]
        activities.insert_many([
            {"user": "john.doe@example.com", "activity_type": "Running", "duration": 30, "date": "2025-04-01"},
            {"user": "jane.smith@example.com", "activity_type": "Cycling", "duration": 45, "date": "2025-04-02"}
        ])

        # Populate leaderboard collection
        leaderboard = db["leaderboard"]
        leaderboard.insert_many([
            {"user": "john.doe@example.com", "points": 100},
            {"user": "jane.smith@example.com", "points": 150}
        ])

        # Populate workouts collection
        workouts = db["workouts"]
        workouts.insert_many([
            {"name": "Morning Yoga", "description": "A relaxing yoga session", "duration": 60},
            {"name": "HIIT", "description": "High-intensity interval training", "duration": 30}
        ])

        self.stdout.write(self.style.SUCCESS('Database populated with test data'))
