import unittest

from sort_dependencies import SortDependencies


class SortDependenciesTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        deps = {
            "packageA": [],
            "packageB": [],
            "packageC": ["packageA", "packageB"],
            "packageD": ["packageC"],
        }
        cls.sort_deps = SortDependencies(deps=deps)

    def test_get_root_nodes(self):
        self.assertSetEqual({"packageA", "packageB"}, self.sort_deps.get_root_nodes())

    def test_cyclic_dependencies(self):
        deps = {
            "packageA": ["packageB"],
            "packageB": ["packageA"],
        }
        s = SortDependencies(deps=deps)
        self.assertIsNone(s.sort_deps())

    def test_sort_dependencies(self):
        """
        #TODO: Test that dependencies are sorted correctly
        """
