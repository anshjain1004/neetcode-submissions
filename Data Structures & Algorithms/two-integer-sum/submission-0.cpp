class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int n = nums.size();
        map<int, int> store;
        for(int i = 0 ; i < n ; i++){
            int remaining = target - nums[i];
            if(store.find(remaining) != store.end()){
                return {store[remaining], i};
            }
            store[nums[i]] = i;
        }
    }
};
