class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> list = new ArrayList<>();
        if(numRows == 0) return list;
        list.add(new ArrayList<>());
        list.get(0).add(1);
        for(int rowNum = 1; rowNum < numRows; rowNum++) {
            List<Integer> row = new ArrayList<>();
            List<Integer> preRow = list.get(rowNum - 1);
            row.add(1);     //first always 1
            for(int index = 1; index < rowNum; index++) {
                row.add(preRow.get(index - 1) + preRow.get(index));
            }
            row.add(1);     //last
            list.add(row);
        }
        return list;
    }
}
