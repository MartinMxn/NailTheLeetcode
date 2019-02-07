class OK_E_119_Pascal'sTriangleII {
    public List<Integer> getRow(int rowIndex) {
        List<Integer> list = new ArrayList<>();
        list.add(1);
        if(rowIndex == 0) return list;  //take care of corner case, especially index
        for(int i = 0; i <= rowIndex; i++) {
            List<Integer> tmpList = new ArrayList<>();
            tmpList.add(1);
            for(int j = 1; j < i; j++) {
                tmpList.add(list.get(j - 1) + list.get(j));
            }
            tmpList.add(1);
            list = tmpList;
        }
        return list;
    }
}
