file_name = 'data.txt'

def rewrie_file(lines):
  f = open (file_name, 'w')
  for lines in lines:
    f.write(lines)
  
  f.close()

def write_line(line):
  f = open(file_name, 'a')
  f.write(line)
  f.close()

def read_file():
  f = open(file_name, 'r')
  if f.mode == 'r':
    contend = f.read()
  else:
    contend = f"Can't read file {file_name}" 

  return contend 

def read_line():
  with open(open_name) as f:
    lines = f.readlines()

  return lines
