# LargePageMapping

**Description:**  
The **LargePageMapping** projectthe task is to select virtual address regions that are 2MB long to map with large pages. our main objective is to reduce the 
number of TLB (Translation Lookaside Buffer) misses in a given workload .This involved collect memory access data, analyze it to find the best 
regions to allocate large pages, and then modify a provided program to utilize these large pages

Performance Optimization: Focuses on reducing TLB misses and improving memory access efficiency.
Data Analysis: Python scripts process memory access data collected from perf mem output to analyze and select the best memory regions for large page mapping.
Visualization: Generates graphs visualizing TLB misses across virtual memory regions, aiding in performance analysis.
# Tool: we collect memory data using perf 
# How TO run this projet:
# first execute c file using this command : SRNO=24796 make run
# To collact data on memory access patterns, using perf mem tool : sudo perf mem record -o mem_data.perf ./main 24796
#  after this converts mem_data into perf.txt file:  sudo perf mem report -i mem_data.perf > perf.txt
# Run python script file to collect top N regions where high tlb miss occure to locate page:  python3 analyze.py <number of region>
# first run c file without modification where we find out high tlb miss spot
# then allocate large pages on this page using modified c file and again run python scipt file and compare before allocation of large page graph and after allocation of large page after allocation of large page tlb miss drastically decrease



