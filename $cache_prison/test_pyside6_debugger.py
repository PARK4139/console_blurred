import inspect
import sys
import time

from pkg_park4139 import Park4139

class debugger:
    def __init__(self):
        Park4139.commentize('print(self.__name__+" is initialized")')
        print(self.__name__+" is initialized")
        Park4139.commentize('super().__init__()')
        super().__init__()


    def print_built_in_info(thing_curious):
        Park4139.commentize(f"{inspect.currentframe().f_code.co_name} {str(thing_curious.__code__.co_varnames)}")
        print("_______________________________________________________________ " + str() + "("+str(thing_curious)+") s")
        Park4139.commentize("print(inspect.getsource(thing_curious))")
        print(inspect.getsource(thing_curious))
        Park4139.commentize("for i in inspect.getmembers(thing_curious_):")
        for i in inspect.getmembers(thing_curious):
            print(i)
        Park4139.commentize("print(help(thing_curious))")
        print(help(thing_curious))
        Park4139.commentize("[x for x in dir(thing_curious) if '__' not in x]")
        [x for x in dir(thing_curious) if '__' not in x]
        # dir() 함수는 값 없이 지정된 객체의 모든 속성과 메서드를 반환합니다 .
        # 이 함수는 모든 속성과 메서드를 반환하며, 모든 개체에 대한 기본값인 내장 속성도 반환합니다.
        Park4139.commentize("[x for x in dir(thing_curious) if '__' not in x]")



    def print_function_info(thing_curious):
        Park4139.commentize(f"{inspect.currentframe().f_code.co_name} {str(thing_curious.__code__.co_varnames)}")
        print(help(thing_curious))
        Park4139.debug_as_cli(f'# of the Arguments : {thing_curious.__code__.co_argcount}')
        # park4139.debug_as_cli(f'Name of the Arguments : {thing_curious.__code__.co_varnames}')
        print("┌>print via getsource s")
        print(inspect.getsource(thing_curious))
        print("└>print via getsource e")

    @staticmethod
    def print_event_info_(event, thing_curious):
        """
            jhp_debugger.print_event_info_(event)
            # └>call sample
        """
        print(f"_______________________________________________________________ {inspect.currentframe().f_code.co_name}        ")
        print(str(event))
        # print(event.type())
        # if type(thing_curious)==str:
        #     print('{{mkr}}')
        # if type(thing_curious)==list:
        #     print(thing_curious[str(event.type())])
        # if type(thing_curious) == tuple:
        #     print('{{mkr}}')
        print(f"_______________________________________________________________ {inspect.currentframe().f_code.co_name}        ")


