function partition(nums, left, right) {
  const x = nums[right];
  let p = left - 1;
  for (let i = left; i < right; i++) {
    if (nums[i] <= x) {
      ++p;
      [nums[p], nums[i]] = [nums[i], nums[p]];
    }
  }

  p++;
  [nums[p], nums[right]] = [nums[right], nums[p]];

  return p;
}

function quickSort(nums, left, right) {
  if (left < right) {
    let i = partition(nums, left, right);
    quickSort(nums, left, i - 1);
    quickSort(nums, i + 1, right);
  }
}

let a = [3, 5, 6, 1, 23, 15, 31, 27, 15, 6, 8, 27, 22];
quickSort(a, 0, a.length - 1);
console.log(a);
