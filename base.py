import unittest


class OkrTest(unittest.TestCase):
	@classmethod
	def setUp(cls):
		cls.driver = webdriver.Chrome()
		cls.driver.maximize_window()
		cls.driver.implicitly_wait(5)
		cls.base_url = "http://10.202.202.94:28080"
		cls.verificationErrors = []
		cls.accept_next_alert = True

	@classmethod
	def tearDown(cls):
		cls.driver.quit()
		cls.assertEqual([], cls.verificationErrors)