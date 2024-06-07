data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]
data = [6, 2, (4, True, [4, {3}]), {8, 7}]
def calculate_structure_sum(tree):
    res_list = []
    def structure_sum(tree):
        s = 0
        if isinstance(tree, (list, tuple, set)):
            for i in tree:
                if isinstance(i, int):
                    s += i
                elif isinstance(i, str):
                    s += len(i)
                elif isinstance(i, dict):
                    pairs = list(i.items())
                    structure_sum(pairs)
                else:
                    structure_sum(i)

        global sum_result
        sum_result = s
        res_list.append(sum_result)
    structure_sum(tree)
    return sum(res_list)

print(calculate_structure_sum(tree = data_structure))
print(calculate_structure_sum(tree = data))