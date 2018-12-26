'''In object-oriented programming, the command pattern is a design pattern in which an object is used to reresent and encapsulate all the information needed to call a method at a later time. This information includes the method name, the object that owns the method and values for the method parameters.'''
'''Command pattern is associated with three components, the client, the invoker, and the reciver : 
    - Client - the client represents the one that    
      instantiates the encapsulated object
    - Invoker - the invoker is responsible for deciding when 
      the method is to be invoked or called
    - Receiver - the receiver is that part of the code that 
      contains the instructions to execute when a 
      corresponding command is given '''

class Switch:
    '''the INVOKER class'''

    def __init__(self, flip_up_cmd, flip_down_cmd):
        self.__flip_up_cmd = flip_up_cmd
        self.__flip_down_cmd = flip_down_cmd


    def flip_up(self):
        self.__flip_up_cmd.execute()

    def flip_down(self):
        self.__flip_down_cmd.execute()

class Light:
    '''The receiver class'''

    def turn_on(self):
        print('The light is on')

    def turn_off(self):
        print('The light is off')


class Command:
    '''The command abstract class '''
    def __init__(self):
        pass

    def execute(self):
        pass


class FlipUpCommand(Command):
    def __init__(self, light):
        self.__light = light

    def execute(self):
        self.__light.turn_on()


class FlipDownCommand(Command):
    def __init__(self, light):
        Command.__init__(self)
        self.__light = light

    def execute(self):
        self.__light.turn_off()


class LightSwitch:
    'The client class'

    def __init__(self):
        self.__lamp = Light()
        self.__switch_up = FlipUpCommand(self.__lamp)
        self.__switch_down = FlipDownCommand(self.__lamp)
        self.__switch = Switch(self.__switch_up,self.__switch_down)

    def switch(self, cmd):
        cmd = cmd.strip().upper()
        try:
            if cmd =='ON':
                self.__switch.flip_up()
            elif cmd == "OFF":
                self.__switch.flip_down()
            else:
                print('Argument "ON" or "OFF" is required.')
        except Exception as msg:
            print('Exception occured : '+ msg)


if __name__ == "__main__":
    light_switch = LightSwitch()

    print("Switch ON test")
    light_switch.switch("ON")

    print("Switch OFF test")
    light_switch.switch("OFF")

    print("Invalid Command test")
    light_switch.switch("*****")