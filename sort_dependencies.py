class SortDependencies:
    def __init__(self, deps: dict):
        self.deps = deps
        # create an adjacency list - dict where each package is used
        self.adjacency_list = {a: [] for a in self.deps}
        for a in self.deps:
            for n in self.deps[a]:
                self.adjacency_list[n].append(a)

    def get_root_nodes(self) -> set:
        """Get nodes without a dependency. Has to be at least one for DAG"""
        return {k for k, v in self.deps.items() if len(v) == 0}

    def sort_deps(self):
        result = []
        no_dependency_nodes = self.get_root_nodes()

        while no_dependency_nodes:
            vertex = no_dependency_nodes.pop()
            result.append(vertex)
            for a in self.adjacency_list.get(vertex, []):
                self.deps[a].remove(vertex)
                if not self.deps[a]:
                    no_dependency_nodes.add(a)

        if len(result) != len(self.deps):
            print("Cycles detected. ")
            return None
        else:
            return result


if __name__ == "__main__":
    packages: dict = {
        "packageA": [],
        "packageB": [],
        "packageC": ["packageA", "packageB"],
        "packageD": ["packageC"],
    }
    sort_deps = SortDependencies(packages)
    print(sort_deps.sort_deps())
