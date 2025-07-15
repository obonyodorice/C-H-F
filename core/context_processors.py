# mychurchproject/core/context_processors.py
from django.db.utils import ProgrammingError # Add this import
from ContributionsApp.models import ChurchLogo # Adjust import if model is in another app

def church_logo_processor(request):
    church_logo = None # Initialize to None

    try:
        # Attempt to fetch the active church logo.
        # .first() will return the first object or None if no matching objects.
        church_logo = ChurchLogo.objects.filter(is_active=True).first()
    except ProgrammingError:
        # This occurs if the database table for ChurchLogo does not exist yet.
        # This is common during initial setup before migrations are applied.
        print("Warning: ChurchLogo table does not exist. Run migrations.")
        church_logo = None
    except Exception as e:
        # Catch any other unexpected errors during database access
        print(f"An unexpected error occurred while fetching church logo: {e}")
        church_logo = None
        
    return {'church_logo': church_logo}