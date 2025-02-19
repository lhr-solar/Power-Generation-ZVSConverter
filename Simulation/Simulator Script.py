from PyLTSpice import SimRunner, SpiceEditor, LTspice, RawRead
import pygame

runner = SimRunner(simulator = LTspice)

for i in range(1, 100):

        
    net = SpiceEditor("Working ZVS Converter.net")
    net.set_component_value('L1','10u')
    net.set_element_model('V3', 'PULSE(0 12 1n 1n ' + str(1000*(i/100)) + 'n 1000n)')
    net.set_element_model('V2', 'PULSE 0 12 1n 1n ' + str((1000*(i/100))/2) + 'n 1000n)')
    log = runner.run_now(net, run_filename='data/test'+str(i))
    print('Test ' + str(i))



pygame.mixer.init()
pygame.mixer.music.load("you-digging-in-me.mp3")
pygame.mixer.music.play()
print('done')
    
