--bubblesort
def bubblesort(x-->list):
  for i in range(len(x)-1,0,-1):
    for j in range(i-1):
      if x[j]>x[j+1]:
        x[j],x[j+1]=x[j+1],x[j]
  return x
