## Exercise

In this problem, you are given a single string *s* that is guaranteed to contain the letter a.

You should output the suffix of *s* that begins with the first occurence of the letter *a*. Namely, if *s* consists of characters *'s1''s2''s3'...'sn'* and *i* is the first index with *si = a*, then you should output the string *'si''s(i+1)'...'sn'*.

Why do you want to do this? To solve a problem in the contest!

### Input
Input consists of a single line containing a single string *s* whose length is between 1 and 1000. The string is composed of lowercase letters with no spaces. You are guaranteed the letter a appears at least once in *s*. 

### Output
Output the suffix of *s* that begins with the first occurence of the letter *a*. 

## Example

### Input 1
<pre>
banana
</pre>
### Output 1
<pre>
anana
</pre>
### Input 2
<pre>
polarbear
</pre>
### Output 2
<pre>
arbear
</pre>
### Input 3
<pre>
art
</pre>
### Output 3
<pre>
art
</pre>