def minTime(files, numCores, limit):
    time = 0
    files.sort(reverse=True)
    for n_of_lines in files:
        if limit > 0 and n_of_lines % numCores == 0:
            time += int(n_of_lines / numCores)
            limit -= 1
        else:
            time += n_of_lines
    return time


if __name__ == '__main__':
    for files, cores, limit, ans in [
        ([4, 1, 3, 2, 8], 4, 1, 12),
        ([5, 3, 1], 5, 5, 5),
        ([3, 1, 5], 1, 5, 9),
    ]:
        resp = minTime(files, cores, limit)
        print(resp, resp == ans)
