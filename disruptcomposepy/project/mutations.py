class Mutation:
    def __init__(self, function):
        self._mutation = self._gen_mutation(function)

    def _gen_mutation(self, function):
        def func(data):
            function(data)

        return func

    def apply(self, data):
        return self._mutation(data)


def clear_func(data):
    return ""


mutations = {"CLEAR": Mutation(clear_func)}
