You are given a large string. You need to cut the string into chunks such that each substring that you get is a palindrome. Remember that each 1 length string is always a palindrome. You need to find the minimum number of cuts that you need to make such that each substring is a palindrome.

Example:

```
String x = "xabaay"
5 cuts makes all the substrings palindrome : x, a, b, a, a, y
4 cuts makes all the substrings palindrome : x, a, b, aa, y
3 cuts makes all the substrings palindrome : x, aba, a, y
Output: 3 cuts
```