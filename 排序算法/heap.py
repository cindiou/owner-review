class Heap:
  def __init__(self,compare):
    self.size=0
    self.values=[]
    self.comparator=compare

  def add(self,n):
    self.values.append(n)
    self.size += 1
    self.bubbleUp()

  def peek(self):
    if self.size:
      return self.values[0]
    else:
      return None

  def poll(self):
    first,last = self.values[0],self.values.pop()
    self.size -= 1
    if self.size:
      self.values[0]=last
      self.bubbleDown()
    return first

  def bubbleDown(self):
    root = 0
    while True:
      swap,left,right = root , 2*root+1 , 2*root+2

      values = self.values
      if left<self.size and self.comparator(values[swap],values[left])>0:
        swap=left
      if right<self.size and self.comparator(values[swap],values[right])>0:
        swap=right

      if swap==root:
        break

      values[root],values[swap] = values[swap],values[root]
      root=swap # 进入下轮，考察 被交换的子节点


  def bubbleUp(self):
    child = self.size-1
    parent = (child-1)>>1

    values = self.values
    while child and self.comparator(values[parent],values[child])>0:
      values[parent],values[child] = values[child],values[parent]

      child = parent
      parent = (parent-1)>>1


if __name__ == "__main__":
  o=Heap(lambda a,b:a-b) # 最小堆
  nums=[2,54,3,4,8,23,15,31,5,43,34]
  for v in nums:
    o.add(v)

  for _ in range(len(nums)):
    print(o.poll())

