import java.io.IOException;
import java.math.BigDecimal;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.mapreduce.Reducer;

public class CountRatingReducer
extends Reducer<IntWritable, IntIntDouble, IntWritable, IntIntDouble>{ 
	@Override
    public void reduce(IntWritable key, Iterable<IntIntDouble> values, Context context)
    throws IOException, InterruptedException{ 
    	int count = 0;
    	int noOfReviews = 0;
    	double rating = 0.0;
    	for (IntIntDouble value : values){
    		count +=value.getCount();
            int tempNo = value.getNoOfReviews();
    		noOfReviews += tempNo;
    		rating += value.getAveRating()* (double)tempNo;
    	}
    	if(noOfReviews > 0){
    		rating /= (double)noOfReviews;
            rating = round(rating, 2);
            if(rating < 0.0 || rating > 5.0) return;
        }
    	context.write (key, new IntIntDouble (count, noOfReviews, rating));
    }

    public double round(double d, int decimalPlace) {
        BigDecimal bd = new BigDecimal(Double.toString(d));
        bd = bd.setScale(decimalPlace, BigDecimal.ROUND_HALF_UP);
        return bd.doubleValue();
    }
}