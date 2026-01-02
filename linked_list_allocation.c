#include <stdio.h>
#define DISK_SIZE 8

int disk[DISK_SIZE]; // 0 = free, 1 = allocated

int allocate_linked(int size) {
    int allocated = 0;
    int first_block = -1;

    for (int i = 0; i < DISK_SIZE && allocated < size; i++) {
        if (disk[i] == 0) {
            disk[i] = 1;
            if (first_block == -1)
                first_block = i;
            allocated++;
        }
    }

    return (allocated == size) ? first_block : -1;
}

void free_all() {
    for (int i = 0; i < DISK_SIZE; i++) {
        disk[i] = 0;
    }
}

void print_disk() {
    printf("Disk: ");
    for (int i = 0; i < DISK_SIZE; i++) {
        printf("%d ", disk[i]);
    }
    printf("\n");
}

int main() {
    for (int i = 0; i < DISK_SIZE; i++)
        disk[i] = 0;

    print_disk();

    int start = allocate_linked(3);
    if (start != -1)
        printf("Allocated 3 blocks starting at %d\n", start);

    print_disk();

    free_all();
    printf("Freed all blocks\n");

    print_disk();
    return 0;
}
