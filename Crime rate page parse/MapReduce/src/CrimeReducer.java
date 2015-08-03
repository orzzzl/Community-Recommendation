import java.io.IOException;

import org.apache.hadoop.io.DoubleWritable;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

public class CrimeReducer extends Reducer<Text, IntWritable, Text, IntWritable> {

  @Override
  public void reduce(Text key, Iterable<IntWritable> values, Context context)
      throws IOException, InterruptedException {
	  int sum = 0, average;
	  for(IntWritable i:values){
		  sum+= i.get();		  
	  }
	  average = sum/2;
	  context.write(key, new IntWritable(average));
  }
}