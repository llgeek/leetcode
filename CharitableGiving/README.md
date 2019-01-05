是个简单题 charity A B C,依次给钱,先给钱最少的,一样少就按照字母排序,先给排在前面
的. 牛返回给的顺序 例子
[25,8,2,35,15,120,55,42]
["A","B","C","C","B","B","A","C",]
第一道,地里已经有的,给一列 Float profits,然后有三个公司 A B C,每次把 profits 中的钱给
A B C 中钱最少的那个;如果 A B C 钱一样多,就按照字母表顺序给。另外 input 是 Float,assign
的时候记得用 0.0f 这样的 assign 方法。
解法:我用的 priorityqueue,把 A B C 编号成 1.0f, 2.0f, 3.0f 放进一个 float[]{id, money},然后写
一个 pq 的 comparator 比较大小。one pass 一遍 profits,每次从 pq 中找出最小的,update,
再放回去