import java.io.IOException;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

public class RemoveRedundanceMapper
extends Mapper<LongWritable, Text, Text, IntWritable>{
	public static final IntWritable one = new IntWritable(1);
	@Override
    public void map(LongWritable key, Text value, Context context)
    throws IOException, InterruptedException{
    	context.write (value, one);
    }
}