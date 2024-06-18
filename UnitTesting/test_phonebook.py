import unittest



class PhoneBookTest(unittest.TestCase):

    def test_lookup_by_name(self):
        phonebook = PhoneBook()
        phonebook.add("Karim", "12345")
        number = phonebook.lookup("Karim")
        self.assertEqual("12345", number)