import unittest
from notifier import app
import json

class NotifierTest(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()
    
    def test_unknown_service(self):
        rv = self.app.post('/notify/facebook', data=json.dumps(dict(to='rob@robspencer.me.uk', body= 'foo')), content_type="application/json")
        self.assertEqual(rv.status_code, 404)

    def test_invalid_content_type(self):
        rv = self.app.post('/notify/twitter', data=dict(to='rob@robspencer.me.uk', body= 'foo'))
        self.assertEqual(rv.status_code, 400)
    
    def test_missing_to_parameter(self):
        rv = self.app.post('/notify/twitter', data=json.dumps(dict(body='foo')), content_type="application/json")
        self.assertEqual(rv.status_code, 400)

    def test_missing_body_parameter(self):
        rv = self.app.post('/notify/twitter', data=json.dumps(dict(to='rob@robspencer.me.uk')), content_type="application/json")
        self.assertEqual(rv.status_code, 400)

    def test_bad_method(self):
        rv = self.app.get('/notify/twitter', content_type="application/json")
        self.assertEqual(rv.status_code, 405)

    def test_sms(self):
        rv = self.app.post('/notify/sms', data=json.dumps(dict(to='07972058628', body='unit test')), content_type="application/json")
        self.assertEqual(rv.status_code, 200)
        self.assertEqual(rv.data, '"OK"\n')

if __name__ == '__main__':
    unittest.main()
