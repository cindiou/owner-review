# 冒泡排序：冒泡一个最大的
def bubbleSort(nums,compare):
  l=len(nums)
  for i in range(1,l):
    for j in range(l-i):
      if compare(nums[j],nums[j+1])>0:
        nums[j],nums[j+1] = nums[j+1],nums[j]

# 选择排序:选择一个最小的
def selectSort(nums,compare):
  l=len(nums)
  for i in range(l):
    for j in range(i+1,l):
      if compare(nums[i],nums[j])>0:
        nums[i],nums[j] = nums[j],nums[i]


# 插入排序:从后往前找出一个适合插入地位置
def insertSort(nums,compare):
  l=len(nums)
  for i in range(l):
    j,tmp = i-1,nums[i]
    while j>=0 and compare(nums[j],tmp)>0:
      nums[j+1]=nums[j] # 当前索引j所在数字 后移一位
      j -= 1

    nums[j+1]=tmp


# 希尔排序
def shellSort(nums,compare):
  l,i = len(nums),1
  while (gap:=l>>i) != 0:
    for j in range(gap,l):
      k=j-gap
      while k>=0 and compare(nums[k],nums[k+gap])>0:
        nums[k],nums[k+gap] = nums[k+gap],nums[k]
        k -= gap

    i += 1