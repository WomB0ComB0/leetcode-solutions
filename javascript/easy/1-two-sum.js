function twoSum(nums, target) {
    var map = new Map();
    for (var i = 0; i < nums.length; i++) {
        var indexDifference = map.get(target - nums[i]);
        if (indexDifference !== undefined) {
            return [indexDifference, i];
        }
        map.set(nums[i], i);
    }
}
;
