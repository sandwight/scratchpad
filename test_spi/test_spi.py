import board
import busio
import digitalio


cs = digitalio.DigitalInOut(board.CS)
cs.direction = digitalio.Direction.OUTPUT
cs.value = True

spi = busio.SPI(board.SCK, MISO=board.MISO)