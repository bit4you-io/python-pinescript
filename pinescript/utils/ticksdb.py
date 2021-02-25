from struct import *
MAX_RECORS_PER_FILE = 322638

class Tick:
	def __init__(self, raw):
		self.time  		  = unpack('<I', raw[:4])[0]
		self.open  		  = unpack('<Q', raw[4:12])[0] / 100000000
		self.close 		  = unpack('<Q', raw[12:20])[0] / 100000000
		self.low 		  = unpack('<Q', raw[20:28])[0] / 100000000
		self.high 		  = unpack('<Q', raw[28:36])[0] / 100000000
		self.volume 	  = unpack('<Q', raw[36:44])[0] / 100000000
		self.marketVolume = unpack('<Q', raw[44:52])[0] / 100000000

	def __str__(self):
		return str(self.time) + " open=" + str(self.open) + " close=" + str(self.close) + " low=" + str(self.low) + " high=" + str(self.high) + " volume=" + str(self.volume) + " marketVolume=" + str(self.marketVolume)

class TicksDB:
	def __init__(self, iso, interval=1):
		self.interval  = interval*60
		self.path      = "data/" + iso  + "/" + str(int(interval)) + "/"
		self.openFiles = {}

		cursor = open(self.path + 'cursor.bin', 'rb')
		self.start = unpack('<I', cursor.read(4))[0]
		self.end = unpack('<I', cursor.read(4))[0]
		cursor.close()

	def close(self):
		for f in self.openFiles:
			self.openFiles[f].close()

		self.openFiles = {}

	def __len__(self):
		if self.start == 0:
			return 0

		return int((self.end - self.start) / self.interval)

	def __getitem__(self, offset):
		return self.get(self.start + (offset * self.interval))

	def has(self, time):
		return time % self.interval == 0 and time >= self.start and time <= self.end and time > 0

	def get(self, from_unix, to = None):
		if to == None:
			data = self.file(from_unix).read(52)
			return Tick(data)

		if self.start == 0:
			return []
		if from_unix < self.start:
			from_unix = self.start
		elif from_unix % self.interval != 0:
			from_unix = from_unix + self.interval - (from_unix % self.interval)

		if to > self.end:
			to = self.end
		elif to % self.interval != 0:
			to = to - (to % self.interval)

		if to < from_unix:
			return []

		f = self.file(from_unix)
		res = []
		ri = 0
		current = from_unix
	
		while current < to:
			if current > from_unix and ((current - self.start) / self.interval) % MAX_RECORS_PER_FILE == 0:
				f = self.file(current)

			readableRecords = MAX_RECORS_PER_FILE - (((current - self.start) / self.interval) % MAX_RECORS_PER_FILE)
			if current + (readableRecords * self.interval) > to:
				readableRecords = ((to - current) / self.interval) + 1

			if readableRecords == 0:
				break

			b1 = f.read(int(readableRecords * 52))
			for i in range(0, int(readableRecords)):
				if i*52 >= len(b1):
					break

				res.append(Tick(b1[i*52:(i+1)*52]))

			current += (readableRecords * self.interval)

		return res

	def file(self, time):
		if time % self.interval != 0 or time < self.start or time > self.end:
			raise NameError('Wrong time required')

		index = 1
		if self.start != 0:
			index = ((time - self.start) / self.interval)
			index = int(((index - (index % MAX_RECORS_PER_FILE)) / MAX_RECORS_PER_FILE) + 1)

		if index not in self.openFiles:
			self.openFiles[index] = open(self.path + str(index) + ".bin", "rb")

		f = self.openFiles[index]
		if self.start != 0:
			pos = int((((time - self.start) / self.interval) - ((index-1) * MAX_RECORS_PER_FILE)) * 52)
			f.seek(pos, 0)

		return f

# p1 = TicksDB("USDT-BTC")
# print("DB opened", p1.count())

# # for tick in p1.getTicks(1577836800, 1577836800 + 240):
# # 	print( tick.time, tick.open, tick.close )

# t = p1.get(1602232140)
# print(t.time, t.open, t.time == 1602232140)
# p1.close()
