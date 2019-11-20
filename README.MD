# regex in file search [![Build Status](https://travis-ci.org/ltblueberry/regex-infile-search.svg?branch=master)](https://travis-ci.org/ltblueberry/regex-infile-search)
It's a simple python script that search specified regular expression in specified input file and save all matches in result files.

# Make executable
```
chmod a+x regex_infile_search.py
```

# Usage
```
./regex_infile_search.py -i [input file] -r [regular expression] -n [name of results]
```
or
```
./regex_infile_search.py --input [input file] --regex [regular expression] --name [name of results]
```

# Example
Let's imagine we have **test.txt** file with big text.
We want to find all **#.*#** strings in that file. We execute next command
```
./regex_infile_search.py -i test.txt -r #.*# -n test
```
And we get results in next files
```
Searching #.*# in /home/user/test.txt
Regex search finished successfully with results:
/home/user/test0.rgxprslt
/home/user/test1.rgxprslt
/home/user/test2.rgxprslt
/home/user/test3.rgxprslt
```

## License

**[MIT License](LICENSE)**

Copyright (c) 2019 [ltblueberry](https://github.com/ltblueberry)