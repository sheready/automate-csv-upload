import csv

from django.core.management import BaseCommand
from django.utils import timezone

from load_csv.models import Movies

#create a django-admin command to extract csv content
#https://docs.djangoproject.com/en/4.0/howto/custom-management-commands/
#https://betterprogramming.pub/3-techniques-for-importing-large-csv-files-into-a-django-app-2b6e5e47dba0

class Command(BaseCommand):
    help = "Loads Netflix movies and TV shows information"

    #Entry point to add parser arguments to handle command line arguments passed to the command
    def add_arguments(self, parser):
        #positional arguments
        parser.add_argument("file_path", type=str)

    def handle(self, *args, **options):
        start_time = timezone.now()
        print(f"I am creating the database now:{start_time}")
        file_path = options["file_path"]
        with open(file_path, "r") as csv_file:
            #reads the content of the csv file 
            data = csv.reader(csv_file, delimiter = ",")
            #excludes the headers i.e the first row
            next(data)
            for row in data:
                created_movie, created = Movies.objects.update_or_create(
                    show_id = row[0],
                    type=row[1],
                    title=row[2],
                    director=row[3],
                    cast=row[4],
                    release_year=row[7],
                    defaults = {
                        'show_id':row[0],
                        'type': row[1],
                        'title':row[2],
                        'director':row[3],
                        'cast':row[4],
                        'release_year':row[7],
                    },
                )
                
        end_time = timezone.now()
       
        print(f"loading CSV file took: {( end_time-start_time).total_seconds()} seconds")    

                
