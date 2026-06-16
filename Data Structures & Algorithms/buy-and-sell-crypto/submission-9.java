class Solution {
    public int maxProfit(int[] prices) {

        int minPrice = prices[0];
        int maxP = 0;
        

        for (int price : prices){
            minPrice = Math.min(minPrice, price);
            maxP = Math.max(maxP, price - minPrice);
        }

        return maxP;
    }
}
