class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        map<int, int> map;
        for (int x : nums) {
            map[x]++;
            if (map[x]> 1) {
                return true;
            }
            
        }
        return false;
    }
};