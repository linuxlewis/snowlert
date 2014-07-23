from unittest.mock import Mock, patch
from unittest import TestCase

from datetime import datetime, tzinfo

from lxml import etree


class NOAATestCase(TestCase):

    def setUp(self):
        from snowlert.lib import noaa
        # requests patch
        # patch the parse_obs_str method. Mock returns value passed to it
        self.parse_obs_time_str_patch = patch.object(noaa, '_parse_observation_time_string', \
            Mock(side_effect=lambda x: x))

    def test_obs_time_string_success(self):
        from snowlert.lib import noaa

        test_data = 'Last Updated on Jul 5 2014, 4:55 pm PDT'

        expected = datetime(year=2014, month=7, day=5, hour=16, minute=55, tzinfo=tzinfo('PDT')).isoformat()

        actual = noaa._parse_observation_time_string(test_data)

        self.assertEqual(expected, actual)

    def test_obs_time_string_format_success(self):
        assert 0

    def test_obs_time_string_fail(self):
        assert 0

    def test_parse_station(self):
        '''
        This unittest tests if the parse station method maps child.tag to key, value
        and handles the special observation_time case.
        '''
        # make fake xml element
        with self.parse_obs_time_str_patch as p:
            from snowlert.lib import noaa

            fake_xml = '''<fake>
            <observation_time>fake obs data</observation_time>
            <other>1</other>
            <cool>test</cool>
            </fake>
            '''
            fxml = etree.fromstring(fake_xml)

            expected = {'other':'1', 'cool':'test', 'observation_time':'fake obs data'}
            # test the unit
            actual = noaa._parse_station(fxml)
            # check if the data was parsed correctly
            self.assertEqual(actual, expected)
            # check if the special data was handled
            self.assertTrue(p.called_with('fake obs data'))

    def test__get_stations_success(self):
        assert 0

    def test_get_stations(self):
        assert 0


