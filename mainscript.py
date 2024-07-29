import ocr_mod
import glob
import os
import time
import decision_meter


#Open set .txt file for meta data.
txt = open('result.txt', 'a')

# time2 buffer used for calculating deltatime
t2 = time.time()

# operating time for each loop
# adjust accordingly
sleepgap :float = 0.2

# calling necessary objects
ocr = ocr_mod.OcrMain()
meter = decision_meter.Dmeter()

# buffer_path used for conditional statement
buffer_path = 'not possible'

# see decision_meter docs.
meter.new() # initial new

# 👇 this is to set the delta time maximum.
# after this amount of seconds passed and ocr results are different,
# it creates new batch for the decision_meter algorithm.
maximum_t = 3.5 # seconds

# buffer and not, this will be sent to decision_meter to calculate, see decision_meter docs.
sent_to_dmeter = 'this is not buffer'
buffer_sent_to_dmeter = 'this is buffer'


plate_id = 0
while True:
    
    # used for result.txt
    curr_time_exact = time.ctime()
    
    # compiles files into 'glob'
    list_of_files = glob.glob('resultsimg\*') 
    
    # find the most recent file
    ocr.path = max(list_of_files, key=os.path.getctime)
    # create ocr results from path
    ocr.make()    
    result = ocr.result


    def getText(res):
    # method for getting the first line of chars from OCR
        result = res
        result = result[0]
        try:
            return [res[1] for res in result]
        except Exception as e:
            return [[None]]    
    
    
    # calculating distance between current time and last OCR result recorded.
    t1 = time.time()
    deltat = t1-t2

    print('time',deltat)
    print(f"b to dmeter {buffer_sent_to_dmeter} || d meter {sent_to_dmeter} ")
    
    # getting result to be calculated.
    sent_to_dmeter = getText(result)[0][0]
    
    # if new OCR reading and more than maximum time
    if deltat > maximum_t:
        if sent_to_dmeter != buffer_sent_to_dmeter:
            print('>4')
            t2 = time.time()
            # create new batch
            meter.new()
            plate_id += 1
            # write to result.txt
            txt.write(f'---\n{curr_time_exact}\n{meter.best}\n{ocr.path}\n')
            
    # if there are new in-coming OCRs from different images
    if deltat < maximum_t:
        if ocr.path != buffer_path:
            print('<4')
            # adds to the batch
            meter.add(sent_to_dmeter)
            print(f"INSIDE b to dmeter {buffer_sent_to_dmeter} || d meter {sent_to_dmeter} ")
        
    
    # buffers
    buffer_sent_to_dmeter = sent_to_dmeter
    buffer_path = ocr.path  
    
    print(meter.batch)
    
    # calculation in decision_meter.py, see docs.
    meter.calculate()
    
    print(f'BEST RESULT: {meter.best}')
    print(f'PLATE ID: #{plate_id}\n') 
    
    # operating time per loop
    time.sleep(sleepgap)