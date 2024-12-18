import click
from sqlalchemy.orm import Session
from app.database import Session, init_db
from app.models import User, Workout, Exercise

init_db()

@click.group()
def cli():
    """Workout Planner CLI"""
    pass

@cli.command()
@click.argument('name')
def add_user(name):
    """Add a new user."""
    session = Session()
    user = User(name=name)
    session.add(user)
    session.commit()
    click.echo(f"User '{name}' added successfully!")
    session.close()

@cli.command()
@click.argument('user_id')
@click.argument('workout_name')
def add_workout(user_id, workout_name):
    """Add a workout."""
    session = Session()
    user = session.get(User, user_id)
    if user:
        workout = Workout(name=workout_name, user=user)
        session.add(workout)
        session.commit()
        click.echo(f"Workout '{workout_name}' added for user '{user.name}'.")
    else:
        click.echo("User not found.")
    session.close()

@cli.command()
@click.argument('workout_id')
@click.argument('exercise_name')
@click.argument('repetitions', type=int)
def add_exercise(workout_id, exercise_name, repetitions):
    """Add an exercise."""
    session = Session()
    workout = session.get(Workout, workout_id)
    if workout:
        exercise = Exercise(name=exercise_name, repetitions=repetitions, workout=workout)
        session.add(exercise)
        session.commit()
        click.echo(f"Exercise '{exercise_name}' added to workout '{workout.name}'.")
    else:
        click.echo("Workout not found.")
    session.close()

@cli.command()
def list_users():
    """List all users."""
    session = Session()
    users = session.query(User).all()
    for user in users:
        click.echo(f"ID: {user.id}, Name: {user.name}")
    session.close()

@cli.command()
def list_workouts():
    """List all workouts."""
    session = Session()
    workouts = session.query(Workout).all()
    for workout in workouts:
        click.echo(f"Workout: {workout.name}, User: {workout.user.name}")
    session.close()
