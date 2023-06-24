## Prerequisites

- Python3
- ANTLR4

## Setup

1. Set environment variable ANTLR_JAR to the file antlr-4.9.2-complete.jar in your computer
2. Change current directory to ppl-222-assignment-4/src where there is a file named run.py, then run below command to generate needed files

   ```sh
   python3 run.py gen 
   ```
3. Run 100 testcases by typing below command

   ```sh
   python3 run.py test CodeGenSuite
   ```

## Notes

- This project runs on Windows 10/11
- If you wanna run on Linux, go to src/test and then open TestUtils.py file
- On line 200, change "java -cp ./lib;. MT22Class" to "java -cp ./lib:. MT22Class"
