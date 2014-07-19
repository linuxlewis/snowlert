from unittest.mock import Mock, patch
import io


from django.test import TestCase
from django.core import management
from django.core.management.base import CommandError
# Create your tests here.
from stations.models import Station

class TestStationsCommand(TestCase):

    def setUp(self):
        # create noaa patch
        from snowlert.lib import noaa
        # return data
        self.fake_station = {'latitude':10.0, 'longitude': 9.0, \
        'fake':'data', 'super':'fake'}
        result = [self.fake_station]
        self.noaa_patch = patch.object(noaa, 'get_stations', Mock(return_value=result))

    def test_missing_command_fail(self):
        '''
        This unittest tests if a CommandError is raised
        if the command is passed without an argument.
        '''
        self.assertRaises(CommandError, management.call_command, 'station', stdout=io.StringIO())

    def test_invalid_command_fail(self):
        '''
        This unittest tests if a CommandError is raised
        if an invalid command is passed
        '''
        self.assertRaises(CommandError, management.call_command, 'station', 'foobar', stdout=io.StringIO())

    def test_import_success(self):
        '''
        This unittest tests if Stations are created in the database when
        the import command is called successfully
        '''
        # patch the noaa lib
        with self.noaa_patch:
            # call the command
            management.call_command('station', 'import', stdout=io.StringIO())

            self.assertGreater(Station.objects.all().count(), 0)

    def test_delete_flag_success(self):
        '''
        This unittest tests if Stations are deleted when the --delete flag is
        passed to the command
        '''
        # test specific setup
        s = Station.objects.create(data=self.fake_station)
        s.save()
        # check the setup is legit
        self.assertGreater(Station.objects.all().count(), 0)
        # test the unit
        # the delete should run but the import should fail
        self.assertRaises(CommandError, management.call_command, 'station', 'foobar', delete=True, stdout=io.StringIO())
        # assert the stations were deleted
        self.assertEqual(Station.objects.all().count(), 0)



