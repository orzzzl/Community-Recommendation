import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

public class CrimeDriver {

  public static void main(String[] args) throws Exception {
	  if (args.length != 2) {
		  System.err.println("Usage: CrimeDriver <input path> <output path>");
		  System.exit(-1);
		  }
		  @SuppressWarnings("deprecation")
		  Job job = new Job();
		  job.setJarByClass(CrimeDriver.class);
		  job.setJobName("Crime Rate Averages");
		  FileInputFormat.addInputPath(job, new Path(args[0]));
		  FileOutputFormat.setOutputPath(job, new Path(args[1]));
		  job.setMapperClass(CrimeMapper.class);
		  job.setReducerClass(CrimeReducer.class);
		  job.setOutputKeyClass(Text.class);
		  job.setOutputValueClass(IntWritable.class);

		  System.exit(job.waitForCompletion(true) ? 0 : 1);

  }
}

