# Name: basic magery trainer
# Description: you need FC2/FCR6
# Author: I'm Papang
# Era: TOL/OSI

def trainMagery():
	mageReal = Skill('Magery')
	mageCap = SkillCap('Magery')
	
	if Mana('self') < 25:
		medit()
	if mageReal >= 0 and mageReal < 34:
		Cast('Bless', 'self')
	elif mageReal >= 34 and mageReal < 45:
		Cast('Greater Heal', 'self')
	elif mageReal >= 45 and mageReal < 67:
		Cast('Magic Reflection')
		Pause(2000)
	elif mageReal >= 67 and mageReal < 82:
		Cast('Invisibility', 'self')
	elif mageReal >= 82 and mageReal < 95:
		Cast('Mass Dispel', 'self')
	else:
		if mageReal >= 95 and mageReal < mageCap:
			if Mana('self') < 40:
				medit()
			Cast('Earthquake')
			Pause(3000)
		else:
			Stop()
	
def medit():
	CancelTarget()
	while Mana('self') < MaxMana('self'):
		if not BuffExists('Active Meditation'):
			UseSkill('Meditation')
			Pause(1000)
		Pause(100)

while not Dead('self'):
	trainMagery()
	Pause(250)
