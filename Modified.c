#include "work.h"
#include <stdio.h>
#include <stdlib.h>
#include <sys/mman.h>
#include <fcntl.h>
#include <unistd.h>

#define pagesize (2 * 1024 * 1024)  

int main(int argc, char *argv[]) {
    if (argc != 2) {
        fprintf(stderr, "Usage: main <last 5 digits of your reg. no>\n");
        return EXIT_FAILURE;
    }
    work_init(atoi(argv[1]));

    FILE *file = fopen("largepages.txt", "r");
    
    unsigned long addr;
    while (fscanf(file, "%lu", &addr) == 1) {
        if (mmap((void *)addr, pagesize, PROT_READ | PROT_WRITE, 
                 MAP_PRIVATE | MAP_ANONYMOUS | MAP_FIXED | MAP_HUGETLB, -1, 0) == MAP_FAILED) {
            perror("mmap failed");
            fclose(file);
            return EXIT_FAILURE;
        }
    }

    fclose(file);
    
    
    if (work_run() == 0) {
        printf("Work completed successfully\n");
    }

    return 0;
}
