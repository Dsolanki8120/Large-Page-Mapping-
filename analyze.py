import re
import sys
import os
import matplotlib.pyplot as plt

pagesize = 2 * 1024 * 1024  
readinput = "perf.txt"
outputfile = "largepages.txt" 
find = re.compile(r'0x[0-9a-fA-F]+\s+.*?(miss|hit)')  

def readinputfile(file_path):
    tlbmiss = {}
    with open(file_path, 'r') as file:
        for line in file:
            match = find.search(line)
            if match:
                try:
                    address = int(match.group(0).split()[0], 16)
                    tlbaccess = match.group(1).lower()
                    if "miss" in tlbaccess:
                        x = 1  
                    else:
                        continue 
                except (ValueError, IndexError):
                    continue  
                
                baseadd = (address // pagesize) * pagesize

                if baseadd in tlbmiss:
                    tlbmiss[baseadd] += x
                else:
                    tlbmiss[baseadd] = x

    return tlbmiss

def saveaddress(tlbmiss, n):
    sorted_data = sorted(tlbmiss.items(), key=lambda x: x[1], reverse=True)
    with open(outputfile, 'w') as largepfile:
        for i in range(min(n, len(sorted_data))):
            largepfile.write(f"{sorted_data[i][0]}\n") 

    return sorted_data  

def graph(X):
    
    misses = [misses for base_address, misses in X]
    
    x_values = list(range(len(misses)))

    plt.figure(figsize=(12, 6))
    plt.plot(x_values, misses, marker='o')
    plt.title('TLB Misses for 2MB Aligned Virtual Regions')
    plt.xlabel('Virtual Region Index')
    plt.ylabel('TLB Misses')
    plt.xticks(x_values)  
    plt.grid()
    plt.tight_layout()
    plt.savefig("tlb_misses_plot.png")  
    plt.show()  

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 analyze.py <n>")
        sys.exit(1)

    n = int(sys.argv[1]) 
    tlbcount = readinputfile(readinput)
    X = saveaddress(tlbcount, n)
    graph(X)

if __name__ == "__main__":
    main()
