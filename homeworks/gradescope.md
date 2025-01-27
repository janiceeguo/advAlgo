CS3100 - Information about Gradescope and Submitting Assignments
===============================

[Back to Homeworks](./index.html)

[Back to Main Page](../index.html)

<a name="introduction"></a>Gradescope
---------------------------------------

For this course, we will be using [Gradescope](https://gradescope.com), a platform for submitting programming assignments, grading paper-based exams, and other similar things. You should have an account on Gradescope, linked to your UVa email address. This page summarizes notes related to getting your code submitted correctly on Gradescope.

<a name="introduction"></a>Programming Assignments
---------------------------------------

Your assignments can be completed in one of three programming languages: Java, C++, or Python. When you submit your code, you MUST submit the following:

- **Individual Code Files:** You must submit all of your code as individual code files with no folder structure. You can submit multiple files, but they cannot be in folders (no Java packages for example).
- **Makefile:** Gradescope will expect you to submit a Makefile. Don't be frightened by this. They are very simple and there are examples provided below. The makefile MUST be named "Makefile" exactly (capital M). 

Once your code is uploaded, the autograder will do the following things:

- **Invoke 'make'**: The unix command 'make' will be called. This will use your provided Makefile to figure out how to compile your code. You can adjust your makefile to the particulars of your project if necessary.
- **Invoke 'make run'**: The unix command 'make run' will be invoked to execute your code on several test cases. Your Makefile will define what command is executed to run your code. Gradescope will use the unix diff command to compare your output to the correct output.
- **Response given**: Once the test cases have been run, you will get one of several responses: If your code doesn't compile, you'll get a message to that effect. If your code does compile, you'll see individual test cases, each of which will say that your code either passed, had a runtime error (we won't be able to tell you what it is though), or time limeout exceeded (your code was too slow). 

**SMALL NOTE:** You can test your make file by using a unix terminal and running the following commands:

```
# compile the code
make

# run the code
# cat sampleInput.in just outputs the contents of the input file you want to test
# make run takes that input and runs your code on it (as if you are typing it in yourself)
# tail -n +2 removes the first line of output from your code (because it will always be the command that executed, not the real output of the program)
# > outputFile.out writes the output of your solution to a file called yourOutputFile.out
cat sampleInput.in | make run | tail -n +2 > yourOutputFile.out

# test if your program worked correctly. Compares your output file to expected one. -w means ignore differences in whitespace.
# If your program worked, you will see no output at all from this command.
diff -w yourOutputFile.out sampleOutput.out
```

<a name="grademeaning"></a>Meaning of Gradescope Scores
---------------------------------------

Graded assignments in Gradescope will have a indicating the percentage of test cases that were passed. For example, if there are 30 test cases and you pass 17 of these your score will be 17/30=0.567 * 10 = 5.67/10.



<a name="introduction"></a>Example Makefiles
---------------------------------------

Below are example makefiles for each language. You should look at these and make slight tweaks if necessary. The comments in the Makefile will give you some information about this.

- [Java Makefile](./makefiles/java/Makefile)
- [C++ Makefile](./makefiles/cpp/Makefile)
- [Python Makefile](./makefiles/python/Makefile)