DISK_SIZE = 8
disk = [0] * DISK_SIZE  # 0 = free, 1 = allocated

def allocate_linked(size):
    allocated = 0
    first_block = -1

    for i in range(DISK_SIZE):
        if disk[i] == 0:
            disk[i] = 1
            if first_block == -1:
                first_block = i
            allocated += 1

            if allocated == size:
                return first_block

    return -1

def free_all():
    global disk
    disk = [0] * DISK_SIZE

def print_disk():
    print("Disk:", disk)

print_disk()
allocate_linked(3)
print_disk()
free_all()
print_disk()
