# Import writer class from csv module
from csv import writer
import datetime

class EventMgr:
    def __init__(self, filename):
        self.filename = filename

    def writeDefault(self, mlist):
        # Open our existing CSV file in append mode
        # Create a file object for this file
        tm = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S,%f")
        mlist.insert(0, tm)
        with open(self.filename, 'a', newline='') as f_object:
        
            # Pass this file object to csv.writer()
            # and get a writer object
            writer_object = writer(f_object)
        
            # Pass the list as an argument into
            # the writerow()
            writer_object.writerow(mlist)
        
            # Close the file object
            f_object.close()

    def writeCustom(self, mlist):
        # Open our existing CSV file in append mode
        # Create a file object for this file
        #tm = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S,%f")
        #mlist.insert(0, tm)
        with open(self.filename, 'a', newline='') as f_object:
        
            # Pass this file object to csv.writer()
            # and get a writer object
            writer_object = writer(f_object)
        
            # Pass the list as an argument into
            # the writerow()
            writer_object.writerow(mlist)
        
            # Close the file object
            f_object.close()
 
# List that we want to add as a new row
_mgr = EventMgr("data/test.csv")
_mgr.writeCustom(['getTotalNLA', 2.34])