import java.util.*;

public class task_dictionary_quicksort {


    public static void main(String[] args) {

        HashMap<String, Integer> map = new HashMap<String, Integer>() {{
            put("a", 1);
            put("b", 9);
            put("c", 8);
            put("d", 33);
            put("e", 12);
            put("f", 21);
            put("g", 8);
            put("h", 6);
        }};


        System.out.println(map);
        System.out.println(quicksortConverted(map));
        System.out.println(keyListSortedQuicksort(map));
    }


    public static LinkedHashMap<String, Integer> quicksortConverted(HashMap<String, Integer> map) {
        List<Map.Entry<String, Integer>> list = new LinkedList<>(map.entrySet());

        task_dictionary_quicksort quicksort = new task_dictionary_quicksort();

        quicksort.quicksort(0, list.size()-1, list);

        LinkedHashMap<String, Integer> convertedHashMap = new LinkedHashMap<>();
        for (Map.Entry<String, Integer> aa : list) {
            convertedHashMap.put(aa.getKey(), aa.getValue());
        }

        return convertedHashMap;
    }

    public static ArrayList<String> keyListSortedQuicksort (HashMap<String, Integer> map) {
        ArrayList<String> keyListSorted = new ArrayList<>();
        LinkedHashMap<String, Integer> sortedMap = quicksortConverted(map);
        Iterator<Map.Entry<String, Integer>> iterator = sortedMap.entrySet().iterator();
        while(iterator.hasNext()){
            keyListSorted.add(iterator.next().getKey());
        }
        return keyListSorted;
    }


    public static int partition (int l, int r, List<Map.Entry<String, Integer>> arrP) {

        int pivot = arrP.get(r).getValue();
        int pointer = l;

        for(int i = l; i < r; i++) {

            if(arrP.get(i).getValue() <= pivot) {

                Map.Entry<String, Integer> temp = arrP.get(i);
                arrP.set(i, arrP.get(pointer));
                arrP.set(pointer, temp);
                pointer += 1;
            }
        }

        Map.Entry<String, Integer> temp = arrP.get(r);
        arrP.set(r, arrP.get(pointer));
        arrP.set(pointer, temp);

        return pointer;
    }


    public void quicksort (int l, int r, List<Map.Entry<String, Integer>> arrQ) {

        if(l<r) {
            int pi = partition(l, r, arrQ);
            quicksort(l, pi-1, arrQ);
            quicksort(pi+1, r, arrQ);
        }
    }
}
