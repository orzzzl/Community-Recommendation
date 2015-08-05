import java.io.DataInput;
import java.io.DataOutput;
import java.io.IOException;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.DoubleWritable;
import org.apache.hadoop.io.Writable;

public class IntDouble implements Writable {
	private IntWritable count;
	private DoubleWritable weightedCount;

	public IntDouble() {
		this.count = new IntWritable ();
		this.weightedCount = new DoubleWritable ();
	} 

	public IntDouble (int cnt, double weightedCount) {
		this.count = new IntWritable (cnt);
        this.weightedCount = new DoubleWritable (weightedCount);
	}

	public void write (DataOutput out) throws IOException {
		count.write (out);
		weightedCount.write (out);
	}

	public void readFields (DataInput in) throws IOException {
		count.readFields (in);
		weightedCount.readFields (in);
	}

	public static IntDouble read (DataInput in) throws IOException {
		IntDouble temp = new IntDouble ();
		temp.readFields (in);
		return temp;
	}

	public int getCount () {
		return count.get();
	}

	public double getWeightedCount() {
		return weightedCount.get();
	}

	@Override
	public String toString() {
		// String s = "Count: " + count.toString()+"; ";
		// s += "No of Reviews: " + noOfReviews.toString() +": ";
		// s += "Average Rating: " + aveRating.toString();
		return String.format(count.toString() + " " + weightedCount.toString());
	}
}