import unittest
import os
from models.base_model import BaseModel
from models.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):

    def setUp(self):
        self.file_path = "file_test.json"
        self.file_storage = FileStorage._FileStorage__file_path  # Save the original file path
        FileStorage._FileStorage__file_path = self.file_path  # Set a temporary file path for testing

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
        FileStorage._FileStorage__file_path = self.file_storage  # Restore the original file path

    def test_all(self):
        file_storage = FileStorage()
        all_objects = file_storage.all()
        self.assertIsInstance(all_objects, dict)
        self.assertEqual(all_objects, {})

    def test_new(self):
        file_storage = FileStorage()
        model = BaseModel()
        file_storage.new(model)
        all_objects = file_storage.all()
        key = "{}.{}".format(model.__class__.__name__, model.id)
        self.assertIn(key, all_objects)
        self.assertEqual(all_objects[key], model)

    def test_save_and_reload(self):
        file_storage = FileStorage()
        model = BaseModel()
        file_storage.new(model)
        file_storage.save()

        # Create a new FileStorage instance to reload
        new_file_storage = FileStorage()
        new_file_storage.reload()

        all_objects_after_reload = new_file_storage.all()
        key = "{}.{}".format(model.__class__.__name__, model.id)

        self.assertIn(key, all_objects_after_reload)
        reloaded_model = all_objects_after_reload[key]
        self.assertIsInstance(reloaded_model, BaseModel)
        self.assertEqual(reloaded_model.id, model.id)
        self.assertEqual(reloaded_model.created_at, model.created_at)
        self.assertEqual(reloaded_model.updated_at, model.updated_at)

if __name__ == '__main__':
    unittest.main()
