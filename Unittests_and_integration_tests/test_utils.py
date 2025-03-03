#!/usr/bin/env python3
""" File for testing utils.py """

import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """ Test Access Nested Map Class """
    @parameterized.expand([
        ("simple_key", {"a": 1}, ("a",), 1),
        ("nested_key", {"a": {"b": 2}}, ("a",), {"b": 2}),
        ("deep_nested_key", {"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, name, nested_map, path, expected):
        """ Test Access Nested Map Method """
        self.assertEqual(access_nested_map(nested_map, path), expected)
