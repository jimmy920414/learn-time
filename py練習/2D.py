# 2為列表、巢狀迴圈
# row 行
# clo 列
nums = [
        [1,2,3],
        [5,6,7]
    ]
# print(nums[1][0]) # []第幾行 []第幾列 從0開始算
for row in nums:
    for clo in row:
        print(clo)