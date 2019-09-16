from copy import copy


def too_chaotic_validate(q):
    for ii in q:
        ii_index = q.index(ii) + 1
        # print(ii_index)
        if abs(ii_index - ii) > 2:
            return True
    return False


def sorter_queue(q, steps=None):
    if not steps:
        steps = 0

    sorted_queue = copy(q)
    for ii in q[:-1]:
        ii_index = q.index(ii)
        if ii > q[ii_index + 1]:
            steps += 1
            sorted_queue[ii_index] = q[ii_index + 1]
            sorted_queue[ii_index + 1] = ii
            return sorter_queue(sorted_queue, steps)

    # If resultado esperado diferente de range(1,len), rodar de novo
    # answer = list(range(1, len(q) + 1))
    # if sorted_queue != answer:
    #     return sorter_queue(sorted_queue, steps)

    return sorted_queue, steps


def minimumBribes(q):
    is_too_chaotic = too_chaotic_validate(q)
    if is_too_chaotic:
        print('Too chaotic')
        return None

    sq, steps = sorter_queue(q)
    print(steps)


if __name__ == '__main__':
    input = [
        {
            'n': 5,
            'q': [2, 1, 5, 3, 4]
        },
        {
            'n': 5,
            'q': [2, 5, 1, 3, 4]
        },
        {
            'n': 7,
            'q': [1, 2, 5, 3, 7, 8, 6, 4]
        }
    ]
    # import pdb; pdb.set_trace()
    for t_itr in input:
        # print(t_itr)
        q = t_itr['q']

        minimumBribes(q)
