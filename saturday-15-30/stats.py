import sys

file_path = sys.argv[1]  

try:
    with open(file=file_path, mode="r") as f:
        content = f.read()
        words = content.lower().split()
        words = [word.strip(",.!?") for word in words]
        stats = {}
        for word in words:
            if word not in stats:
                stats[word] = 0
            stats[word] += 1
        stats_sorted = dict(sorted(stats.items(), key=lambda pair: pair[1], reverse=True))
        for (word, occurance) in stats_sorted.items():
            print(f"{word}: {occurance}")
except FileNotFoundError:
    print("File not found. Try different file name")

except PermissionError:
    print("File exists but you don't have permissions to access it.")

