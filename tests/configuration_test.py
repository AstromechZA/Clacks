import unittest
import os
import tempfile

from clacks import configuration

class ConfigurationTest(unittest.TestCase):

    def build_fake_config(self, **kwargs):
        kwargs['custom_path'] = os.path.join(tempfile.mkdtemp(), '.config', 'clacks', 'settings')
        return configuration.Config(**kwargs)

    def test_cantouch(self):
        self.assert_(configuration.config != None)

    def test_blank_new_config(self):
        c = self.build_fake_config()

        # file should not exist
        self.assert_(not os.path.exists(c.file_path))

        # load
        c.load()

        # config should be blank
        self.assert_(c._config == {})

        # should not be able to load anything
        with self.assertRaises(KeyError):
            c.get('a')

        # save
        c.save()

        # file should exist
        self.assert_(os.path.exists(c.file_path))

    def test_save_before_load(self):
        c = self.build_fake_config()
        with self.assertRaises(RuntimeError):
            c.save()

    def test_double_load(self):
        c = self.build_fake_config(auto_load=True)
        with self.assertRaises(RuntimeError):
            c.load()

    def test_get_and_set(self):
        # create fake config
        c = self.build_fake_config(auto_load=True)

        # test that set and get work
        c.set('a', 'hello')
        self.assert_(c.get('a') == 'hello')
        self.assert_(c._config == {'a':'hello'})

        # save
        c.save()

        # open new config with same file
        c2 = configuration.Config(custom_path=c.file_path, auto_load=True)

        # check that contents are the same
        self.assert_(c.get('a') == 'hello')

    def test_bad_key(self):
        # create fake config
        c = self.build_fake_config(auto_load=True)

        c.get('lolwhut')


if __name__ == "__main__":
    unittest.main()
