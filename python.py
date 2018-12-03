"""
Notes:

  http://www.learnpython.org/
      Numbers: integer:  myint = 7               float:   myfloat = 7.0  or myfloat = float(7)
                        print(myint)                      print(myfloat)
      Strings: mystring = 'hello' or "hello"   <- easy to use 
      assignment can be done on more than one variable "simultaneously" on the same line 
      mixed operations on numbers and strings are not supported 
      4 ** 2   # squred   2 ** 3  #cubed 
      lotsofhello = "hello" * 10
      lists can be joined with addition operators 
      form repeating sequence using the multiplication operator 
      format strings:  print("%s is %d years old!" %(v1, v2))
                      %s - String (or any object with a string representation, like numbers)
                      %d - Integers
                      %f - Floating point numbers
                      %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.
                      %x/%X - Integers in hex representation (lowercase/uppercase)
            data = ["john", "don", 53.44]
            format_string = "Hello %s %s. Your current balance is %s"
            print(format_string % data)
      basic string ops:  len(), s.count("l"), s.index("o"), [3:7], .[3:7:2]     [:7] start to 7, [2:] 2 to end, [::-1] reverse a string
                        upper(), lower(), .startwith(), .endwith(), .split()
      boolean ops: in op: is op: (not value but variable themselves) not op: 
      for loop   can use elif; while loop 
      functions: def function_name(arg1,arg2)
      classes and objects 
      dictionaries: dics = {} dics["one"] = 1 dics["two"] = 2 dics["three"] = 3 or dics = {"one":1, "two":2, "three":3}
            iterate through dics: for name, value in dics.items():
            remove a value: del dics["one"] or .pop("one")
      modules and packages: build-in modules: urllib
        extending module load path: 1. pythonpath=/foo python game.py 2. sys.path.append("/foo") 
        We can look for which functions are implemented in each module by using the dir function:
          import urllib
          dir(urllib)
        write packages: basically directories, must contain _init_.py inside 
      Numpy array: import numpy as np           np.array(list)
        element wise calculations 
        subsetting 
      Pandas Basics 
        indexing DataFrames: []   or [[]]
      list comprehension: create a new list based on a list in a single line of code 
      multiple argument function: * and ** kwargs, order not important
                            kwargs["key"] == value 
      except
      set:  ()   aset.intersect(bset), aset.difference(bset), aset.union(bset), symmetric_difference
      Serialization: import json, json.dump() (into json), json.load(string) (load into json data structure)
      ??generator: 
      ??decorator:
      ??closures:
    https://pythonprogramming.net/introduction-to-python-programming/
    https://pythonprogramming.net/introduction-intermediate-python-tutorial/
      String:   " ".join("hi there", listElement)
                os.path.join( , )
                string format:  who = 'Gary'
                                how_many = '12
                                print('{} bought {} apples today'.format(who, how_many))
      argparse:
            import argparse
            import sys

            def main():
                parser = argparse.ArgumentParser()
                parser.add_argument('--x', type=float, default=1.0,
                                    help='What is the first number?')
                parser.add_argument('--y', type=float, default=1.0,
                                    help='What is the second number?')
                parser.add_argument('--operation', type=str, default='add',
                                    help='What operation? Can choose add, sub, mul, or div')
                args = parser.parse_args()
                sys.stdout.write(str(calc(args)))
                
            def calc(args):
                if args.operation == 'add':
                    return args.x + args.y
                elif args.operation == 'sub':
                    return args.x - args.y
                elif args.operation == 'mul':
                    return args.x * args.y
                elif args.operation == 'div':
                    return args.x / args.y

            if __name__ == '__main__':
                main()
            python argparse_example.py --x=5 --y=3 --operation=mul
            python argparse_example.py -h
    list comprehension and generator 
    enumerate
 """
