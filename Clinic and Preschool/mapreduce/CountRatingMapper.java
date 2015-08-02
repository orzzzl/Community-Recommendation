import java.io.IOException;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

public class CountRatingMapper
extends Mapper<LongWritable, Text, IntWritable, IntIntDouble>{ 
	@Override
    public void map(LongWritable key, Text value, Context context)
    throws IOException, InterruptedException{
    	String line = value.toString();
        String[] tokens = line.split(";");
        if (!tokens[5].contains ("NY"))
        	return;
        String[] temp = tokens[5].split("NY");
        int len = temp.length;
        temp[len-1] = temp[len-1].trim();
        if(!temp[len-1].matches("[0-9]{5}"))
                    return;
        int zipcode = Integer.parseInt(temp[len-1]);
        tokens[2] = tokens[2].trim();
        temp = tokens[2].split(" ");
        temp[0] = temp[0].trim();
        double rating = Double.parseDouble(temp[0]);
        tokens[3] = tokens[3].trim();
        temp = tokens[3].split(" ");
        temp[0] = temp[0].trim();
        int noOfReviews = Integer.parseInt(temp[0]);

        context.write(new IntWritable(zipcode), new IntIntDouble(1, noOfReviews, rating));
    }
}