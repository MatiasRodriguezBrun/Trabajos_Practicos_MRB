bio = open("bio.txt","w")
bio.write("Me llamo Matias, tengo 19 anos y estoy estudiando N.D. \n")
bio.write("Por otro lado, me gusta mucho el deporte, ppalmente el futbol\n")
print (bio)

bio = open ("bio.txt","r")
bio.read()
bio.readlines()

bio.close()

