import heapq

def huffman_coding(freq):
    heap = [[w, [ch, ""]] for ch, w in freq.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    return sorted(heapq.heappop(heap)[1:], key=lambda x: (len(x[-1]), x))

freq = {'A': 5, 'B': 9, 'C': 12, 'D': 13, 'E': 16, 'F': 45}
print("Huffman codes:", huffman_coding(freq))


'''
Huffman Coding Algorithm
Definition: A compression algorithm that assigns variable-length binary codes to characters based on their frequency.
Objective: Minimize the total length of the encoded message.
     (Root)
     /    \
   'F'(45)  (70)
         /      \
      'C'(16)  ...

'''