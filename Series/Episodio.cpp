//? Sergio Tomás Vargas Villarreal A00837196

#include <iostream>
#include <string>
#include "Episodio.h"


using namespace std;

Episodio::Episodio(){

}


Episodio::Episodio(string _titulo, int _temporada,int _calificacion){
    titulo = _titulo;
    temporada = _temporada;
    calificacion = _calificacion;
}

void Episodio::setTitulo(string _titulo){
    titulo = _titulo;
}

void Episodio::setCalificacion(int _calificacion){
    calificacion = _calificacion;
}

void Episodio::setTemporada(int _temporada){
    temporada = _temporada;
}


string Episodio::getTitulo(){
    return titulo;
}


int Episodio::getCalificacion(){
    return calificacion;
}



int Episodio::getTemporada(){
    return temporada;
}



string Episodio::str(){
    return titulo + "," + to_string(temporada) + "," + to_string(calificacion);
};