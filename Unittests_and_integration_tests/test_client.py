#!/usr/bin/env python3
""" Tests for client.py """
import unittest
from parameterized import parameterized, parameterized_class
from unittest.mock import patch, PropertyMock
from client import GithubOrgClient
from utils import get_json
import fixtures


class TestGithubOrgClient(unittest.TestCase):
    """ Test the GithubOrgClient class """
    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch("client.get_json")
    def test_org(self, org_name, mock_get_json):
        """ Test that GithubOrgClient.org returns the correct value """
        expected_result = {
            "name": org_name, "repos_url": f"https://api.github.com/orgs/{org_name}/repos"}
        mock_get_json.return_value = expected_result

        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, expected_result)

        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}")

    @patch("client.GithubOrgClient.org", new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org):
        """ Test that _public_repos_url returns the expected URL """
        mock_org.return_value = {
            "repos_url": "https://api.github.com/orgs/test_org/repos"}
        client = GithubOrgClient("test_org")
        self.assertEqual(client._public_repos_url,
                         "https://api.github.com/orgs/test_org/repos")

    @patch("client.get_json")
    @patch("client.GithubOrgClient._public_repos_url", new_callable=PropertyMock)
    def test_public_repos(self, mock_public_repos_url, mock_get_json):
        """ Test that public_repos returns the expected list """
        mock_public_repos_url.return_value = "https://api.github.com/orgs/test_org/repos"
        mock_get_json.return_value = [
            {"name": "repo1"},
            {"name": "repo2"},
        ]
        client = GithubOrgClient("test_org")
        expected_repos = ["repo1", "repo2"]
        self.assertEqual(client.public_repos(), expected_repos)

        mock_public_repos_url.assert_called_once()
        mock_get_json.assert_called_once_with(
            "https://api.github.com/orgs/test_org/repos")

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """ Test that has_license returns the expected boolean """
        self.assertEqual(GithubOrgClient.has_license(
            repo, license_key), expected)


@parameterized_class([
    {"org_payload": fixtures.org_payload, "repos_payload": fixtures.repos_payload,
     "expected_repos": fixtures.expected_repos, "apache2_repos": fixtures.apache2_repos}
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """ Integration test for GithubOrgClient.public_repos """

    @classmethod
    def setUpClass(cls):
        """ Set up test class by mocking requests.get """
        cls.get_patcher = patch("requests.get")
        cls.mock_get = cls.get_patcher.start()

        def get_json_side_effect(url):
            if url == f"https://api.github.com/orgs/test_org":
                return cls.org_payload
            elif url == cls.org_payload["repos_url"]:
                return cls.repos_payload
            return None

        cls.mock_get.return_value.json.side_effect = get_json_side_effect

    @classmethod
    def tearDownClass(cls):
        """ Stop the patcher """
        cls.get_patcher.stop()

    def test_public_repos(self):
        """ Test that public_repos returns the correct list """
        client = GithubOrgClient("test_org")
        self.assertEqual(client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        """ Test public_repos with Apache 2 license filtering """
        client = GithubOrgClient("test_org")
        self.assertEqual(client.public_repos("apache-2.0"), self.apache2_repos)
