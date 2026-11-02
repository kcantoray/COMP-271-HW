
import unittest

from lookup_table import ArrayLookupTable as TableUnderTest
# Change ArrayLookupTable to LinkedLookupTable for the second run.

# Sample data used by several tests.
COMP_163 = ("COMP 163", "Discrete Structures")
COMP_170 = ("COMP 170", "Introduction to Object-Oriented Programming")
COMP_271 = ("COMP 271", "Data Structures I")
MISSING_KEY = "COMP 999"


class TestLookupTableContract(unittest.TestCase):
    """Tests written from the LookupTableADT contract only."""

    def setUp(self) -> None:
        """Runs before each test method: a fresh, empty table."""
        self.table = TableUnderTest()

    def put_three_courses(self) -> None:
        """Add COMP 163, COMP 170, COMP 271 in order."""
        for code, title in (COMP_163, COMP_170, COMP_271):
            self.table.put(code, title)

    def test_get_returns_stored_value(self) -> None:
        """get: 'Return the value stored under key'."""
        # ARRANGE
        self.put_three_courses()

        # ACT and ASSERT
        self.assertEqual(self.table.get("COMP 271"), "Data Structures I")

    def test_put_existing_key_replaces_value(self) -> None:
        """put: 'only its value is replaced'."""
        # ARRANGE
        self.put_three_courses()

        # ACT
        self.table.put("COMP 170", "Updated Course")

        # ASSERT
        self.assertEqual(self.table.get("COMP 170"), "Updated Course")
        self.assertEqual(self.table.keys(), [
            "COMP 163", "COMP 170", "COMP 271"
        ])
        self.assertEqual(self.table.size(), 3)

    def test_put_empty_key_raises_value_error(self) -> None:
        """put: 'Raise ValueError if key is the empty string'."""
        # ARRANGE
        self.put_three_courses()

        # ACT and ASSERT
        with self.assertRaises(ValueError):
            self.table.put("", "Invalid Course")

        self.assertEqual(self.table.size(), 3)

    def test_remove_returns_value(self) -> None:
        """remove: 'Remove the entry for key and return its value'."""
        # ARRANGE
        self.put_three_courses()

        # ACT
        removed_value = self.table.remove("COMP 170")

        # ASSERT
        self.assertEqual(removed_value,
                         "Introduction to Object-Oriented Programming")

    def test_failed_remove_leaves_table_unchanged(self) -> None:
        """remove: 'the table is then unchanged'."""
        # ARRANGE
        self.put_three_courses()
        original_keys = self.table.keys()

        # ACT and ASSERT
        with self.assertRaises(KeyError):
            self.table.remove(MISSING_KEY)

        self.assertEqual(self.table.keys(), original_keys)
        self.assertEqual(self.table.size(), 3)

    def test_keys_oldest_first(self) -> None:
        """keys: 'oldest entry first'."""
        # ARRANGE
        self.put_three_courses()

        # ACT and ASSERT
        self.assertEqual(self.table.keys(), [
            "COMP 163", "COMP 170", "COMP 271"
        ])

    # PART 3: FIVE ORIGINAL TESTS

    def test_put_invalid_types_raise_type_error(self) -> None:
        """put: 'Raise TypeError if key or value is not a string'."""
        # ARRANGE
        self.put_three_courses()

        # ACT and ASSERT
        with self.assertRaises(TypeError):
            self.table.put(271, "Data Structures I")

        with self.assertRaises(TypeError):
            self.table.put("COMP 271", 271)

        self.assertEqual(self.table.size(), 3)

    def test_get_missing_key_raises_key_error(self) -> None:
        """get: 'raise KeyError if absent'."""
        # ARRANGE
        self.put_three_courses()

        # ACT and ASSERT
        with self.assertRaises(KeyError):
            self.table.get(MISSING_KEY)

    def test_contains_returns_correct_result(self) -> None:
        """contains: 'Return True if key is in the table, False otherwise'."""
        # ARRANGE
        self.put_three_courses()

        # ACT and ASSERT
        self.assertTrue(self.table.contains("COMP 170"))
        self.assertFalse(self.table.contains(MISSING_KEY))

    def test_size_returns_number_of_entries(self) -> None:
        """size: 'Return the number of entries in the table'."""
        # ARRANGE
        self.put_three_courses()

        # ACT and ASSERT
        self.assertEqual(self.table.size(), 3)

        self.table.remove("COMP 170")

        self.assertEqual(self.table.size(), 2)

    def test_is_empty_returns_correct_result(self) -> None:
        """is_empty: 'Return True if the table has no entries'."""
        # ARRANGE
        self.assertTrue(self.table.is_empty())

        # ACT
        self.table.put("COMP 271", "Data Structures I")

        # ASSERT
        self.assertFalse(self.table.is_empty())


if __name__ == "__main__":
    unittest.main()
 
