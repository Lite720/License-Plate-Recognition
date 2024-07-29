import ocr_mod
import glob
import os
import time
import decision_meter

# txt file
txt = open('result.txt', 'a')

t2 = time.time()
ocr = ocr_mod.OcrMain()
meter = decision_meter.Dmeter()

buffer_path = 'not possible'
meter.new() # initial new
maximum_t = 3.5 # seconds
sent_to_dmeter = 'this is not buffer'
buffer_sent_to_dmeter = 'this is buffer'

plate_id = 0
while True:
    curr_time_exact = time.ctime()
    list_of_files = glob.glob('resultsimg\*') # * means all if need specific format then *.csv
    ocr.path = max(list_of_files, key=os.path.getctime)
    ocr.make()
    
    result = ocr.result

    def getText(res):
        result = res
        result = result[0]
        try:
            return [res[1] for res in result]
        except Exception as e:
            return [[None]]    
    
    t1 = time.time()
    
    deltat = t1-t2

    print('time',deltat)
    print(f"b to dmeter {buffer_sent_to_dmeter} || d meter {sent_to_dmeter} ")
    ## Dmeter part 👇
    sent_to_dmeter = getText(result)[0][0]
    
    if deltat >maximum_t:
        if sent_to_dmeter != buffer_sent_to_dmeter:
            print('>4')
            t2 = time.time()
            meter.new()
            plate_id += 1
            txt.write(f'---\n{curr_time_exact}\n{meter.best}\n{ocr.path}\n')
            
    if deltat <maximum_t:
        if ocr.path != buffer_path:
            print('<4')
            meter.add(sent_to_dmeter)
            print(f"INSIDE b to dmeter {buffer_sent_to_dmeter} || d meter {sent_to_dmeter} ")
        
    buffer_sent_to_dmeter = sent_to_dmeter

    buffer_path = ocr.path  
    
    print(meter.batch)
    
    meter.calculate()
    
    print('best', meter.best)
    print(f'PLATE NUMBER: #{plate_id}') 
    print('')
    time.sleep(0.2)