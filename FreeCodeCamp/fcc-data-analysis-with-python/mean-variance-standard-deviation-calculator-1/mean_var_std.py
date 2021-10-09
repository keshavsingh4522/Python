import numpy as np

def calculate(biglist):
  if len(biglist) != 9:
    raise ValueError("List must contain nine numbers.")
  
  cal = np.array(biglist).reshape(3,3)
  mean = []
  variance = []
  sd = []
  maxi = []
  mini = []
  summ = []

  for i in range(0,2):
    mean.append(cal.mean(axis=i).tolist())
    variance.append(cal.var(axis=i).tolist())
    sd.append(cal.std(axis=i).tolist())
    maxi.append(cal.max(axis=i).tolist())
    mini.append(cal.min(axis=i).tolist())
    summ.append(cal.sum(axis=i).tolist())
  
  mean.append(cal.mean())
  variance.append(cal.var())
  sd.append(cal.std())
  maxi.append(cal.max())
  mini.append(cal.min())
  summ.append(cal.sum())

  calculation = {'mean': mean, 'variance': variance, 'standard deviation': sd, 'max': maxi, 'min': mini, "sum": summ}
  
  return calculation
