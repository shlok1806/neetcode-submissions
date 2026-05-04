class Solution {
public:
    bool isPalindrome(string s) {
        int left = 0; 
        int right = s.length() - 1;  // Fixed: should be length - 1
        
        while (left < right) {
            // Skip non-alphanumeric characters from left
            if (!isalnum(s[left])) {
                left++;
                continue;
            }
            
            // Skip non-alphanumeric characters from right
            if (!isalnum(s[right])) {
                right--;
                continue;
            }
            
            // Compare alphanumeric characters
            if (tolower(s[left]) != tolower(s[right])) {
                return false;
            }
            
            // Move both pointers
            left++;
            right--;
        }
        return true;
    }
};