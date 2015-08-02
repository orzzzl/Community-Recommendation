import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

public class CountRating {
	public static void main (String[] args) throws Exception {
		if(args.length !=2){
            System.err.println("Usage: StringCount <input path> <output path>");
            System.exit(-1);
        }

        Job job = new Job ();
        job.setJarByClass (CountRating.class);
        setTextoutputformatSeparator (job, " ");
        job.setJobName ("Count and Average Rating");

        FileInputFormat.addInputPath (job, new Path(args[0]));
        FileOutputFormat.setOutputPath (job, new Path(args[1]));

        job.setMapperClass (CountRatingMapper.class);
        job.setReducerClass (CountRatingReducer.class);

        job.setMapOutputKeyClass (IntWritable.class);
        job.setMapOutputValueClass (IntIntDouble.class);

        job.setOutputKeyClass (IntWritable.class);
        job.setOutputValueClass (IntIntDouble.class);
        System.exit(job.waitForCompletion(true)? 0 : 1);
	}

	static void setTextoutputformatSeparator(final Job job, final String separator){
        final Configuration conf = job.getConfiguration(); //ensure accurate config ref
        conf.set("mapred.textoutputformat.separator", separator); //Prior to Hadoop 2 (YARN)
        conf.set("mapreduce.textoutputformat.separator", separator);  //Hadoop v2+ (YARN)
        conf.set("mapreduce.output.textoutputformat.separator", separator);
        conf.set("mapreduce.output.key.field.separator", separator);
        conf.set("mapred.textoutputformat.separatorText", separator); // ?
    }
}