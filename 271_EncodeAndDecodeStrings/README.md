Design an algorithm to encode __a list of strings__ to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

Machine 1 (sender) has the function:
```c++
string encode(vector<string> strs) {
  // ... your code
  return encoded_string;
}
```

Machine 2 (receiver) has the function:
```c++
vector<string> decode(string s) {
  //... your code
  return strs;
}
```
So Machine 1 does:
```c++
string encoded_string = encode(strs);
```
and Machine 2 does:
```c++
vector<string> strs2 = decode (encoded_string);
```
`strs2` in Machine 2 should be the same as `strs` in Machine 1.

Implement the  `encode` and `decode` methods.

__Note__:

* The string may contain any possible characters out of 256 valid ascii characters. Your algorithm should be generalized enough to work on any possible characters.

* Do not use class member/global/static variables to store states. Your encode and decode algorithms should be stateless.

* Do not rely on any library method such as eval or serialize methods. You should implement your own encode/decode algorithm.