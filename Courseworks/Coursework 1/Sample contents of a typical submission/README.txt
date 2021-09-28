Your set of files uploaded to Moodle will include the following:

1. A file UPXXXXXX.py containing the Python program that will interpolate tables of points. In the Moodle sample folder, needless to say, this file is almost empty except for a header that I suggest you keep and complete.

2. A file table.txt with some points arranged in two columns. These points will be chosen by you (please don't restrict yourself to the ones in the sample...), and will be the points your program will interpolate. I want your table.txt to see how your interpolation was produced, but please bear in mind that I will also test your program with my own set of points.

3. A file function_to_plot.txt containing a lot more points -- namely points of the graph of the polynomial interpolating the points of table.txt. This file should be an output of your program UPXXXXXX.py.

4. A file divided_differences.txt containing the divided differences (the upper diagonal row in the tables shown to you in examples) with which to compute the interpolating polynomial p(x) at any x with minimal number of operations.
This file should be an output of your program UPXXXXXX.py.

5. A plot of the points of the file function_to_plot.txt. 

6. A Jupyter notebook similar to the one shown in the sample folder. If there are enough plots in it, you may skip point 5. Remember, though, that I will be testing my own table and producing my own plot with your program to test it! What is referred to as "interpolation.py" in my Jupyter notebook, is your actual UPXXXXXX.py in your case.