import pysam


samfile = pysam.AlignmentFile("/Users/osmanwa/workspace/Bioinformatics101/SC_SA1CB_SC_SA1CB_analysis888_DNA_v1.bam", "rb")

# print pysam.sort.usage()

iter = samfile.fetch("AGC", 10, 20)
for x in iter:
    print (str(x))
    if x > 13:
        print x
        else if