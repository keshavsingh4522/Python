import unittest
import demographic_data_analyzer

class DemographicAnalyzerTestCase(unittest.TestCase):
    def setUp(self):
        self.data = demographic_data_analyzer.calculate_demographic_data(print_data = False)

    def test_race_count(self):
        actual = self.data['race_count'].tolist()
        expected = [27816, 3124, 1039, 311, 271]
        self.assertAlmostEqual(actual, expected, msg="Expected race count values to be [27816, 3124, 1039, 311, 271]")
    
    def test_average_age_men(self):
        actual = self.data['average_age_men']
        expected = 39.4
        self.assertAlmostEqual(actual, expected, msg="Expected different value for average age of men.")

    def test_percentage_bachelors(self):
        actual = self.data['percentage_bachelors']
        expected = 16.4 
        self.assertAlmostEqual(actual, expected, msg="Expected different value for percentage with Bachelors degrees.")

    def test_higher_education_rich(self):
        actual = self.data['higher_education_rich']
        expected = 46.5
        self.assertAlmostEqual(actual, expected, msg="Expected different value for percentage with higher education that earn >50K.")
  
    def test_lower_education_rich(self):
        actual = self.data['lower_education_rich']
        expected = 17.4
        self.assertAlmostEqual(actual, expected, msg="Expected different value for percentage without higher education that earn >50K.")

    def test_min_work_hours(self):
        actual = self.data['min_work_hours']
        expected = 1
        self.assertAlmostEqual(actual, expected, msg="Expected different value for minimum work hours.")     

    def test_rich_percentage(self):
        actual = self.data['rich_percentage']
        expected = 10
        self.assertAlmostEqual(actual, expected, msg="Expected different value for percentage of rich among those who work fewest hours.")   

    def test_highest_earning_country(self):
        actual = self.data['highest_earning_country']
        expected = 'Iran'
        self.assertEqual(actual, expected, "Expected different value for highest earning country.")   

    def test_highest_earning_country_percentage(self):
        actual = self.data['highest_earning_country_percentage']
        expected = 41.9
        self.assertAlmostEqual(actual, expected, msg="Expected different value for highest earning country percentage.")   

    def test_top_IN_occupation(self):
        actual = self.data['top_IN_occupation']
        expected = 'Prof-specialty'
        self.assertEqual(actual, expected, "Expected different value for top occupations in India.")      

if __name__ == "__main__":
    unittest.main()
