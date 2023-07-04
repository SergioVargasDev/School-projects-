//? Sergio Tomás Vargas Villarreal A00837196

#ifndef Episodio_h
#define Episodio_h

#include <iostream>
#include <stdio.h>
#include <string>

using namespace std;

class Episodio{
private:
    string titulo;
    int temporada;
    int calificacion;
    
public:
    Episodio();
    Episodio(string _titulo, int _temporada,int _calificacion);
    void setTitulo(string);
    void setTemporada(int);
    void setCalificacion(int);
    
    
    string getTitulo();
    int getTemporada();
    int getCalificacion();
    string str();
    
};

#endif /* Episodio_h */