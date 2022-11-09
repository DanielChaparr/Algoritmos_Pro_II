a=int(1)
b=int(0)



print("Tablas de la verdad")

print("Tabla de verdad de y")
print(str(a==a)+ " and " +str(a==a)+ "-->" +str(a==a))
print(str(a==a)+ " and " +str(a==b)+ "-->" +str(a==b))
print(str(a==b)+ " and " +str(a==a)+ "-->" +str(a==b))
print(str(a==b)+ " and " +str(a==b)+ "-->" +str(a==b))

print("------------------------------------------------------------------------------------")

print("tabla de la verdad de o")
print(str(a==a)+ " or " +str(a==a)+ "-->" +str(a==a))
print(str(a==a)+ " or " +str(a==b)+ "-->" +str(a==a))
print(str(a==b)+ " or " +str(a==a)+ "-->" +str(a==a))
print(str(a==b)+ " or " +str(a==b)+ "-->" +str(a==b))

print("------------------------------------------------------------------------------------")

print("Tabla de si-entonces")
print(str(a==a)+ " then " +str(a==a)+ "-->" +str(a==a))
print(str(a==a)+ " then " +str(a==b)+ "-->" +str(a==b))
print(str(a==b)+ " then " +str(a==a)+ "-->" +str(a==a))
print(str(a==b)+ " then " +str(a==b)+ "-->" +str(a==a))

print("------------------------------------------------------------------------------------")

print("Tabla de la verdad ´si y solo si´")
print(str(a==a)+ " only if " +str(a==a)+ "-->" +str(a==a))
print(str(a==a)+ " only if " +str(a==b)+ "-->" +str(a==b))
print(str(a==b)+ " only if " +str(a==a)+ "-->" +str(a==b))
print(str(a==b)+ " only if " +str(a==b)+ "-->" +str(a==a))

print("------------------------------------------------------------------------------------")

print("Tabla de la verdad o-o")
print(str(a==a)+ " or " +str(a==a)+ "-->" +str(a==b))
print(str(a==a)+ " or " +str(a==b)+ "-->" +str(a==a))
print(str(a==b)+ " or " +str(a==a)+ "-->" +str(a==a))
print(str(a==b)+ " or " +str(a==b)+ "-->" +str(a==b))


