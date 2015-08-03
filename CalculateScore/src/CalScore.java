import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;

import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.JSONValue;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;

public class CalScore {
	private static final String filePath1 = "RestaurantData.json";
	private static final String filePath2 = "ShoppingData.json";

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
	
	public static void addRatingToList(ArrayList<ZipCodeEntry> list, String zipcode, String rating) {
		for (ZipCodeEntry entry : list) {
			if(zipcode.equals(entry.getZipCode())) {
				if (rating.equals("NONE")) {
					continue;
				}else {
					entry.addRating(Double.parseDouble(rating));
				}
			}
		}
	}

	public static void createNewData(String filePath, String outputPath) {
		try {			
			FileReader reader = new FileReader(filePath);
			JSONParser jsonParser = new JSONParser();
			JSONArray jsonArray = (JSONArray) jsonParser.parse(reader);

			File outputfile = new File(outputPath);
			if (outputfile.exists()) {
				System.out.println("\""+outputPath+"\" file existed");
			} else {
				System.out.println("create " + "\""+outputPath+"\"" + " file");
				outputfile.createNewFile();
			}
			BufferedWriter output = new BufferedWriter(new FileWriter(outputfile));
			int counter = 1;
			StringBuilder resultStr = new StringBuilder("[");
			
			if (filePath.equals(filePath1)) {
				RestaurantsCollection rc = new RestaurantsCollection();
				rc.CreateCollectionFromFile();
				ArrayList<ZipCodeEntry> restList = rc.getRestList();
				
				for (Object obj : jsonArray) {
					JSONObject jsonObject = (JSONObject) obj;
					String name = (String) jsonObject.get("name");
					String zipcode = modifyAddress((String) jsonObject.get("address"));
					String price = (String) jsonObject.get("price");
					String rating = modifyRating((String) jsonObject.get("rating"));
					
					addRatingToList(restList, zipcode, rating);
				}
				
				rc.CreateInterval();
				for (ZipCodeEntry entry : restList) {
					entry.calAreaScore(rc.getIntervals());
					JSONObject tempObj = new JSONObject();
					JSONObject fields = new JSONObject();
					fields.put("zipcode", entry.getZipCode());
					fields.put("score", entry.getAreaScore());
					tempObj.put("pk", counter);
					tempObj.put("model", "rcmOnUsers.restaurantScore");
					tempObj.put("fields", fields);
					resultStr.append(tempObj.toString()+"\n") ;
					counter++;
				}	
			}else if (filePath.equals(filePath2)){
				ShoppingCollection sc = new ShoppingCollection();
				sc.CreateCollectionFromFile();
				ArrayList<ZipCodeEntry> shopList = sc.getShopList();
				
				for (Object obj : jsonArray) {
					JSONObject jsonObject = (JSONObject) obj;
					String name = (String) jsonObject.get("name");
					String zipcode = modifyAddress((String) jsonObject.get("address"));
					String price = (String) jsonObject.get("price");
					String rating = modifyRating((String) jsonObject.get("rating"));
					
					addRatingToList(shopList, zipcode, rating);
				}
				
				sc.CreateInterval();
				for (ZipCodeEntry entry : shopList) {
					entry.calAreaScore(sc.getIntervals());
					JSONObject tempObj = new JSONObject();
					JSONObject fields = new JSONObject();
					fields.put("zipcode", entry.getZipCode());
					fields.put("score", entry.getAreaScore());
					tempObj.put("pk", counter);
					tempObj.put("model", "rcmOnUsers.shoppingScore");
					tempObj.put("fields", fields);
					resultStr.append(tempObj.toString()+"\n") ;
					counter++;
				}
			}else {
				System.out.println("filepath is wrong!");
				System.exit(-1);
			}
			resultStr.append("]");
			output.write(resultStr.toString());
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
		String restaurantOutput = filePath1.replace("Data", "Score");
		createNewData(filePath1, restaurantOutput);
		String shoppingOutput = filePath2.replace("Data", "Score");
		createNewData(filePath2, shoppingOutput);
	}
}
