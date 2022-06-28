
#Primero se importan los datos y se le asignan a una variable que en este caso 
# llamaremos data 1 

data1 <- read.csv(file.choose(), header= T)

#Se revizan los datos para comprobar que se hayan importado correctamente
# Para esto se visualiza la estructura de los datos con las siguientes funciones

head(data1)
names(data1)
View(data1)

# Posteriormente se crea una nueva variable, la cual va a estar asociada con la regresión
# y lugo se presenta los resultados de dicha regresión con la función summary()

regla_taylor <- lm(Tr ~ Bi + Bd + BA + Bp + ST, data1)
summary(regla_taylor)



#Ver correlaciones de forma gráfica 
pairs(data1[2:6]) 
plot(regla_taylor)

# Distribución t
plot( function(x) dt( x, df = 5 ), -5, 5, ylim = c( 0, 0.4 ),
      col = "blue", type = "l", lwd = 2 )






