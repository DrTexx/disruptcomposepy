class Mutation:
    def __init__(self, name, function, filetypes):
        self.name = name
        self._mutation = self._gen_mutation(function)
        self.filetypes = filetypes

    def _gen_mutation(self, function):
        def func(data):
            return function(data)

        return func

    def apply(self, data):
        if data.filetype not in self.filetypes:
            raise Exception(
                f"Cannot mutate filetype '{data.filetype}'"
                + f" with '{self.name} mutator"
            )
        return self._mutation(data)


def clear_func(data):
    return ""


mutations = {
    "CLEAR": Mutation(name="CLEAR", function=clear_func, filetypes=[".xml"])
}
