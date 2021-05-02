# take-home-test-alalv

This repo contains my solution to the prefix and infix calculator take home test. It can be run in the command line or as a flask app.
It is currently running in Heroku in this url:

https://take-home-test-alalv.herokuapp.com/

### Requirements

The code uses Python version 3.9.1.
To run it in the command line or to run the tests no additional dependencies are needed.
To run it as a flask app, flask is needed.
To deploy it in Heroku, gunicorn and flask are needed.

### Tests

Some basic test cases are included in *test_calculator.py*, and can be run with the following comand:

```
python test_calculator.py -v
```

### CLI

To run it in the command line use:

```
python calculator.py
```
It will execute an infite loop that computes the input as an expression in either prefix or infix format.
```
Current reading format is Infix, to change enter Prefix
Enter input:
> ( 1 + ( 2 * 3 ) )
7
Current reading format is Infix, to change enter Prefix
Enter input:
 > ( 2 / 2 )
 1
 ```
 The format can be changed by entering the desired format:
 ```
 Current reading format is Infix, to change enter Prefix
Enter input:
>Prefix
Current reading format is Prefix, to change enter Infix
Enter input:
> + 1 * 2 3
7
Current reading format is Prefix, to change enter Infix
Enter input:
```

### Implementation

The code uses a recursive solution, which means that for a large enough input (approx 2000 operations) max recursion depth will be reached. 
