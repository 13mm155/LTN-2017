'''
Created on Aug 30, 2017

@author: Hossein
'''
import unittest
from . import main

class TestScrapingMethods(unittest.TestCase):
  '''
  Test the methods used to collect data from the web, save into and load from files. 
  '''
  def test_get_team_members(self):
    team_members = main.get_team_members()
    found_Johanna = False
    for d in team_members: 
      if d['name'] == 'Johanna Nicoletta': 
        found_Johanna = True
    self.assertEqual(found_Johanna, True, "The AJAX call was not successful!")
    
  def test_save_and_load(self):
    team_members = main.get_team_members()
    team_data = {'date': team_members}
    # save data to file 
    data_file_name = '../data/web_data_json_test.data'

    main.save_to_file(data_file_name, team_data)    
    #
    # test loading from the file and if the name of Johanna can be found
    #
    print('loading from the file...')
    member_data = main.load_from_file(data_file_name)
    a_day_data = {}
    # take the first item in the dictionary; doesn'e matter which one it is
    for key in member_data: 
      a_day_data = member_data[key]
      break
    found_Johanna = False
    for d in a_day_data: 
      if d['name'] == 'Johanna Nicoletta': 
        found_Johanna = True
    self.assertEqual(found_Johanna, True, "Can not save or load from file")
    
  def test_update_ledger(self):
    test_ledger = {'20170901': [{'name': 'Johanna', 'amount': '345$'}, {'name':"Hossein", 'amount': '22$'}], 
                   '20170901': [{'name': 'Johanna', 'amount': '355$'}, {'name':"Hossein", 'amount': '23$'}]}
    new_data = [{'name': 'Johanna', 'amount': '355$'}, {'name':"Hossein", 'amount': '23$'}, {'name':"Ron", 'amount': '100$'}]
    main.update_ledger(test_ledger, new_data)
    from time import gmtime, strftime
    today_date = strftime("%Y%m%d", gmtime())
    self.assertEqual(today_date in test_ledger, True, "The data has not been added to the ledger")
    # test updating
    update_data = [{'name': 'Johanna', 'amount': '355$'}, {'name':"Hossein", 'amount': '50$'}]
    main.update_ledger(test_ledger, update_data, '20170901')
    self.assertEqual(test_ledger['20170901'][1]['amount'] == '50$', True, "Ledger is not updated.")
    #
    main.update_ledger(['list', 'of', 'some string'], 'something', '20170901')
    self.assertEqual(test_ledger['20170901'][1]['amount'] == '50$', True, "Ledger is not updated.")






    