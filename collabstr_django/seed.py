import os
import django


def load_fixtures(*fixture_files):
    """
    Load the given fixture files using Django's loaddata command.
    """
    # Set up Django environment
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "collabstr_django.settings")
    django.setup()

    # Import the management call command
    from django.core.management import call_command

    # Load each fixture file
    for fixture_file in fixture_files:
        call_command("loaddata", fixture_file)


if __name__ == "__main__":
    # List of your fixture files
    fixtures = [
        "creators/fixtures/creator_fixtures.json",
        "creators/fixtures/content_fixtures.json",
        # Add more fixture files here as needed
    ]

    load_fixtures(*fixtures)
