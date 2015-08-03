import java.util.ArrayList;
import java.util.List;

/*
 * For each zip code, the score equals to:
 * score = rcoe * Part1 + ncoe * Part2
 * Part1 is related to rating and part2 is related to the number of restaurants in this area.
 * And rcoe and ncoe are coefficient, I temporarily define them to 0.7 and 0.3 respectively, 
 * since rating is supposed to have higher weight.
 * part1 = averageRating + variance * coe, coe is temporarily defined to 0.1
 * Because Part1's range is [0, 5], I also divide Part2 to [0, 5].
 * Find the max number and min number of restaurants in all areas, and divide the range to 6 part.
 * So [minSize, maxSize] => [0, 5]
 */

public class ZipCodeEntry {
	private String zipcode;
	private List<Double> ratingList;
	private double aveRating;
	private double variance;
	private double part1Score;
	private double part2Score;
	private double areaScore;
	private static final double coe = 0.1;      // coefficient of variance
	private static final double rcoe = 0.7;     // coefficient of rating part score
	private static final double ncoe = 0.3;     // coefficient of number part score

	public ZipCodeEntry(String zipcode) {
		this.zipcode = zipcode;
		this.ratingList = new ArrayList<Double>();
		aveRating = 0.0;
		variance = 0.0;
		part1Score = 0.0;
		part2Score = 0.0;
		areaScore = 0.0;
	}
	
	public String getZipCode(){
		return zipcode;
	}
	
	public List<Double> getRatings() {
		return ratingList;
	}
	
	public void addRating(double rating) {
		ratingList.add(rating);
	}
	
	public void calAveRating() {
		if(ratingList.isEmpty()) {
			return;
		}
		int size = ratingList.size();
		for (Double rating : ratingList) {
			aveRating += rating.doubleValue() / (double)size;
		}
	}
	
	public void calVariance() {
		if (ratingList.isEmpty()) {
			return;
		}
		for (Double rating : ratingList) {
			variance += Math.pow((rating.doubleValue() - aveRating), 2);
		}
		variance *= coe;
	}
	
	public void calPart1Score() {
		if (ratingList.isEmpty()) {
			return;
		}
		part1Score = aveRating + coe * variance;
	}
	
	public void calPart2Score(ArrayList<Integer> intervals) {
		if (ratingList.isEmpty()) {
			return;
		}
		double score = 0.0;
		int intervalSize = intervals.size();
		int restSize = ratingList.size();
		for(int i = 0; i < intervalSize; i++) {
			if(i < intervalSize - 1) {
				if(restSize >= intervals.get(i) && restSize < intervals.get(i + 1)) {
					score = i;
				}else {
					continue;
				}
			}else {
				score = i;
			}
		}
		part2Score = score;
	}
	
	public void calAreaScore(ArrayList<Integer> intervals) {
		if (ratingList.isEmpty()) {
			return;
		}
		calAveRating();
		calVariance();
		calPart1Score();
		calPart2Score(intervals);
		areaScore = rcoe * part1Score + ncoe * part2Score;
	}
	
	public double getAreaScore() {
		return areaScore;
	}
}
