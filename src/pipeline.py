import spark_df_profiling
import pyspark as ps
import pickle

spark = (ps.sql.SparkSession.builder 
        .master("local[4]") 
        .appName("sparkSQL exercise") 
        .getOrCreate()
        )

cc_df = spark.read.json('../data/data.json',
                         multiLine=True)
cc_df.printSchema()
# spark_df_profiling.ProfileReport(cc_df)

# profile = spark_df_profiling.ProfileReport(cc_df)
# profile.to_file(outputfile="../html/simple_eda.html")

# with open('../data/clean.pkl', 'wb') as data_file:
#     pickle.dump(final_set, data_file)