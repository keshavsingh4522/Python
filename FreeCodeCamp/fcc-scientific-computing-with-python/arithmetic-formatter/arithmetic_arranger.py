def arithmetic_arranger(problems, ans = False):
  line1 = ""
  line2 = ''
  line3 = ''
  line4 = ''
  soindex = 0

  plist = map(lambda x: x.split(" "), problems)

  for equations in list(plist):

    if equations[0].isdigit() is False or equations[2].isdigit() is False:
      return "Error: Numbers must only contain digits."

    if equations[1] != "+" and equations[1] != "-":
      return "Error: Operator must be '+' or '-'."

    if len(equations[0]) > 4 or len(equations[2]) > 4:
      return "Error: Numbers cannot be more than four digits."

    if len(problems) > 5:
      return "Error: Too many problems."
    
    else:
      firstno = equations[0]
      secondno = equations[2]
      operator = equations[1]
      length = max(len(firstno), len(secondno))

      if len(firstno) >= len(secondno):
        line2 += operator + (" " * (length - len(secondno) + 1)) + secondno
        line1 += firstno.rjust(length + 2)

      elif len(secondno) > len(firstno):
        line1 += firstno.rjust(length + 2)
        line2 += operator + " " + secondno
        
      line4 += (str(eval(problems[soindex]))).rjust(length + 2)
      soindex += 1
      

      line3 += "-" * (length + 2)

      line1 += " " * 4
      line2 += " " * 4
      line3 += " " * 4
      line4 += " " * 4

  if ans:
    final = f"{line1[:-4]}\n{line2[:-4]}\n{line3[:-4]}\n{line4[:-4]}"
  else:
    final = f"{line1[:-4]}\n{line2[:-4]}\n{line3[:-4]}"
  
  return final