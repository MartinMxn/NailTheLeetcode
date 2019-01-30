package Java.Medium;

public class Fine_M_983_MinimumCostForTickets {
    public int mincostTickets(int[] days, int[] costs) {
        boolean[] dayTraveled = new boolean[366];
        for(int day : days){
            dayTraveled[day] = true;
        }
        int[] dp = new int[366];

        for(int i = 1; i < 366; i++){
            if(!dayTraveled[i]){
                dp[i] = dp[i - 1];
                continue;
            }
            int min = dp[i - 1] + costs[0];
            min = Math.min(min, dp[Math.max(0, i - 7)] + costs[1]);
            min = Math.min(min, dp[Math.max(0, i - 30)] + costs[2]);
            dp[i] = min;
        }

        return dp[365];
    }
}
