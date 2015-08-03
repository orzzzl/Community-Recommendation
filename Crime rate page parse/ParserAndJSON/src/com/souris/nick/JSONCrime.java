package com.souris.nick;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.StringTokenizer;


import org.json.simple.JSONObject;

public class JSONCrime {
	@SuppressWarnings("unchecked")
	public static void main(String[] args) throws IOException {

		String zipcode, crime, property;
		BufferedReader br = new BufferedReader(new FileReader("hiveoutput"));
		StringTokenizer st = new StringTokenizer(br.readLine());
		br.close();
		st.nextToken();
		int minimum = Integer.parseInt(st.nextToken());

		int cr, pr;
		float sc;
		int counter = 0;
		String s;
		FileWriter jsonFileWriter = new FileWriter("crime3.json");
		BufferedReader br1 = new BufferedReader(new FileReader("crime3.txt"));

		JSONObject json = new JSONObject();

		jsonFileWriter.write("[");

		while ((s = br1.readLine()) != null) {
			StringTokenizer st1 = new StringTokenizer(s);
			zipcode = st1.nextToken();
			crime = st1.nextToken();
			property = st1.nextToken();

			jsonFileWriter.write("{ \"fields\": ");
			json.put("zipcode", zipcode);

			json.put("crime", crime);

			json.put("property", property);

			cr = Integer.parseInt(crime);
			pr = Integer.parseInt(property);

			sc = ((cr + pr) / minimum);
			sc = 1 / sc;

			json.put("score", Double.toString(sc));

			jsonFileWriter.write(json.toJSONString());
			jsonFileWriter.write(", \"model\": \"rcmOnUser.crimeData\",");
			jsonFileWriter.write("\"pk\": " + (counter + 1));
			jsonFileWriter.write("}");
			if (!zipcode.equalsIgnoreCase("11697")) {
				jsonFileWriter.write(",");
			}
			json.clear();
			jsonFileWriter.flush();
			s = br1.readLine();
			counter++;

		}
		jsonFileWriter.write("]");
		jsonFileWriter.close();
		br1.close();
	}

}