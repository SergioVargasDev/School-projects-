//? Sergio Tomás Vargas Villarreal A00837196

#include <iostream>
#include <string>
#include "Serie.h"




using namespace std;

Serie::Serie(){
//    int duracion = 0;
//    int calificacion = 0;
//    int cantEpisodios = 0;
}
Serie::Serie(string _iD,string _titulo, int _duracion,string _genero,int _calificacion,int _cantEpisodios){
    iD = _iD;
    titulo = _titulo;
    duracion = _duracion;
    genero = _genero;
    calificacion = _calificacion;
    cantEpisodios = _cantEpisodios;

}

//*Validar que el episodio index exista, si no existe index = -1 y retorno un epi 
//*si sí existe el episodio index retorno episodios [index]


Episodio Serie::getEpisodio(int &index){

    Episodio epi;

    if (index >= 0 && index < cantEpisodios){
        return episodios[index];
    
    }

    else {
        index = -1;
        return epi;

    }

}


void Serie:: setEpisodio(int &index, Episodio epi) {
    //*Validación de que exista el episodio index
    if (index>= 0 && index < cantEpisodios){
        episodios[index] = epi;

    }

    else {
        //*con esto le decimos al ing. que no existe ese episodio, no se pudo cambiar
        index = -1;

    }


}



//*Sumar todas las calificaciones de cada episodio de la serie
//*calcular el promedio y asignarlo al atributo calificacion - promedio de sus epidodios 
//* si no tiene episodios se le asigna un 0

void Serie::calculaCalificacionPromedio(){
    int acumulador = 0;

    //*acumular - sumar las calificacion de todos los episodios 
    for(int index = 0; index<cantEpisodios; index++){
        acumulador += episodios[index].getCalificacion();

    }

    //*cacular el promedio -VALIDAR - 
    if (cantEpisodios > 0){
        calificacion = acumulador / cantEpisodios;
    }

    else {
        calificacion = 0;
    }

}




void Serie::addEpisodio(Episodio epi) {
    //*validar que haya espacio para añadir el espacio

    if (cantEpisodios < 5){
            episodios[cantEpisodios++] = epi;


    }

}




 //*Añade el episodio en la posición disponible
void Serie::delEpisodio(){
    if (cantEpisodios >0){
        cantEpisodios --;


}




}
    
















        // Metodos modificadores
void Serie::setID(string _iD){
    iD = _iD;
}



void Serie::setTitulo(string _titulo){
    titulo = _titulo;
}



void Serie::setDuracion(int _duracion){
    duracion = _duracion;
}

void Serie::setGenero(string _genero){
    genero = _genero;
}




void Serie::setCalificacion(int _calificacion){
    calificacion = _calificacion;
}




void Serie::setCantidadEpisodios(int _cantEpisodios){
    cantEpisodios = _cantEpisodios;
}


        // Metodos de acceso

string Serie::getID(){
    return iD;
}

string Serie::getTitulo(){
    return titulo;
}


int Serie::getDuracion(){
    return duracion;
}


string Serie::getGenero(){
    return genero;
}



int Serie::getCalificacion(){
    return calificacion;
}



int Serie::getCantidadEpisodios(){
    return cantEpisodios;
}



string Serie::str(){
    string acumulador = "\n";

    for (int index = 0; index < cantEpisodios; index++){
        acumulador += "E" + to_string(index) + episodios[index].str() + "\n";

    }

    return iD + "," + titulo + "," + to_string(duracion) + "," + genero + "," + to_string(calificacion) + "," + to_string(cantEpisodios) + acumulador;

};  