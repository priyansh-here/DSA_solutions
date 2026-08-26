from collections import defaultdict

class FreqStack:

    def __init__(self):
        self.freq = defaultdict(int)
        self.group = defaultdict(list)
        self.maxfreq = 0

    def push(self, x):
        self.freq[x] += 1
        f = self.freq[x]

        self.group[f].append(x)
        self.maxfreq = max(self.maxfreq, f)

    def pop(self):
        x = self.group[self.maxfreq].pop()
        self.freq[x] -= 1

        if not self.group[self.maxfreq]:
            self.maxfreq -= 1

        return x