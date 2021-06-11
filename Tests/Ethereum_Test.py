import unittest, Ethereum

class TestStringMethods(unittest.TestCase):


  def test_check(self):
      self.assertEqual(Ethereum.check('asdasd'), 'Помилка, не правильно введено адресу')
      self.assertEqual(Ethereum.check('0xb804b8a18C3F2ee4e3E4E96E6d3f3dc488c0A663'.lower()), '0xb804b8a18C3F2ee4e3E4E96E6d3f3dc488c0A663')

  @unittest.expectedFailure
  def test_check_fail(self):
      self.assertEqual(Ethereum.check('asdasd'), '0xb804b8a18C3F2ee4e3E4E96E6d3f3dc488c0A663')

  # def test_isupper(self):
  #     self.assertTrue('FOO'.isupper())
  #     self.assertFalse('Foo'.isupper())


  @unittest.expectedFailure
  def test_info(self):
      self.assertEqual(Ethereum.get_info({'user_address':'asd'}, '0xab0846e1300268Cd2D84A87790f68913e83e13e6'), ['hello', 'world'])

  @unittest.expectedFailure
  def test_info_fail(self):
      self.assertIsNotNone(Ethereum.get_info('0xab0846e1300268Cd2D84A87790f68913e83e13e6'))


  def test_info_fail(self):
      self.assertIsNotNone(Ethereum.get_info(None, '0xab0846e1300268Cd2D84A87790f68913e83e13e6'))



  def test_event_succ(self):
      self.assertIsNotNone(Ethereum.auction_event('0xab0846e1300268Cd2D84A87790f68913e83e13e6',123))

  @unittest.expectedFailure
  def test_event_fail(self):
      self.assertIsNotNone(Ethereum.auction_event('sdf',123))



if __name__ == '__main__':
    unittest.main()
