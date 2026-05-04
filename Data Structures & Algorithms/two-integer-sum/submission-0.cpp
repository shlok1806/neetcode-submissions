class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int, int> res; 
        int i =0;
        for(int num : nums) {
            if (res.find(target - num) != res.end()) {
                return {res[target - num], i};
            } 
            res[num] = i;
            i++;
        }
        return {};
    }
};
