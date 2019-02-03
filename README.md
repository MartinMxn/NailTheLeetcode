# NailTheLeetcode
Java-Transform
1.List<Object> list -> Object[] array
list.toArray(new Object[size])
  
2.String -> int/double
int i = Integer/Double.parseInt/parseDouble(string)
int i = Integer/Double.valueOf(string)
dif: parseInt return int, valueOf return object
parseInt is better in efficiency

3.int -> String
String s = String.valueOf(i);
String s = Integer.toString(i);
String s = "" + i;

4.int -> ArrayList
ArrayList<Integer> a = new ArrayList<>(Arrays.asList());

5.ArrayList -> int
int[] arr = list.stream().mapToInt(Integer::valueOf).toArray();

