class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int minprice = 1000000; 
        int max  =0; 
        for (int price : prices) {
            minprice = std::min(minprice, price); 
            max = std::max(max, price - minprice);
        }
        return max;
    }
};
