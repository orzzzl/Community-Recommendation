import java.io.IOException;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

public class RemoveRedundanceReducer
extends Reducer<Text, IntWritable, Text, Text>{ 
	public static final Text empty = new Text ("");
	@Override
    public void reduce(Text key, Iterable<IntWritable> values, Context context)
    throws IOException, InterruptedException{ 
    	String emptystr = "";
    	context.write (key, empty);
    }
}