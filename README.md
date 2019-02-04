# NailTheLeetcode

## Java-Transform

1. List<Object> list -> Object[] array
list.toArray(new Object[size])

2. String -> int/double
int i = Integer/Double.parseInt/parseDouble(string)
int i = Integer/Double.valueOf(string)
dif: parseInt return int, valueOf return object
parseInt is better in efficiency

3. int -> String
String s = String.valueOf(i);
String s = Integer.toString(i);
String s = "" + i;

4. int -> ArrayList
ArrayList<Integer> a = new ArrayList<>(Arrays.asList());

5. ArrayList -> int
int[] arr = list.stream().mapToInt(Integer::valueOf).toArray();

## Java-Sort
1. Collections.sort(collectionsName, (a,b)-> ....)


## Java-String
1. lexicographic/alphabetical/dictionary order
s1.compareTo(s2) 
//compares strings on the basis of Unicode value, If first string is lexicographically greater than second string, it returns positive number (difference of character value). If first string is less than second string lexicographically, it returns negative number and if first string is lexicographically equal to second string, it returns 0.

## Java-List
1. list.subList(0, k) return k elements in the list
