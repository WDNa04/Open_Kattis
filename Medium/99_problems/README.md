## Exercise

You’re creating problems for a practical examination, but you’re told your problems are either too hard or too easy. Fortunately, you’ve got 99 problems and coming up with more ain’t one. To decide on suitable problems, you will discard problems based on their difficulty.

After coming up with *N* problems of difficulty *D*<sub>i</sub>, you will be told to discard either
1. The easiest problem *strictly harder than difficulty D*. If you have problems of difficulties [10, 10, 11] and students find *D* = 10 too hard, you will discard *D*<sub>i</sub> = 11 to get [10, 10]. 
2. The hardest problem *not harder than difficulty D.* If you have problems of difficultues [10, 10, 11] and students find *D* = 10 too easy, you will discard teh last *D*<sub>i</sub> = 10 to get [10,11]. 

### Input
The first line contains two integers *N* (1 $\le$ *N* $\le$ $5\times10^5$) and *Q* (1 $\le$ *Q* $\le$ $10^5$). 

The next line contains *N* integers of *D*<sub>i</sub> (1 $\le$ *D*<sub>i</sub> $\le$ $10^9$), the difficulties of the *N* problems you came up with.

The next *Q* lines contain two integers *T* (1 or 2) and *D* (1 $\le$ *D* $\le$ $10^9$). *T* corresponds to discarding problems *strictly harder than* (1) or *not harder than* (2) *D*. 
### Output
For each problem discarded, print the difficulty *D*<sub>i</sub> of the problem on a new line. If a problem of the required difficulty does not exist or was previously discarded, print -1. 

## Example
### Input 1
<pre>
3 4
10 10 11
1 10
1 10
1 9
1 5
</pre>
### Output 1
<pre>
11
-1
10
10
</pre>
### Input 2
<pre>
3 4
10 10 11
2 10
2 10
2 10
2 15
</pre>
### Output 2
<pre>
10
10
-1
11
</pre>