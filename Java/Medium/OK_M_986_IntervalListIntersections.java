/**
 * Definition for an interval.
 * public class Interval {
 *     int start;
 *     int end;
 *     Interval() { start = 0; end = 0; }
 *     Interval(int s, int e) { start = s; end = e; }
 * }
 */
class OK_M_986_IntervalListIntersections {
    public Interval[] intervalIntersection(Interval[] A, Interval[] B) {
        List<Interval> list = new ArrayList<>();
        int i = 0, j = 0;
        while(i < A.length && j < B.length) {
            int maxstart = Math.max(A[i].start, B[j].start);
            int minend = Math.min(A[i].end, B[j].end);
            if(maxstart <= minend) list.add(new Interval(maxstart, minend));
            if(minend == A[i].end) i++;
            else j++;
        }
        return list.toArray(new Interval[list.size()]);
    }
}
