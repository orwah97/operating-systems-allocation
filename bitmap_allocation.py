DISK_SIZE = 8
bitmap = [0] * DISK_SIZE  # 0 = free, 1 = allocated

def allocate_bitmap(size):
    free_count = 0
    start_index = -1

    for i in range(DISK_SIZE):
        if bitmap[i] == 0:
            if free_count == 0:
                start_index = i
            free_count += 1

            if free_count == size:
                for j in range(start_index, start_index + size):
                    bitmap[j] = 1
                return start_index
        else:
            free_count = 0

    return -1

def free_bitmap(start, size):
    for i in range(start, start + size):
        if i < DISK_SIZE:
            bitmap[i] = 0

def print_bitmap():
    print("Bitmap:", bitmap)

print_bitmap()
start = allocate_bitmap(3)
print_bitmap()
free_bitmap(start, 3)
print_bitmap()
