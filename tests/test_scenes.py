import os
import json
import unittest

from config import basedir
from storage_api import app, db


class StorageAPIScenesTestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'test.db')
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_newScene(self):
        resp = self.app.post('/scenes', data={'scene_id': 'LC81110562015326LGN00', 'bundle_size': 724500})
        self.assertEqual(resp.status_code, 200)

    def test_newSceneDuplicate(self):
        resp = self.app.post('/scenes', data={'scene_id': 'LC81110562015326LGN00', 'bundle_size': 724500})
        resp = self.app.post('/scenes', data={'scene_id': 'LC81110562015326LGN00', 'bundle_size': 724500})
        self.assertEqual(resp.status_code, 409)

    def test_newSceneIdIsRequired(self):
        resp = self.app.post('/scenes', data={'bundle_size': 724500})
        self.assertEqual(resp.status_code, 422)

    def test_newSceneBundleSizeIsRequired(self):
        resp = self.app.post('/scenes', data={'scene_id': 'LC81110562015326LGN00'})
        self.assertEqual(resp.status_code, 422)

    def test_getScenesEmpty(self):
        resp = self.app.get('/scenes')
        self.assertListEqual(json.loads(resp.data), [])

    def test_getScenes(self):
        resp = self.app.post('/scenes', data={'scene_id': 'LC81110562015326LGN00', 'bundle_size': 724500})
        resp = self.app.get('/scenes')
        self.assertListEqual(json.loads(resp.data), [{
            'scene_id': 'LC81110562015326LGN00',
            'bundle_size': 724500,
            'bundle_url': None,
            'bundle_hash': None}])

    def test_getScenesMustNotSaveDuplicates(self):
        self.app.post('/scenes', data={'scene_id': 'LC81110562015326LGN00', 'bundle_size': 724500})
        self.app.post('/scenes', data={'scene_id': 'LC81110562015326LGN00', 'bundle_size': 724500})

        resp = self.app.get('/scenes')
        self.assertListEqual(json.loads(resp.data), [{
            'scene_id': 'LC81110562015326LGN00',
            'bundle_size': 724500,
            'bundle_url': None,
            'bundle_hash': None}])

    def test_getScene(self):
        self.app.post('/scenes', data={'scene_id': 'LC81110562015326LGN00', 'bundle_size': 724500})

        resp = self.app.get('/scenes/LC81110562015326LGN00')
        self.assertEqual(resp.status_code, 200)
        self.assertDictEqual(json.loads(resp.data), {
            'scene_id': 'LC81110562015326LGN00',
            'bundle_size': 724500,
            'bundle_url': None,
            'bundle_hash': None})

    def test_getSceneDoesNotExist(self):
        resp = self.app.get('/scenes/LC81110562015326LGN01')
        self.assertEqual(resp.status_code, 404)

if __name__ == '__main__':
    unittest.main()
