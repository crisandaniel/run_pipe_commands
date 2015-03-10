Run Piped Commands
==================

Using subprocess run piped commands

Usage:
```
$ python pipecmds.py
```

The following commands are executed - there must be at least one pipe
```
print runPipe(['ls -1', 'cat sample.txt']) 								=> ls -1 | cat sample.txt
print runPipe(['cat sample.txt', 'head -6']) 							=> cat sample.txt | head -6
print runPipe(['cat sample.txt', 'head -6', 'tail -3'])					=> cat sample.txt | head -6 | tail -3
print runPipe(['cat sample.txt', 'head -6', 'tail -3', 'grep grep'])	=> cat sample.txt | head -6 | tail -3 | grep grep
print runPipe(['ls -1', 'cat nofile.txt'])								=> ls -1 | cat nofile.txt
```

Sample output
```
(True, ['line 1', 'line 2', 'line 3', 'line 4', 'line 5 grep this', 'line 6', 'line 7 ', 'line 8', 'line 9', 'line 10'])
(True, ['line 1', 'line 2', 'line 3', 'line 4', 'line 5 grep this', 'line 6'])
(True, ['line 4', 'line 5 grep this', 'line 6'])
(True, ['line 5 grep this'])
(False, 'cat: nofile.txt: No such file or directory\n')
```