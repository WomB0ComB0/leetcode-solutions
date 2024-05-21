function twoSum(nums: number[], target: number): [number, number] {
    const map = new Map<number, number>();
    for (let i = 0; i < nums.length; i++){
        const indexDifference = map.get(target - nums[i]);
        if (indexDifference !== undefined){
            return [indexDifference, i];
        }
        map.set(nums[i], i);
    }
};