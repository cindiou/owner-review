# 归并排序：
def mergeSort(nums,compare):
  def merge(nums,left,mid,right):
    tmp,l,r=[],left,mid+1
    while l<=mid or r<=right:
      if l<=mid and r<=right:
        if compare(nums[r],nums[l]) > 0:
          tmp.append(nums[l])
          l += 1
        else:
          tmp.append(nums[r])
          r += 1
      elif l<=mid:
          tmp.append(nums[l])
          l += 1
      elif r<=right:
          tmp.append(nums[r])
          r += 1       

    for i in range(len(tmp)):
      nums[left + i] = tmp[i]         

  def _mergeSort(nums,left,right):
    if left>=right:return 

    mid=left+(right-left)//2

    _mergeSort(nums,left,mid)
    _mergeSort(nums,mid+1,right)
    merge(nums,left,mid,right)

  _mergeSort(nums,0,len(nums)-1)






# 快速排序
import random
def quickSort(nums,compare):
  def partititon(nums,left,right):
    pivot=nums[right]
    ptr=left-1
    for i in range(left,right):
      if compare(pivot,nums[i]) > 0:
        ptr += 1
        nums[ptr],nums[i] = nums[i],nums[ptr]
    
    ptr += 1 # 确保ptr之前都小于nums[ptr]，之后都大于nums[ptr]
    nums[ptr],nums[right] = nums[right],nums[ptr]
    return ptr

  def _quickSort(nums,left,right):
    if left>=right:return 

    randPivot=random.randrange(left,right+1) # 随机值不包括right+1
    nums[right],nums[randPivot]=nums[randPivot],nums[right]
    p = partititon(nums,left,right)
    
    _quickSort(nums,left,p-1)
    _quickSort(nums,p+1,right)

  _quickSort(nums,0,len(nums)-1)





# 堆排序：最大堆
def heapSort(nums,compare):
  def heapify(nums,root,size):
    while True:
      swap,left,right = root,root*2+1,root*2+2

      if left<size and compare(nums[left],nums[swap]) > 0:
        swap = left
      if right<size and compare(nums[right],nums[swap]) > 0:
        swap = right

      if swap == root: break

      nums[root],nums[swap] = nums[swap],nums[root]
      root=swap
    
  def buildHeap(nums):
    size = len(nums)
    for i in range(size>>1,-1,-1):
      heapify(nums,i,size)


  buildHeap(nums)
  last=len(nums)-1
  while last:
    # 最大堆 => 顺序排序
    # 最小堆 => 逆序排序
    nums[0],nums[last] = nums[last],nums[0] # 将极值放到数组末尾

    heapify(nums,0,last)
    last -= 1




# 基数排序：O(n);而不是O(n * ln n)
def radixSort(nums,reverse=False):
  l,exp = len(nums),1
  max_num=max(nums)
  tmp=[None for _ in range(l)]

  while max_num >= exp :
    count=[0 for _ in range(10)]
    for v in nums:
      count[v//exp % 10] += 1

    if not reverse:
      # 顺序
      for i in range(1,10):
        count[i] += count[i-1]
      for v in reversed(nums):
        count[v//exp % 10] -= 1
        tmp[ count[v//exp % 10] ] = v
    else:
      _sum=0
      for i in range(9,-1,-1):
        cur_cnt=count[i]
        count[i]=_sum
        _sum += cur_cnt
      for v in nums:
        tmp[ count[v//exp % 10] ] = v
        count[v//exp % 10] += 1

    exp *= 10
    for i in range(l):
      nums[i]=tmp[i]


if __name__ == "__main__":
  n=[3,5,6,1,23,15,31,27,15,6,8,27,22]
  print("n=",n)
  radixSort(n,lambda a,b:a-b)
  print("n=",n)