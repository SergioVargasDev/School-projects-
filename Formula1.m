%%Rodrigo Morales Guillaux A00835678
%%Fernando Daniel Rentería Saldaña A00836509
%%Sergio Tomás Vargas Villarreal A00837196
%%Emilio Vidal Cavazos Páez A00835995

%Leyes de la Conservación

%1/12/2022

%% Valores a utilizar : 
g = 9.8;
friccionS = 0.523;
friccionC = 0.8
%% Gráfica de la pista 

%Aquí se nos estipularon las primeras dos coordenadas coordenadas.
%Posteriormente agregamos otras dos coordenadas dentro del rango de las
%primeras dos coordenadas estipuldas
% (10,170)-(280,20)-(50,180)-(220,10)

%Sustituímos los valores de las coordenadas de x en la función polinomial.
%Dicho estará dentro de una matriz A. 
A = [10.^3 10.^2 10 1;
     280.^3 280.^2 280 1;
     50.^3 50.^2 50 1;
     220.^3 220.^2 220 1];
%Aquí la matriz y tendrá los valores de la variable dependiente y, donde
%será el resultado de la sustitución de x en la función polinomial.
y = [170; 20; 180; 10];

% x se establecerá como el producto de la matriz de A y la matriz de y.

x = inv(A)*y;

% Posterior a dicho se le asignará a dicha variable el nombre de
% coeficiente.

coef = x

%La función "yf" servirá para encontrar la curva de la pista. 
% Aquí sólo será de sustituir el valor del coeficiente en la función
%polinomial cúbica. 
yf = @(z) coef(1).*z.^3+coef(2).*z.^2+coef(3).*z+coef(4);
%Se deriva la función polinomial cúbica para encontrar el radio de
%curvatura..
dyf = @(x) (coef(1)*3.*x.^2+coef(2)*2.*x+coef(3));
%La variable zv sirve para estipular los margenes de las líneas en el
%espacio para la hoja de cuadrícula.
zv = linspace(10,290,100);


plot(zv,yf(zv), 'LineWidth', 12, 'Color','black')
hold on



%% Zona de curvas 
%18.7, 50.5
%233.3, 265.2

%Se obtendra el radio de curvatura mediante la siguiente función. 
dp = @(x) ((1+(coef(1)*3.*x.^2+coef(2)*2.*x+coef(3)).^2).^(3/2))./abs(coef(1)*6.*x+2*coef(2)); % 18,7-50.5 233.3-265.2
%Para obtener la longitud utilizamos la siguiente función
d1 = @(x)sqrt(((1+(coef(1)*3.*x.^2+coef(2)*2.*x+coef(3)).^2)));

int1 = integral(d1, 10, 280)

% se hace un circulo que esta en el centro de la curva y en la linea
centers = [39 143]; % se crea una variable la cual indica el centro del circulo 
radii = 39; % el raidio del circulo


% aqui abajo se hace lo mismo pero para la otra curva
%center2 = [245 42];
%randii2 = 39;
%viscircles(center2, randii2)
%%  Zona de derrape 
vxradio1=[];
vxradio2=[];

%se crea la condicional que si es que es mayor de 50 y de 145 se resalta
%verde 
for i=zv
    if dp(i)<50
        if i<145
            vxradio1=[vxradio1 i];
        else
            vxradio2=[vxradio2 i];
        end
    end
end

%se resalta verde la zona de derrape
plot(vxradio1,yf(vxradio1),"Color",'green','LineWidth',15)
plot(vxradio2,yf(vxradio2),"Color",'green','LineWidth',15)

%se crea la recta tangente y pendiente
%La recta tangente es la recta donde se derrapa el carro
vxTang=@(x) x:x+50;
%La recta pendiente son los 90 grados para saber donde graficar las gradas.  
vxPend=@(x) x-50:x;
x0=21.31;
x01 = 233.4343;
%se hace los calculos de la recta tangente y la recta pendiente
rectaTangente=@(x) yf(x)+dyf(x)*(vxTang(x)-x);
rectaPend=@(x) yf(x)+(-1/dyf(x))*(vxPend(x)-x);


%plot(vxPend(x0),rectaPend(x0),"Color","blue","LineWidth",7)
%hold on 

%plot(vxTang(x01),rectaTangente(x01),"Color","red","LineWidth",1)
%plot(vxPend(x01),rectaPend(x01),"Color","blue","LineWidth",7) 
%no sabemos porque no nos salio 90° entre la linea azul y la roja

% se hacelos rectangulos
p = plot([5.5  85.5 85.5 5.5 5.5] , [ 197  197  217  217 197],"Color",'yellow',"LineWidth",1); %Los puntos se iran uniendo en el orden que los vayas colocando
rotate(p, [0 0 5.5], 30, [5.5 197 0] ) ;%se configura en base a los valores del rectangulo para rotarlo
grid on
pbaspect([1 1 1])


%igual que en la anterior solo que para las gradas de la parte inferior derecha
p = plot([227.8  307.8 307.8 227.8 227.8] , [ -16  -16  -36  -36 -16],"Color",'yellow',"LineWidth",1); %Los puntos se iran uniendo en el orden que los vayas colocando
rotate(p, [0 0 227.8], 345, [227.8 -16 0] ) ;
grid on
pbaspect([1 1 1])


disp("Si ingresa un valor mayor de 14 va a haber derrape");
vUsr = input("Velocidad del auto: ");
xpd = @(x) sqrt(friccionS*g*dp(x))-vUsr;
xpderr = fzero(xpd,34);
x0=xpderr;
if (vUsr<=14)
    comet(zv,yf(zv))
    vUsr="Velocidad: "+num2str(vUsr);
    text(150,250,vUsr,"FontSize",15,"FontName","times") %mostrar velocidad en grafica
else
    wnc = (1/2)*752*vUsr^2;
    d = (vUsr^2)/(2*friccionC*g);
    plot(vxTang(x0),rectaTangente(x0),"Color","red","LineWidth",1);
    comet(vxTang(x0),rectaTangente(x0))

    wnc="Calor: "+num2str(wnc);
    text(150,250,wnc,"FontSize",15,"FontName","times") %mostrar calor en grafica

    d ="Distancia: "+num2str(d);
    text(150,220,d,"FontSize",15,"FontName","times") %mostrar long en grafica

end



%Aportes de los integrantes:

%Emilio Vidal: Modifique las curvas para que estuvieran mejor integradas, contribui en el
% proceso de encontrar  las zonas de derrape e integrando las gradas en el c
% odigo de manera en la cual la gente estuviera segura y ayude a
% implementar en el ultimo condicional.

%Fernando: Busque como desplegar el calor y la distancia en respectó al
%derrape.

%Rodrigo: Yo hice la fórmula que verifica en qué posición se derrapa.

%Sergio: Yo busqué cómo realizar la gráficas mediante el polinomio cúbico y
%asimismo ayudé en la implementación de fórmulas en la zona de curvas. Y ayude 
% meter las leyendas en el gráfico. 

