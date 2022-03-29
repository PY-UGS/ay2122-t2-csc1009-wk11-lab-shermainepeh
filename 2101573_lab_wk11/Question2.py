class ClockTime:
    # Constructor
    def __init__(self):
        # Set hours, minutes and seconds to 0
        self.hours = 0
        self.minutes = 0
        self.seconds = 0

    # Method to assign hrs to self.hours
    def setHours(self, hrs):
        self.hours = hrs

    # Method to assign mins to self.minutes
    def setMinutes(self, mins):
        self.minutes = mins

    # Method to assign secs to self.seconds
    def setSeconds(self, secs):
        self.seconds = secs

    # Method to assign time to self accordingly
    def setTime(self, hrs, mins, secs):
        self.hours = hrs
        self.minutes = mins
        self.seconds = secs

    # Method to show time using print statement
    def showTime(self):
        # display the time in the format of hours:minutes:seconds
        print("Time: {:02d}:{:02d}:{:02d}".format(self.hours, self.minutes, self.seconds))


# Main method
if __name__ == '__main__':
    # Create ClockTime object
    ct = ClockTime()

    # User to input hours, minutes and seconds
    # Check inputs using if-else
    hrs = int(input("Enter hours: "))
    if hrs < 0 or hrs > 23:
        print("Invalid hours")
    else:
        mins = int(input("Enter minutes: "))
        if mins < 0 or mins > 59:
            print("Invalid minutes")
        else:
            secs = int(input("Enter seconds: "))
            if secs < 0 or secs > 59:
                print("Invalid seconds")
            else:
                # Assign user inputs to setTime method
                ct.setTime(hrs, mins, secs)
                # Display time
                ct.showTime()
