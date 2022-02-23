# pelican = open("pelican.txt","x")
# pelican.close()
# TODO: Ask Martina do you have to do the above first to ensure it's safe to open file? Do you need w mode if working in a mode?
# Is Pelican the file handle? so it's a variable for an open file?
pelican = open("pelican.txt", "w")
pelican.write("A wonderful bird is the Pelican.\n")
pelican.write("His bill holds more than his belican.\n")
limerickList=["He can take in his beak,\n", "Enough food for a week,\n", "But I'm damned if I see how the helican.\n"]
pelican.writelines(limerickList)
pelican.close()
#\n is required because writelines() does not include line breaks


