## Exercise

2048 is a single-player puzzle game created by Gabriele Cirulli1. It is played on a $ 4 X 4$
 grid that contains integers $\ge$ 2 that are powers of 2. The player can use a keyboard arrow key (left/up/right/down) to move all the tiles simultaneously. Tiles slide as far as possible in the chosen direction until they are stopped by either another tile or the edge of the grid. If two tiles of the same number collide while moving, they will merge into a tile with the total value of the two tiles that collided. The resulting tile cannot merge with another tile again in the same move. Please observe this merging behavior carefully in all Sample Inputs and Outputs.

### Input
The input is always a valid game state of a 2048 puzzle. The first four lines of input, that each contains four integers, describe the 16 integers in the $ 4 X 4$ grid of 2048 puzzle. The 
j-th integer in the 
i-th line denotes the content of the cell located at the i-th row and the j-th cell. For this problem, all integers in the input will be either {0, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024}. Integer 0 means an empty cell.

The fifth line of input contains an integer 0, 1, 2, or 3 that denotes a left, up, right, or down move executed by the player, respectively.

### Output
Output four lines with four integers each. Two integers in a line must be separated by a single space. This describes the new state of the $ 4 X 4$ grid of 2048 puzzle. Again, integer 0 means an empty cell. Note that in this problem, you can ignore the part from the 2048 puzzle where it introduces a new random tile with a value of either 2 or 4 in an empty spot of the board at the start of a new turn.

## Example

### Input 1
<pre>
2 0 0 2
4 16 8 2
2 64 32 4
1024 1024 64 0
0
</pre>
### Output 1
<pre>
4 0 0 0
4 16 8 2
2 64 32 4
2048 64 0 0
</pre>

### Input 2
<pre>
2 0 0 2
4 16 8 2
2 64 32 4
1024 1024 64 0
1
</pre>
### Output 2
<pre>
2 16 8 4
4 64 32 4
2 1024 64 0
1024 0 0 0
</pre>

### Input 3
<pre>
2 0 0 2
4 16 8 2
2 64 32 4
1024 1024 64 0
2
</pre>
### Output 3
<pre>
0 0 0 4
4 16 8 2
2 64 32 4
0 0 2048 64
</pre>

### Input 4
<pre>
2 0 0 2
4 16 8 2
2 64 32 4
1024 1024 64 0
3
</pre>
### Output 4
<pre>
2 0 0 0
4 16 8 0
2 64 32 4
1024 1024 64 4
</pre>