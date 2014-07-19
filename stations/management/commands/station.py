from optparse import make_option
from django.core.management.base import BaseCommand, CommandError
from django.contrib.gis.geos import Point

from snowlert.lib import noaa
from stations.models import Station

class Command(BaseCommand):
    help='Helper tool for stations data'
    option_list = BaseCommand.option_list + (
        make_option('--delete',
            action='store_true',
            dest='delete',
            default=False,
            help='Delete the stations before action'),
        )

    def handle(self, *args, **options):

        if args:
            if options['delete']:
                self.stdout.write('deleting stations...')
                Station.objects.all().delete()
            if args[0] == 'import':
                self.stdout.write("downloading stations...")
                stations_dicts = noaa.get_stations()

                stations = []
                for s in stations_dicts: 
                    station = Station.objects.create(data=s, station_source=Station.NOAA)
                    station.location = Point(float(station.data['latitude']), float(station.data['longitude']),srid=4326) 
                    station.save()
                self.stdout.write("complete.")

            elif args[0] == 'count':
                pass
            else:
                raise CommandError("station command: %s does not exist." % args[0])

        else:
            raise CommandError("No command passed. Accepted values: import, count")
