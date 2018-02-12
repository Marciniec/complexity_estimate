In order to run program you need to install package using:
```
pip install git+https://github.com/Marciniec/complexity_estimate
```
In order to determine complexity of your program you need make new class that inherits from _Basic_ class and implement methods:
 * \__init__   -declare all variables you'll need in your program

* set_up(self, l): - set up your program and this won't be taken into account during complexity mesurement, takes size of the problem as parameter

* function(self): - write code you want to be measured

* cleaning(self): -write code to clean up after _function_

example code:
```
from complexitymeasureproject import Basic


class i_do(Basic):
    def __init__(self):
        super().__init__()
        self.l = 0

    def set_up(self, l):
        self.l = l

    def function(self):
        for i in range(0, self.l):
            x = 2 * 5 + i

    def cleaning(self):
        pass

```
Then you can use:
* predict_elements(package.module.class,time,timeout) -shows complexity and returns aproximated number of elements computed in time
* predict_time(package.module.class,time,timeout) -shows complexity and returns aproximated time to compute
* show_complexity(package.module.class,timeout) - shows complexity
Where timeout - max time of measuring program default - 30s

Example usage:
```
from complexitymeasureproject import main

f = main.predict_elements('okidoki.i_do',10)
x = main.predict_time('okidoki.i_do',10)
main.show_complexity('okidoki.i_do')

```
