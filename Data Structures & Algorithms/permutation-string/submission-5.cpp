class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        if (s1.length() > s2.length()) return false;
        
        for (int i = 0; i <= s2.length() - s1.length(); i++) {
            map<char, int> map1;
            map<char, int> map2;
            
            // Count characters in s1
            for (int k = 0; k < s1.length(); k++) {
                map1[s1[k]]++;
            }
            
            // Count characters in current window of s2
            for (int j = i; j < i + s1.length(); j++) {
                map2[s2[j]]++;
            }
            
            if (map1 == map2) {
                return true;
            }
        }
        return false;
    }
};