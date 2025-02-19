from PyLTSpice import  RawRead

volts = []

for n in range(1, 100):

        raw = RawRead('data/test'+str(n) +'.raw')


        steps = raw.get_steps()

        vout = raw.get_trace('V(out)').get_wave()
        output = max(vout)
        volts.append(output)
        

print('Max voltage of: ' + str(max(volts)))
print('Achieved at: ' + str(volts.index(max(volts))) + '% duty cycle')
print('done')
