import java.io.IOException;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

public class FinalScoreMapper
extends Mapper<LongWritable, Text, IntWritable, IntDouble>{
	@Override
    public void map(LongWritable key, Text value, Context context)
    throws IOException, InterruptedException{
    	String line = value.toString();
        String[] tokens = line.split(" ");
        int zipcode = Integer.parseInt(tokens[0]);
        int count = Integer.parseInt(tokens[1]);
        double weightedcnt = Double.parseDouble(tokens[2]);
        weightedcnt = Math.pow(weightedcnt/36.55, 0.2); // 36.55 for preschool; 214.79 for clinic
        
        context.write(new IntWritable(zipcode), new IntDouble(count, weightedcnt));
    }
}