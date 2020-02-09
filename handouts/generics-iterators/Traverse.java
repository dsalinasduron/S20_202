/**
 * Traverse.java
 *
 * Example program that highlights the use of iterators.
 */

import java.util.*;

public class Traverse
{
    public static void main(String[] args) {
        List<String> foods = new ArrayList<String>();

        foods.add("Apple");
        foods.add("Banana");
        foods.add("Cherry");
        foods.add("Date");
        foods.add("Eggplant");

        int i = 0;

        while (i < foods.size()) {
            System.out.println(foods.get(i));

            i++;
        }
    }
}


