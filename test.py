import unittest
from flask import Flask
import app


class TestApp(unittest.TestCase):


    def setUp(self):
        self.app = app.app.test_client()
        self.app.testing = True
    
    def test_search_text(self):
        response = self.app.get('/search?string=Now%20is', content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['query_text'], 'Now is')
        self.assertIsInstance(data['number_of_occurrences'], int)
        self.assertIsInstance(data['occurrences'], list)

    def test_search_text_no_results(self):
        response = self.app.get('/search', content_type='application/json')
        self.assertEqual(response.status_code, 400)


    def test_find_string(self):
        text = "Now is the time\nfor all good men\nto come to the aid\nof their country."

        # test case_1 - single occurrence
        results = app.find_string(text, 'Now is') 
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]['line'], 1)
        self.assertEqual(results[0]['start'], 1)
        self.assertEqual(results[0]['end'], 7)
        self.assertEqual(results[0]['in_sentence'], 'Now is the time for all good men to come to the aid of their country.')
        
        #test case_2 - multiple occurrences
        results_2 = app.find_string(text, 'to')
        self.assertEqual(len(results_2), 2)
        self.assertEqual(results_2[0]['line'], 3)
        self.assertEqual(results_2[0]['start'], 1)
        self.assertEqual(results_2[0]['end'], 3)
        self.assertEqual(results_2[0]['in_sentence'], 'Now is the time for all good men to come to the aid of their country.')
        self.assertEqual(results_2[1]['line'], 3)
        self.assertEqual(results_2[1]['start'], 9)
        self.assertEqual(results_2[1]['end'], 11)
        self.assertEqual(results_2[1]['in_sentence'], 'Now is the time for all good men to come to the aid of their country.')

        #test case_3 - multiple lines
        results_3 = app.find_string(text, 'aid of')
        self.assertEqual(len(results_3), 1)
        self.assertEqual(results_3[0]['line'], 3)
        self.assertEqual(results_3[0]['start'], 16)
        self.assertEqual(results_3[0]['end'], 3)
        self.assertEqual(results_3[0]['in_sentence'], 'Now is the time for all good men to come to the aid of their country.')

        
        text_2 = "Now is the time\nfor all good men\nto come to the aid\nof their country.  Now is the time\nfor all good women\nto come to the aid\nof their country."
        
        #test case_4 - multiple sentences
        results_4 = app.find_string(text_2, 'country.  Now is the time for')
        self.assertEqual(len(results_4), 1)
        self.assertEqual(results_4[0]['line'], 4)
        self.assertEqual(results_4[0]['start'], 10)
        self.assertEqual(results_4[0]['end'], 4)
        self.assertEqual(results_4[0]['in_sentence'], ['Now is the time for all good men to come to the aid of their country.', 'Now is the time for all good women to come to the aid of their country.'])


        #test case_5 - no results
        results_5 = app.find_string(text_2, 'hello')
        self.assertEqual(len(results_5), 0)


        #tet cast6 - mutiple lines 
        result_6 = app.find_string(text, 'men to come to the aid of their country')
        self.assertEqual(len(result_6), 1)
        self.assertEqual(result_6[0]['line'], 2)
        self.assertEqual(result_6[0]['start'], 14)
        self.assertEqual(result_6[0]['end'], 17)
        self.assertEqual(result_6[0]['in_sentence'], 'Now is the time for all good men to come to the aid of their country.')

if __name__=='__main__':
    unittest.main()