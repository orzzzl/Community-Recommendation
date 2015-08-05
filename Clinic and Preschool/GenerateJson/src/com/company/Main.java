package com.company;

import java.io.*;
import java.util.StringTokenizer;

//import org.json.simple.JSONArray;
import org.json.simple.JSONObject;

public class Main {

    public static void main(String[] args) {
        BufferedReader br = null;
        BufferedWriter bw = null;

        try {
            br = new BufferedReader(new FileReader("./preschool_score.txt"));

            File outputfile = new File("./preschool_score.json");
            if (outputfile.exists()) {
                System.out.println("file existed");
            } else {
                System.out.println("create new file");
                outputfile.createNewFile();
            }

            bw = new BufferedWriter(new FileWriter(outputfile));
           // file.write(obj.toJSONString());
            int counter = 1;
            StringBuilder resultStr = new StringBuilder("[");
            String line;
            while((line = br.readLine()) != null){
                StringTokenizer st = new StringTokenizer(line);
                int zipcode = Integer.parseInt(st.nextToken());
                int count = Integer.parseInt(st.nextToken());
                double score = Double.parseDouble(st.nextToken());
                JSONObject tempObj = new JSONObject();
                JSONObject fields = new JSONObject();
                fields.put("zipcode", zipcode);
                fields.put("score", score);
                fields.put("totalNo", count);
                tempObj.put("model", "rcmOnUser.preschoolScore");
                tempObj.put("fields", fields);
                tempObj.put("pk", counter);
                resultStr.append(tempObj.toString()+"\n") ;
                counter++;
            }
            resultStr.append("]");
            bw.write(resultStr.toString());
            bw.flush();
            bw.close();

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}

