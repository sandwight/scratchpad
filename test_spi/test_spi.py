import board
import busio
import digitalio


cs = digitalio.DigitalInOut(board.D8)
cs.direction = digitalio.Direction.OUTPUT
cs.value = True

spi = busio.SPI(board.SCK, MISO=board.MISO)