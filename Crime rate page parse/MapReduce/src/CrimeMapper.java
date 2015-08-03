import java.io.IOException;
import java.util.ArrayList;
import java.util.StringTokenizer;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

public class CrimeMapper extends Mapper<LongWritable, Text, Text, IntWritable> {

  @Override
  public void map(LongWritable key, Text value, Context context)
      throws IOException, InterruptedException {

   StringTokenizer st = new StringTokenizer(value.toString());
   String zipcode = st.nextToken();
  
   for(int i =0;i<2;i++){
	   context.write(new Text(zipcode), new IntWritable(Integer.parseInt(st.nextToken())));
	   
	   
   }
   
   
  }
}
