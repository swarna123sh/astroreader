import pyaztro
sign=input("Enter your sun sign:")
horoscope = pyaztro.Aztro(sign.lower())

print("Your horoscope for today: \n",horoscope.description)
print("Your mood today: \n",horoscope.mood)
print("Sun signs that you are compatible with: \n",horoscope.compatibility)
print("Your lucky number: \n",horoscope.lucky_number)
print("Your lucky color: \n",horoscope.color)
