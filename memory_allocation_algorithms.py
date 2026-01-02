free_list = [[0, 100]]
last_position = 0

def allocate_best_fit(size):
    global free_list
    best_index = -1
    best_size = float('inf')

    for i, (start, length) in enumerate(free_list):
        if length >= size and length < best_size:
            best_size = length
            best_index = i

    if best_index == -1:
        return -1

    alloc_start = free_list[best_index][0]
    free_list[best_index][0] += size
    free_list[best_index][1] -= size

    if free_list[best_index][1] == 0:
        free_list.pop(best_index)

    return alloc_start

def allocate_worst_fit(size):
    global free_list
    worst_index = -1
    worst_size = -1

    for i, (start, length) in enumerate(free_list):
        if length >= size and length > worst_size:
            worst_size = length
            worst_index = i

    if worst_index == -1:
        return -1

    alloc_start = free_list[worst_index][0]
    free_list[worst_index][0] += size
    free_list[worst_index][1] -= size

    if free_list[worst_index][1] == 0:
        free_list.pop(worst_index)

    return alloc_start

def allocate_next_fit(size):
    global free_list, last_position
    n = len(free_list)
    if n == 0:
        return -1

    checked = 0
    i = last_position

    while checked < n:
        start, length = free_list[i]
        if length >= size:
            alloc_start = start
            free_list[i][0] += size
            free_list[i][1] -= size

            if free_list[i][1] == 0:
                free_list.pop(i)
                last_position = i % len(free_list) if free_list else 0
            else:
                last_position = i

            return alloc_start

        i = (i + 1) % n
        checked += 1

    return -1

def free_memory(start, size):
    global free_list
    free_list.append([start, size])
    free_list.sort()

    merged = []
    for block in free_list:
        if not merged:
            merged.append(block)
        else:
            last = merged[-1]
            if last[0] + last[1] == block[0]:
                last[1] += block[1]
            else:
                merged.append(block)
    free_list = merged

def print_free_list():
    print("Free List:", free_list)
