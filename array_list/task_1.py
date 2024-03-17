"""
1. Сумма двух
Учитывая массив целых чисел nums и целое число target,
верните индексы двух чисел таким образом,
чтобы они в сумме равнялись target.
Вы можете предположить, что каждый ввод будет иметь ровно одно решение,
и вы не можете использовать один и тот же элемент дважды.
Вы можете вернуть ответ в любом порядке.
входные данные: числа = [2,7,11,15], target = 9
Выходные данные: [0,1]
Объяснение: Поскольку nums[0] + nums[1] == 9, мы возвращаем [0, 1].
"""
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        return next((i, j) for i in range(len(nums)) for j in range(len(nums[:i])) if (nums[i] + nums[j] == target))
        
if __name__ == '__main__':
    print(*sorted(Solution.twoSum(self=Solution, nums=[3,2,3], target=6)))


# for i in range(len(nums)):
        # for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]
        # return []