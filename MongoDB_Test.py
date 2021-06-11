import unittest, MongoDB

class TestStringMethods(unittest.TestCase):


  def test_buyer(self):
      self.assertEqual(MongoDB.get_buyer('0x4AA93b9fa90a8234e4dDf77C8a9b79F993b3Abf6'), '0x7A02915146f1256a66E2FeD29D15A1e430639a8B')
      self.assertIsNone(MongoDB.get_buyer('asd'))


  def test_selected(self):
      self.assertEqual(MongoDB.get_selected_contract(505423220), 'Не обрано контракт')
      self.assertEqual(MongoDB.get_selected_contract(''), 'Не обрано контракт')


  def test_is_admin(self):
    self.assertFalse(MongoDB.is_admin(1388856541))
    self.assertTrue(MongoDB.is_admin(462535778))
    self.assertFalse(MongoDB.is_admin(0))

  @unittest.expectedFailure
  def test_admin(self):
    self.assertFalse(MongoDB.is_admin(462535778))
    self.assertTrue(MongoDB.is_admin(1388856541))
    self.assertFalse(MongoDB.is_admin(462535778))


if __name__ == '__main__':
    unittest.main()