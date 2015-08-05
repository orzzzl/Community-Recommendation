import java.io.IOException;
import java.math.BigDecimal;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.DoubleWritable;
import org.apache.hadoop.mapreduce.Reducer;

public class FinalScoreReducer
extends Reducer<IntWritable, IntDouble, IntWritable,  IntDouble>{
	@Override
    public void reduce(IntWritable key, Iterable<IntDouble> values, Context context)
    throws IOException, InterruptedException{
        double weightedCount = 0.0;
        int count = 0;

    	for (IntDouble value : values){
            weightedCount = value.getWeightedCount();
            count = value.getCount();
    	}
        weightedCount = round(weightedCount, 2);
    	context.write (key, new IntDouble(count, weightedCount));
    }

    public double round(double d, int decimalPlace) {
        BigDecimal bd = new BigDecimal(Double.toString(d));
        bd = bd.setScale(decimalPlace, BigDecimal.ROUND_HALF_UP);
        return bd.doubleValue();
    }
}