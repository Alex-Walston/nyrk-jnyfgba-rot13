
realtxt = input(str("What would you like to rot13?"))
uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def rot_13(realtxt, ss):
  outtext = []
  ctext = []
  for letter in realtxt:
    if letter in uppercase:
      run = uppercase.index(perletter)
      crypt = (index + ss) % 26
      ctext.append(crypt)
      new = uppercase[crypt]
      outtext.append(new)
    elif letter in lowercase:
      index = lowercase.index(letter)
      crypt = (index + ss) % 26
      ctext.append(crypt)
      new = lowercase[crypt]
      outtext.append(new)
  return outtext

txt = rot_13(realtxt,13)

print (txt)
