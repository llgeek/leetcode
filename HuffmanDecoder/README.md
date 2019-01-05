Given an array of Huffman code and a Huffman-encoded string, find the decoded string.

1. 1 <= n <= 100
2. 1 <= |encoded| <= 7000
3. All characters of encoded are either '0' or '1'
4. All inputs will represent a valid Huffman encoded string

Sample input:
```
7
a   100100
b   100101
c   110001
d   100000
[newline]   111111
p   111110
q   000001
111110000001100100111111100101110001111110
```

Sample output:
```
pqa
bcp
```