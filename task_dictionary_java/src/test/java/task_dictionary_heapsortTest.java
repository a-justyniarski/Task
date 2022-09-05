import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;

import static org.junit.jupiter.api.Assertions.*;

class task_dictionary_heapsortTest {

    @Test
    void alreadySortedDict() {

        HashMap<String, Integer> map1 = new HashMap<String, Integer>() {{
            put("a", 1);
            put("b", 2);
            put("c", 3);
            put("d", 4);
            put("e", 5);
            put("f", 6);
            put("g", 7);
        }};

        ArrayList<String> mapKeysSorted = task_dictionary_heapsort.keyListSortedHeapsort(map1);
        for (int i = 0; i < mapKeysSorted.size() - 1; i++) {
            assertTrue(map1.get(mapKeysSorted.get(i)) <= map1.get(mapKeysSorted.get(i + 1)));
        }
    }

    @Test
    void reverseSortedDict() {

        HashMap<String, Integer> map1 = new HashMap<String, Integer>() {{
            put("a", 7);
            put("b", 6);
            put("c", 5);
            put("d", 4);
            put("e", 3);
            put("f", 2);
            put("g", 1);
        }};

        ArrayList<String> mapKeysSorted = task_dictionary_heapsort.keyListSortedHeapsort(map1);
        for (int i = 0; i < mapKeysSorted.size() - 1; i++) {
            assertTrue(map1.get(mapKeysSorted.get(i)) <= map1.get(mapKeysSorted.get(i + 1)));
        }
    }


    @Test
    void sameValuesSortedDict() {

        HashMap<String, Integer> map1 = new HashMap<String, Integer>() {{
            put("a", 1);
            put("b", 1);
            put("c", 1);
            put("d", 1);
            put("e", 1);
            put("f", 1);
            put("g", 1);
        }};

        ArrayList<String> mapKeysSorted = task_dictionary_heapsort.keyListSortedHeapsort(map1);
        for(int i = 0; i< mapKeysSorted.size()-1; i++) {
            assertTrue(map1.get(mapKeysSorted.get(i)) <= map1.get(mapKeysSorted.get(i+1)));
        }
    }


    @Test
    void emptyDict() {

        HashMap<String, Integer> map1 = new HashMap<String, Integer>() {{
        }};

        ArrayList<String> mapKeysSorted = task_dictionary_heapsort.keyListSortedHeapsort(map1);
        for (int i = 0; i < mapKeysSorted.size() - 1; i++) {
            assertTrue(map1.get(mapKeysSorted.get(i)) <= map1.get(mapKeysSorted.get(i + 1)));
        }
    }


    @Test
    void repeatedDoubleSortedDict() {

        HashMap<String, Integer> map1 = new HashMap<String, Integer>() {{
            put("a", 1);
            put("b", 2);
            put("c", 1);
            put("d", 2);
            put("e", 1);
            put("f", 2);
            put("g", 1);
        }};

        ArrayList<String> mapKeysSorted = task_dictionary_heapsort.keyListSortedHeapsort(map1);
        for (int i = 0; i < mapKeysSorted.size() - 1; i++) {
            assertTrue(map1.get(mapKeysSorted.get(i)) <= map1.get(mapKeysSorted.get(i + 1)));
        }
    }

    @Test
    void LargeNumbersSortedDict() {

        HashMap<String, Integer> map1 = new HashMap<String, Integer>() {{
            put("a", 165498426);
            put("b", 245665132);
            put("c", 654621658);
            put("d", 421562315);
            put("e", 562165132);
            put("f", 235321545);
            put("g", 465421354);
        }};

        ArrayList<String> mapKeysSorted = task_dictionary_heapsort.keyListSortedHeapsort(map1);
        for (int i = 0; i < mapKeysSorted.size() - 1; i++) {
            assertTrue(map1.get(mapKeysSorted.get(i)) <= map1.get(mapKeysSorted.get(i + 1)));
        }
    }

}