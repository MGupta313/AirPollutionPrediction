# AQI Calculation is derived from:
# https://www.kaggle.com/anbarivan/indian-air-quality-analysis-prediction-using-ml


class AQI():

    def _calculate_si(self, so2):
        '''
        Function to calculate so2 individual pollutant index(si)
        '''
        si = 0
        if (so2 <= 40):
            si = so2*(50/40)
        if (so2 > 40 and so2 <= 80):
            si = 50+(so2-40)*(50/40)
        if (so2 > 80 and so2 <= 380):
            si = 100+(so2-80)*(100/300)
        if (so2 > 380 and so2 <= 800):
            si = 200+(so2-380)*(100/800)
        if (so2 > 800 and so2 <= 1600):
            si = 300+(so2-800)*(100/800)
        if (so2 > 1600):
            si = 400+(so2-1600)*(100/800)
        return si

    def _calculate_ni(self, no2):
        '''
        Function to calculate no2 individual pollutant index(ni)
        '''
        ni = 0
        if(no2 <= 40):
            ni = no2*50/40
        elif(no2 > 40 and no2 <= 80):
            ni = 50+(no2-14)*(50/40)
        elif(no2 > 80 and no2 <= 180):
            ni = 100+(no2-80)*(100/100)
        elif(no2 > 180 and no2 <= 280):
            ni = 200+(no2-180)*(100/100)
        elif(no2 > 280 and no2 <= 400):
            ni = 300+(no2-280)*(100/120)
        else:
            ni = 400+(no2-400)*(100/120)
        return ni

    def _calculate_rpi(self, rspm):
        '''
        Function to calculate no2 individual pollutant index(rpi).
        Many data values of spm values is unawailable since it was not measure before.
        '''
        rpi = 0
        if(rspm <= 30):
            rpi = rpi*50/30
        elif(rspm > 30 and rspm <= 60):
            rpi = 50+(rpi-30)*50/30
        elif(rspm > 60 and rspm <= 90):
            rpi = 100+(rpi-60)*100/30
        elif(rspm > 90 and rspm <= 120):
            rpi = 200+(rpi-90)*100/30
        elif(rspm > 120 and rspm <= 250):
            rpi = 300+(rpi-120)*(100/130)
        else:
            rpi = 400+(rpi-250)*(100/130)
        return rpi

    def _calculate_spi(self, spm):
        '''
        Function to calculate no2 individual pollutant index(spi)
        Many data values of rspm values is unawailable since it was not measure before.
        '''
        spi = 0
        if(spm <= 50):
            spi = spm
        if(spm < 50 and spm <= 100):
            spi = spm
        elif(spm > 100 and spm <= 250):
            spi = 100+(spm-100)*(100/150)
        elif(spm > 250 and spm <= 350):
            spi = 200+(spm-250)
        elif(spm > 350 and spm <= 450):
            spi = 300+(spm-350)*(100/80)
        else:
            spi = 400+(spm-430)*(100/80)
        return spi

    def _calculate_aqi(self, si, ni, spi, rpi):
        '''
        calculate the air quality index (AQI). Its is calculated as per indian govt standards.
        '''
        aqi = 0
        if(si > ni and si > spi and si > rpi):
            aqi = si
        if(spi > si and spi > ni and spi > rpi):
            aqi = spi
        if(ni > si and ni > spi and ni > rpi):
            aqi = ni
        if(rpi > si and rpi > ni and rpi > spi):
            aqi = rpi
        return aqi

    def calculate_aqi(self, so2, no2, spm, rspm):
        # Calculate individual components
        si = self._calculate_si(so2)
        ni = self._calculate_ni(no2)
        rpi = self._calculate_rpi(rspm)
        spi = self._calculate_spi(spm)

        aqi = self._calculate_aqi(si, ni, spi, rpi)

        return aqi
