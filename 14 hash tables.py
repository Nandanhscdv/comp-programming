# Hash table example for fast string lookup
# Reads a list of strings to store and then answers queries

def main():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    try:
        n = int(next(it))
    except StopIteration:
        return
    stored = set()
    for _ in range(n):
        try:
            s = next(it)
        except StopIteration:
            break
        stored.add(s)
    try:
        q = int(next(it))
    except StopIteration:
        q = 0
    out_lines = []
    for _ in range(q):
        try:
            query = next(it)
        except StopIteration:
            break
        if query in stored:
            out_lines.append("found")
        else:
            out_lines.append("not found")
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    main()
