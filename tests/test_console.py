import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand

class TestHBNBCommand(unittest.TestCase):
    def setUp(self):
        self.hbnb_cmd = HBNBCommand()
        self.hbnb_cmd.stdout = StringIO()

    def tearDown(self):
        self.hbnb_cmd.stdout.close()

    @patch('sys.stdout', new_callable=StringIO)
    def assert_output(self, expected_output, mock_stdout):
        self.hbnb_cmd.cmdqueue.append(expected_output)
        self.hbnb_cmd.cmdloop()
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    def test_quit_command(self):
        self.assertTrue(self.hbnb_cmd.onecmd('quit'))

    def test_create_command(self):
        self.assert_output("** class name missing **", 'create')

    def test_show_command(self):
        self.assert_output("** class name missing **", 'show')
        self.assert_output("** instance id missing **", 'show BaseModel')

    def test_destroy_command(self):
        self.assert_output("** class name missing **", 'destroy')
        self.assert_output("** instance id missing **", 'destroy BaseModel')

    def test_all_command(self):
        self.assert_output("['{}']".format(str(models.storage.all())), 'all')
        self.assert_output("** class doesn't exist **", 'all InvalidClass')

    def test_update_command(self):
        self.assert_output("** class name missing **", 'update')
        self.assert_output("** instance id missing **", 'update BaseModel')
        self.assert_output("** attribute name missing **", 'update BaseModel 123')
        self.assert_output("** value missing **", 'update BaseModel 123 attribute_name')

if __name__ == '__main__':
    unittest.main()
