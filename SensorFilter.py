'''MIT License

Copyright (c) 2020 Kankan Kumar Sarkar

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''
class KalmanFilter():
    def __init__(self,InitialEstimate=0,SensorError=0,debug=0):
        self.KG=0 # Kalman Gain between 0<=KG<=1
        self.Eest=2 # Error in the Estimate, to be calcuated
        self.Estimate = 0  # Error in the Estimate, to be calcuated
        self.Emea=SensorError # Error in the Measurement ,Look in the datasheet of the sensor for the error
        self.PrevEstimate=InitialEstimate # Previous Estimate
        # self.RawSensorReading=0 # Sensor Reading
        self.debug=debug # Duh Its the debug flag
    def Predict(self,RawsensorReading=0):
        self.Estimate=self.PrevEstimate+self.KG*(float(RawsensorReading)-self.PrevEstimate)
        if self.debug:
            print("Predicted Sensor Value=", self.Estimate)
        return self.Estimate
    def CalculateGain(self):
        self.KG=float(self.Eest/(self.Emea+self.Eest))
        if self.debug:
            print("Kalman Gain=",self.KG)
    def ErrorEstimate(self):
        return (1-self.KG)*self.Eest
    def Run(self,RawSensorData=0):
        self.CalculateGain()
        self.PrevEstimate=self.Predict(RawSensorData)
        self.Eest=self.ErrorEstimate()
        if self.debug:
            print("Error In the Estimate=",self.Eest)
        return self.PrevEstimate
    def GetSensorReading(self):
        return self.PrevEstimate


'Test KalmanFilter'
# # Initializing with a intial Estimate and the sensor error ,
# # if you are not sure of the intial error you can set to zero
# # and the sensor error can be retrieved from the senosr datasheet
# sens1=KalmanFilter(68,4,1)
# #Push the First SensorReading
# sens1.Run(75)
# #Push the Second SensorReading
# sens1.Run(71)
# #Push the Third SensorReading
# sens1.Run(70)