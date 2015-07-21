import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStreamReader;

import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;

public class ReadJson {
	private static final String filePath1 = "restaurantData.json";
	private static final String filePath2 = "shoppingData.json";

	public static String modifyAddress(String address) {
		String[] temp = address.split(" ");
		String zipcode = temp[temp.length - 1];
		return zipcode;
	}

	public static String modifyRating(String rating) {
		String[] temp = rating.split(" ");
		String rate = temp[0];
		return rate;
	}

	public static void createNewData(String filePath, String outputPath) {
		try {			
			JSONArray newItems = new JSONArray();
			File f = new File(outputPath);
			if (f.exists()) {
				System.out.println("\""+outputPath+"\" file existed");
			} else {
				System.out.println("create " + "\""+outputPath+"\"" + " file");
				f.createNewFile();
			}
			BufferedWriter output = new BufferedWriter(new FileWriter(f));
			
			FileReader reader = new FileReader(filePath);
			JSONParser jsonParser = new JSONParser();
			JSONArray jsonArray = (JSONArray) jsonParser.parse(reader);
			int counter = 1;
			for (Object obj : jsonArray) {
				JSONObject jsonObject = (JSONObject) obj;
				String name = (String) jsonObject.get("name");
				String zipcode = modifyAddress((String) jsonObject.get("address"));
				String price = (String) jsonObject.get("price");
				String rating = modifyRating((String) jsonObject.get("rating"));
				
				JSONObject tempObj = new JSONObject();
				JSONObject fields = new JSONObject();
				fields.put("name", name);
				fields.put("zipcode", zipcode);
				fields.put("price", price);
				fields.put("rating", rating);
				
				tempObj.put("pk", counter);
				if (filePath=="restaurantData.json") {
					tempObj.put("model", "rcmOnFacts.restaurant");
				}else if(filePath=="shoppingData.json"){
					tempObj.put("model", "rcmOnFacts.shopping");
				}else {
					System.out.println("Something wrong");
					System.exit(-1);
				}	
				tempObj.put("fields", fields);
				newItems.add(tempObj);
				//resultStr += tempObj.toString()+"\n";
			}
			
			//output.write(resultStr);
			output.write(newItems.toString());
			output.flush();
			output.close();
		} catch (FileNotFoundException ex) {
			ex.printStackTrace();
		} catch (IOException ex) {
			ex.printStackTrace();
		} catch (NullPointerException ex) {
			ex.printStackTrace();
		} catch (ParseException e) {
			e.printStackTrace();
		}
	}

	public static void main(String[] args) {
		String restaurantOutput = "New"+filePath1;
		createNewData(filePath1, restaurantOutput);
		String shoppingOutput = "New"+filePath2;
		createNewData(filePath2, shoppingOutput);
	}
}
