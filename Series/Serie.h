//? Sergio Tomás Vargas Villarreal A00837196

#ifndef Serie_h
#define Serie_h

#include <iostream>
#include <stdio.h>
#include <string>

using namespace std;

//*vamos a tener COMPOSICION en la clase serie -
#include "Episodio.h"

class Serie{
private:
    string iD;
    string titulo;
    int duracion;
    int calificacion;
    int cantEpisodios;
    string genero;  //{"innovacion","accion","documental"};
    Episodio episodios[5];
    
public:
    //metodo constructor de clase
    Serie();
    Serie(string _iD,string _titulo, int _duracion,string _genero,int _calificacion,int _cantEpisodios);
    
    //metodo modificador que cambia el valor de los atributos
    void setID(string _iD);
    void setTitulo(string _titulo);
    void setDuracion(int _duracion);
    void setGenero(string _genero);
    void setCalificacion(int _calificacion);
    void setCantidadEpisodios(int _cantEpisodios);
    
    //metodo de acceso que retorna el valor del atributo
    string getID();
    string getTitulo();
    int getDuracion();
    string getGenero();
    int getCalificacion();
    int getCantidadEpisodios();


    Episodio getEpisodio(int & index);
    void setEpisodio(int &index, Episodio epi); //*
    void calculaCalificacionPromedio();
    void addEpisodio(Episodio epi); //*Añade el episodio en la posición disponible
    void delEpisodio();
    
    //funcionalidad
    string str();
    
};
#endif /* Serie_hpp */