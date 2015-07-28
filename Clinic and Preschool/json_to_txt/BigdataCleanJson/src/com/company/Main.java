package com.company;
import java.io.FileNotFoundException;
import java.io.File;
import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.FileReader;
import java.io.IOException;
import java.util.Iterator;
import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;

public class Main {
    public static void main(String[] args) {
        JSONParser parser = new JSONParser();

        try {
            File file = new File ("/Users/April/Documents/Java/BigdataCleanJson/preschool_nyc_995.txt");

            if (!file.exists())
                file.createNewFile();
            BufferedWriter bw = new BufferedWriter(new FileWriter(file.getAbsoluteFile()));

            JSONArray jsonArray = (JSONArray) parser.parse(new FileReader("/Users/April/Documents/Java/BigdataCleanJson/preschool_nyc_995.json"));

            for (Object o : jsonArray) {
                JSONObject jsonObject = (JSONObject) o;
                // loop array
                JSONArray title = (JSONArray) jsonObject.get("title");
                Iterator<String> it2 = title.iterator();
                String temp = it2.next();
                temp = temp.trim();
                bw.write(temp);
                //    System.out.print(it2.next());
                while (it2.hasNext()) {
                    //    System.out.print(" Clinic ");
                    //    System.out.print(it2.next());
                    bw.write(" Clinic ");
                    temp = it2.next();
                    temp = temp.trim();
                    bw.write(temp);
                }
                bw.write("; ");
                //System.out.print("; ");
                JSONArray category = (JSONArray) jsonObject.get("category");
                Iterator<String> it1 = category.iterator();
                while (it1.hasNext()) {
                //    System.out.print(it1.next());
                    temp = it1.next();
                    temp = temp.trim();
                    bw.write(temp);
                    if (it1.hasNext())
                //        System.out.print(", ");
                        bw.write(", ");
                }
            //    System.out.print("; ");
                bw.write("; ");

                String rating = (String) jsonObject.get("rating");
                rating = rating.trim();
            //    System.out.print(rating);
            //    System.out.print("; ");
                bw.write(rating);
                bw.write("; ");

                String NoOfReview = (String) jsonObject.get("NoOfReview");
                NoOfReview = NoOfReview.trim();
                //    System.out.print(NoOfReview);
                //    System.out.print("; ");
                bw.write(NoOfReview);
                bw.write("; ");

                String neighborhood = (String) jsonObject.get("neighborhood");
                neighborhood = neighborhood.trim();
            //    System.out.print(neighborhood);
             //   System.out.print("; ");
                bw.write(neighborhood);
                bw.write("; ");

                JSONArray address = (JSONArray) jsonObject.get("address");
                Iterator<String> it3 = address.iterator();
                while (it3.hasNext()) {
                //    System.out.print(it3.next());
                    temp = it3.next();
                    temp = temp.trim();
                    bw.write(temp);
                    if (it3.hasNext())
                        bw.write(", ");
                    //    System.out.print(", ");
                }
             //   System.out.print("; ");
                bw.write("; ");

                String phoneNo = (String) jsonObject.get("phoneNo");
                phoneNo = phoneNo.trim();
                bw.write(phoneNo);
                bw.write('\n');
            //    System.out.print(phoneNo);
            //    System.out.println();
            }
            bw.close();

        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        } catch (ParseException e) {
            e.printStackTrace();
        }

        /*JSONParser parser = new JSONParser();

        try {

            Object obj = parser.parse(new FileReader("/Users/April/Documents/Java/tryJsonSimple/test.json"));

            JSONObject jsonObject = (JSONObject) obj;

            String name = (String) jsonObject.get("name");
            System.out.println(name);

            long age = (Long) jsonObject.get("age");
            System.out.println(age);

            // loop array
            JSONArray msg = (JSONArray) jsonObject.get("messages");
            Iterator<String> iterator = msg.iterator();
            while (iterator.hasNext()) {
                System.out.println(iterator.next());
            }

        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        } catch (ParseException e) {
            e.printStackTrace();
        }*/
    }
}