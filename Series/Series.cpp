//? Sergio Tomás Vargas Villarreal A00837196
//? https://youtu.be/WM_yEpyUjhg
#include "Series.h"
#include <iomanip>





//* Aquí se estipula al constructor por default, donde la cantidad de series
//* se le adjudica el valor de 0. 
    Series:: Series()
    {
        cantidadSeries = 0;

    }

    //* Aquí se estipula la función setCantidadSeries. 
    void Series::setCantidadSeries(int _cantidadSeries)
    {
        cantidadSeries = _cantidadSeries;
    }


    //* Aquí se estipula la función getCantidadSeries. 
    int Series:: getCantidadSeries()
    {
        return cantidadSeries;

    }


//* Este es el método addSerie, dicho entrará en función si se cumple la condición de que haya un espacio disponible. 
//*Asimismo, se incrementa cuantitativamente en 1 la cantidadSeries. De no ser así, se despliega el "No se pudo agregar la serie".


void Series::addSerie(Serie _serie)
{

    if (cantidadSeries < 100)
    {
        arrSeries[cantidadSeries] = _serie;
        cantidadSeries++;
    }
    else{
        cout << "No se pudo agregar la serie en lo absoluto";

    }
}




//* Aquí se estipula que para todas las series que existan en el arreglo, se aplicará
//* el método calculaCalificaciónPromedio para poder agregar la calificación pertinente a la serie.

void Series::CalculaPromedioSerie()
{
    
    for(int indexSerie = 0 ; indexSerie < cantidadSeries; indexSerie ++)
    {
        arrSeries[indexSerie].calculaCalificacionPromedio();
    }
}



void Series::leerArchivo()
{
    string linea, dato;
    int index, columna;
    Episodio ep;
    Serie serie;
    ifstream lectura;
    
    lectura.open("Series22.csv",ios::in);
    index = 0;
    while (getline(lectura, linea)) // lee una serie
    {
        // cout << linea << endl; //borrar
            std::stringstream renglon{linea};
            
            columna = 0;
            while (getline(renglon, dato, ',')) // separa los elementos,
            {
                switch (columna++)
                {
                    case 0: // iD
                        serie.setID(dato);
                        break;
                    case 1: // Titulo
                        serie.setTitulo(dato);
                        break;
                    case 2: // duracion
                        serie.setDuracion(stoi(dato));
                        break;
                    case 3: // genero
                        serie.setGenero(dato);
                        break;
                    case 4: // calificación promedio
                        serie.setCalificacion(stoi(dato));
                        break;
                    case 5: //cant episodios - inicializar con 0 episodios todas las series
                        serie.setCantidadEpisodios(0);
                        break;
                }
            }// fin while
            
            // para verificar si se guardo correctamente
           // cout << serie.str( ) << endl;
            addSerie(serie);
        
            //cout << "*********  se añadio una serie - Cantidad de series ="  <<  cantidadSeries << endl;
            
        }
        lectura.close();
        
        // LEER LOS EPISODIOS DE LAS SERIES
        index = 0;
        
        // IMPORTANTE - COPIA EL PATH DE TU ARCHIVO CUANDO LO SUBAS A GITHUB SOLO DEJA EL NOMBRE
        lectura.open("Episodios22.csv", ios::in);
        while ( getline(lectura, linea))
        {
          //  cout << linea << endl; // se borra
            std::stringstream renglon(linea);
            columna = 0;
            while (getline(renglon, dato, ',')) // separar los elementos,
            {
                switch (columna++)
                {
                    case 0:
                        index = stoi(dato) - 1;  // a qué serie pertenece?
                        break;
                    case 1: // Titulo
                        ep.setTitulo(dato);
                        break;
                    case 2: // temporada
                        ep.setTemporada(stoi(dato)); // string to int
                        break;
                    case 3: // calificacion
                        ep.setCalificacion(stoi(dato)); // string to double
                        break;
                }
            } // al salir de aqui ya se separo toda la línea
            
            arrSeries[index].addEpisodio(ep);
        }
        
        lectura.close();
    }




//*Aquí dicha función corrobora si existe dicho género en el arreglo de géneros, si llega a existir, 
//* se retorna la posición donde se encuentra el arreglo. 
//* Posteriormente el arreglo de géneros con la posición se convertira en el género y se retornará la cantidad por 1 más.
int existe_genero(std::string arrGeneros[], int &cantidad, std::string genero){
    for (int index = 0; index < cantidad; index++){
        if (arrGeneros[index] == genero)
            return index;
    }
    arrGeneros[cantidad] = genero;
    return cantidad++;
    
    
        
}






void Series::reporteFrecuenciasYPromedioSeries()
{
    //*recorrer todo el arreglo de series con un ciclo for
    //*desplegar la información de la serie usando el método str()
    //*incremenrar el acumuladorPromedio con la calificación de la serie [index] para la serie [index] sacar su genero
    
    //*Aquí se declara un arreglo de carácter string con capacidad absoluta de 100.
    string Generos[100];

    //*sSe declara un arreglo para contar las frecuencias, inicializarlo con 0, 0, 0, 0, 0.
    int frecuencias[]= {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0};
    //*Aquí se declara la variable genero de carácter string.
    string genero; 
    //*Se declaran las variables de carácter int
    int frecuenciaRelativa, acumulador, cantidadDeGeneros, acumuladorPromedio, posicionGenero;
    //*
    //* Se inicializa la variable cantidadDeGeneros con 0
    cantidadDeGeneros = 0;
    //* Se inicializa la variable acumuladorPromedio con 0
    acumuladorPromedio = 0;

    //*Aquí se hace un reporte donde con un for se va desplanzando entre la cantidad de series
    //* que hay y entra a un acumulador donde se le agrega la calificación de la serie y con el 
    //* método str se finiquita. 
    cout << "Reporte" << endl;
    for (int index = 0; index < cantidadSeries; index++){

        acumuladorPromedio = acumuladorPromedio + arrSeries[index].getCalificacion();
        cout << arrSeries[index].str() << endl;

        posicionGenero = existe_genero(Generos, cantidadDeGeneros, arrSeries[index].getGenero());
        frecuencias[posicionGenero]++;
    }

    //* Aquí se inicializa el acumulador con 0. 
        acumulador = 0;

        //*
    
    cout << "Frecuencias"<< endl;
        for(int index = 0; index < cantidadDeGeneros; index ++){
            frecuenciaRelativa = double(frecuencias[index]) / cantidadSeries * 100;
            
            acumulador = acumulador + frecuencias[index];
            
            cout << Generos[index] <<","  << frecuencias[index] <<"," << frecuenciaRelativa  << endl;
        }
        

    cout << "Total="<< cantidadSeries<<endl;
        if (cantidadSeries > 0){
            cout << "Promedio=" << acumuladorPromedio / cantidadSeries << endl;
        }

        else{
            cout << "No se puede calcular la calificación promedio en lo absoluto\n";
        }
}
            