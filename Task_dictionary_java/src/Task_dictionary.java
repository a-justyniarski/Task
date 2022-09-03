import java.util.*;

public class Task_dictionary {

    public static void main(String[] args) {

        int[] arr = {1,9,8,33,12,21,8,6};

        HashMap<String, Integer> map = new HashMap<String, Integer>();
        map.put("a", 1);
        map.put("b", 9);
        map.put("c", 8);
        map.put("d", 33);
        map.put("e", 12);
        map.put("f", 21);
        map.put("g", 8);
        map.put("h", 6);


        Task_dictionary sorting = new Task_dictionary();

        sorting.convert(map);


        System.out.println(map);


    }

    public void convert(HashMap<String, Integer> map) {
        List<Map.Entry<String, Integer>> list = new LinkedList<Map.Entry<String, Integer>>(map.entrySet());

        Task_dictionary sorting = new Task_dictionary();
        sorting.sort(list, list.size());
        HashMap<String, Integer> temp = new LinkedHashMap<String, Integer>();
        for (Map.Entry<String, Integer> aa : list) {
            temp.put(aa.getKey(), aa.getValue());
        }
    }

    public void sort (List<Map.Entry<String, Integer>> arr, int limit) {
        for (int i=limit/2-1; i>=0; i--) {
            heapify(arr, i, limit);
        }

        for (int i=limit-1; i>=0; i--) {
            Map.Entry<String, Integer> temp = arr.get(0);
            arr.set(0, arr.get(i));
            arr.set(i, temp);
            heapify(arr,0, i);
        }
    }

    public void heapify(List<Map.Entry<String, Integer>> arr, int i, int limit) {
        int max_i = i;
        int l = i*2+1;
        int r = i*2+2;

        if (r<limit && arr.get(r).getValue()>arr.get(max_i).getValue()) {

            max_i = r;
        }

        if (l<limit && arr.get(l).getValue()>arr.get(max_i).getValue()) {

            max_i = l;

        }

        if (max_i!=i) {

            Map.Entry<String, Integer> temp = arr.get(i);
            arr.set(i, arr.get(max_i));
            arr.set(max_i, temp);

            heapify(arr, max_i, limit);

        }

    }

}

