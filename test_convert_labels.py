import os
import unittest
import get_labels
import convert_labels


class TestGetLabels(unittest.TestCase):
    def setUp(self):
        pass # Nothing for now

    def tearDown(self):
        pass # Nothing for now

    def test_get_labels(self):
        # To test the convert_labels function using "test_papers_label_conversion.csv" file

        labels = get_labels.get_labels("test_papers_label_conversion.csv")
        function_map = "function_map.csv"

        first_test = convert_labels.convert_labels(function_map, labels[0])
        second_test = convert_labels.convert_labels(function_map, labels[1])
        third_test = convert_labels.convert_labels(function_map, labels[2])

        self.assertEqual(first_test, ["Process resources,Chemically modify","Store resources,Change energy state","Store energy,Modify/convert mechanical energy"])
        self.assertEqual(second_test, ["Attach,Maintain structural integrity","Attach temporarily,Manage structural forces","Manage stress/strain,Manage impact"])
        self.assertEqual(third_test, ["Maintain structural integrity","Manage structural forces,Prevent structural failure","Manage impact,Manage shear,Prevent fracture/rupture"])

if __name__ == '__main__':
    unittest.main()