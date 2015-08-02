import java.io.DataInput;
import java.io.DataOutput;
import java.io.IOException;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.DoubleWritable;
import org.apache.hadoop.io.Writable;

public class IntIntDouble implements Writable {
	private IntWritable count;
	private IntWritable noOfReviews;
	private DoubleWritable aveRating;

	public IntIntDouble() {
		this.count = new IntWritable ();
		this.noOfReviews = new IntWritable ();
		this.aveRating = new DoubleWritable ();
	} 

	public IntIntDouble (int cnt, int noReviews, double aveRating) {
		this.count = new IntWritable (cnt);
		this.noOfReviews = new IntWritable (noReviews);
		this.aveRating = new DoubleWritable (aveRating);
	}

	public void write (DataOutput out) throws IOException {
		count.write (out);
		noOfReviews.write (out);
		aveRating.write (out);
	}

	public void readFields (DataInput in) throws IOException {
		count.readFields (in);
		noOfReviews.readFields (in);
		aveRating.readFields (in);
	}

	public static IntIntDouble read (DataInput in) throws IOException {
		IntIntDouble temp = new IntIntDouble ();
		temp.readFields (in);
		return temp;
	}

	public int getCount () {
		return count.get();
	}

	public int getNoOfReviews() {
		return noOfReviews.get();
	}

	public double getAveRating() {
		return aveRating.get();
	}

	@Override
	public String toString() {
		// String s = "Count: " + count.toString()+"; ";
		// s += "No of Reviews: " + noOfReviews.toString() +": ";
		// s += "Average Rating: " + aveRating.toString();
		return String.format(count.toString() + " " + aveRating.toString() + " " + noOfReviews.toString());
	}

}