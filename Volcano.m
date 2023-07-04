clc;
clear;
clf;


%Para empezar programas de este tipo es de suma importancia tener estos
%comandos, porque le decimos a Matlab que reinicie los valores que
%anteriormente han sido evaluados. En especial cuando el usuario quiere
%poner sus datos.

%Este es un while para que el programa pueda ejecutarse sin ningun error,
%esto quiere decir que elimina todo margen de error posible. Si no es un
%valor correcto, lo pregunta las veces que asi sean necesarias.
def = input('Para utilizar variables definidas (ingresa 1), o para utilizar variables propias (ingresa 2): ');
while def < 1 || def > 2
    disp ("No se tomo ninguna decisión")
    def = input('Para utilizar variables definidas (ingresa 1), o para utilizar variables propias (ingresa 2): ');
end 


% Variables (variables definidas)
%Velocidad inicial 
v0 = 166.6;
%Altura inicial
y0 = 5426;
%angulo
angulo = 65;
%diametro
d = 0.32;
%Gravedad
g = 9.8;
%Coeficiente de arrastre
c = 0.45 * d^2;
v0x = v0.*cosd(angulo);
%La velocidad en x será absolutamente constante, esto debido a lo dirección
%de la trayectoría que se mantiene uniformemente proporcional.
v0y = v0.*sind(angulo);
%Esta velocidad inicial será de ayuda para poder sacar la velocidad final
%en "y" mediante la fórmula de ag = vfy-viy/t 
m = 230;


%Aqui ya entra la condicion dependiendo a lo que el usuario deseo, para 1
%ya unicamente se muestran los datos iniciales, y para dos se convierten en
%inputs que preguntan por los datos para continuar.
if def == 1 
    disp('Primer proyectil cuenta con fricción, segundo proyectil es ideal')
    disp('Variables definidas de acuerdo a la investigación:')
    disp('Velocidad inicial es = 166.6 m/s')
    disp('Altura inicial es = 5426 m')
    disp('Angulo de disparo = 65 º')
    disp('Diametro de la roca = 0.32 m')
    disp('Masa de la Roca= 230kg')
    disp('Coeficiente de Arrastre 0.45*d^2')
%se le pide al usuario que ponga las variables 
elseif def == 2
    c = input('Coeficiente de Arrastre (0.45-0.25): ' );
    v0 = input('Velocidad inicial (en m/s)(30m/s-170 m/s): ');
    angulo = input('Angulo de disparo(50°- 65°): ');
    d = input('Diámetro de la roca disparada por el volcán (en metros)(0.32m-0.07m): ');
    m = input('Masa de la Roca en g(150kg-700kg): ');
    c = c*d^2;

end 


%grafica del volcan
%Base
n = 10;
diametro = 400;
base = n * diametro;
figure(1);
%Lo limpia antes de graficarlo
clf;
%Funcion para graficar la base del volcan.
x = [0 ,(base/2) - (diametro/2), (base/2) + (diametro/2), base];
% Se obtiene tanto la base como la altura de este mismo.
y = [0 y0 y0 0];
%Al volcan se le otorga el formato necesario para que se muestre, esto
%debido a que la funcion patch es un poligono vacio, por eso se le asignan
%parametros, de la altura, de la base y el color.
patch(x,y,'Blue')

%Puntos entre la boca del volcan, para que se conozca la posicion del
%crater y saber de donde se lanzara el proyectil. Las dos gráficas saldrán
%del mismo punto
d1 = (base/2) - (diametro/2);
d2 = (base/2) + (diametro/2);

%Randomiza el punto de lanzamiento, para obtener graficas distintas, y que
%no siempre termine exactamente en el mismo punto.
x0 = randi([d1 d2]);

%Vectores

t0 = 0;
tf = 100;
dt = 0.01;
t = t0:dt:tf;
np = length(t);


vy = zeros(1, np);
vx = zeros(1, np);
y = zeros(1, np);
x = zeros(1, np);

%Valores iniciales
y(1) = y0;
vx(1) = v0x;
x(1) = x0;
vy(1) = v0y;



%Formula de Euler con fricción
%Se utiliza un for para iniciar Euler donde los argumentos inician en 1
%hasta el valor de las pocisiones de tiempo menos 1, y posteriormente hace
%el Euler tantas veces el for mantenga el loop.
for j = 1:np-1
    vx(j+1) = vx(j) + (dt * ((-c/m) * vx(j) * sqrt((vx(j)^2) + (vy(j)^2))));
    x(j+1) = x(j) + dt * vx(j);
    
    vy(j+1) = vy(j) + (dt * ((-c/m) * vy(j) * sqrt((vx(j)^2) + (vy(j)^2)) - g));
    y(j+1) = y(j) + dt * vy(j);
%El valor que arroja Euler, si llega a ser negativo, la funcion se volvera
%cero.
    if y(j+1) < 0
        y(j+1) = 0;
    end

end

%Figure(1) se necesita poner para que Matlab grafique en un cierto plano y
%no grafique fuera de este. Se le asigna un numero para distinguir la
%grafica a utilizar.
figure(1)
legend AutoUpdate off
legend('VOLCAN','Location','northwest','Orientation','vertical')
hold on
%Se utiliza este comando para que al usuario sepa que trayectoria es la que
%esta viendo.
text(3000,4000, "CON FRICCION")

comet(x,y);


%Formula de Euler sin fricción
%En esta formula de Euler se busca la trayectoria ideal, es decir
%unicamente se desprecia la friccion y el arrastre que produce el viento y
%consecuentemente la velocidad del objeto mas veloz, es decir llegara mas
%lejos debido a que no esta sufriendo las fuerzas resistivas mencionadas.
for j=1:np-1
    vx(j+1) = vx(j);
    x(j+1) = x(j) + dt * vx(j);

    vy(j+1) = vy(j) - dt * g;
    y(j+1) = y(j) + dt * vy(j);

    if y(j+1) < 0
        y(j+1) = 0;
        x(j+1) = x(j);
        
    end
    
end

%Se vuelve poner en figure(1) para que se muestre en la misma que con
%friccion.
figure(1)
hold on 
text(5000,4000, "SIN FRICCION")
comet(x,y);

%Label con sus parametros asignados, nos despliega una especie de titulo
%para cada eje.
xlabel('x');
ylabel('y');

%Estas dos funciones tambien son para darle formato a la grafica, una le
%agrega un titulo principal y la otra despliega cuadricula a la grafica.
title('Modelación Volcán');
grid on

