/**
 * Definition for an interval.
 * public class Interval {
 *     int start;
 *     int end;
 *     Interval() { start = 0; end = 0; }
 *     Interval(int s, int e) { start = s; end = e; }
 * }
 */
class Solution {
    public List<Interval> merge(List<Interval> intervals) {
        LinkedList<Interval> res = new LinkedList<>();
        if(intervals == null || intervals.size() == 0) return res;
        Collections.sort(intervals, (a, b) -> {
            return a.start - b.start;
        });
        Interval curInterval = intervals.get(0);
        for (int i = 1; i < intervals.size(); i++) {
            if (curInterval.end < intervals.get(i).start) {
                res.add(curInterval);
                curInterval = intervals.get(i);
            } else {
                curInterval.end = Math.max(curInterval.end, intervals.get(i).end);
            }
        }
        res.add(curInterval);
        return res;
    }
}
