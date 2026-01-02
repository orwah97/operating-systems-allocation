#include <stdio.h>
#define DISK_SIZE 8

int bitmap[DISK_SIZE]; // 0 = free, 1 = allocated

int allocate_blocks(int size) {
    int count = 0;
    int start_index = -1;

    for (int i = 0; i < DISK_SIZE; i++) {
        if (bitmap[i] == 0) {
            if (count == 0)
                start_index = i;

            count++;

            if (count == size) {
                for (int j = start_index; j < start_index + size; j++) {
                    bitmap[j] = 1;
                }
                return start_index;
            }
        } else {
            count = 0;
            start_index = -1;
        }
    }
    return -1;
}

void free_blocks(int start, int size) {
    for (int i = start; i < start + size; i++) {
        if (i < DISK_SIZE)
            bitmap[i] = 0;
    }
}

void print_bitmap() {
    printf("Bitmap: ");
    for (int i = 0; i < DISK_SIZE; i++) {
        printf("%d ", bitmap[i]);
    }
    printf("\n");
}

int main() {
    for (int i = 0; i < DISK_SIZE; i++)
        bitmap[i] = 0;

    print_bitmap();

    int start = allocate_blocks(3);
    if (start != -1)
        printf("Allocated 3 blocks starting at %d\n", start);

    print_bitmap();

    free_blocks(start, 3);
    printf("Freed blocks\n");

    print_bitmap();
    return 0;
}
