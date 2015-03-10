import subprocess

def runPipe(cmds):
  try: 
    p1 = subprocess.Popen(cmds[0].split(' '), stdin = None, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
    prev = p1
    for cmd in cmds[1:]:
      p = subprocess.Popen(cmd.split(' '), stdin = prev.stdout, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
      prev = p
    stdout, stderr = p.communicate()
    p.wait()
    returncode = p.returncode
  except Exception, e:
    stderr = str(e)
    returncode = -1
  if returncode == 0:
    return (True, stdout.strip().split('\n'))
  else:
    return (False, stderr)


if __name__ == "__main__": 
  print runPipe(['ls -1', 'cat sample.txt']) 
  print runPipe(['cat sample.txt', 'head -6'])
  print runPipe(['cat sample.txt', 'head -6', 'tail -3'])
  print runPipe(['cat sample.txt', 'head -6', 'tail -3', 'grep grep'])
  print runPipe(['ls -1', 'cat nofile.txt'])

  

