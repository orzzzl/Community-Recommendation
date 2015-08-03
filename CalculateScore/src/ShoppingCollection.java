import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.util.ArrayList;


public class ShoppingCollection {
	private static final String filePath = "zipcode.txt";
	private ArrayList<ZipCodeEntry> shopList;
	private int minSize;
	private int maxSize;
	private ArrayList<Integer> intervals;
	private static final int interSize = 6;

	public ShoppingCollection() {
		shopList = new ArrayList<ZipCodeEntry>();
		minSize = Integer.MAX_VALUE;
		maxSize = Integer.MIN_VALUE;
		intervals = new ArrayList<Integer>();
	}

	public ArrayList<ZipCodeEntry> getShopList() {
		return shopList;
	}
	
	public ArrayList<Integer> getIntervals(){
		return intervals;
	}

	public void CreateCollectionFromFile() {
		try {
			File zipcodeFile = new File(filePath);
			if (zipcodeFile.isFile() && zipcodeFile.exists()) {
				InputStreamReader read = new InputStreamReader(new FileInputStream(
						zipcodeFile));
				BufferedReader bufferedReader = new BufferedReader(read);
				String lineTxt = null;
				while ((lineTxt = bufferedReader.readLine()) != null) {
					shopList.add(new ZipCodeEntry(lineTxt));
				}
				read.close();
			} else {
				System.out.println("Cannot open the file!");
				System.exit(-1);
			}
		} catch (Exception e) {
			// TODO: handle exception
			System.out.println("Reading file is wrong!");
			e.printStackTrace();
		}
	}

	public void findMaxSize() {
		for (ZipCodeEntry entry : shopList) {
			int size = entry.getRatings().size();
			maxSize = maxSize > size ? maxSize : size;
		}
	}

	public void findMinSize() {
		for (ZipCodeEntry entry : shopList) {
			int size = entry.getRatings().size();
			minSize = minSize < size ? minSize : size;
		}
	}
	
	public void CreateInterval() {
		findMaxSize();
		findMinSize();
		int temp = (maxSize - minSize) / interSize;
		for (int i = 0; i < interSize; i++) {
			intervals.add(minSize + i * temp);
		}
	}
}
